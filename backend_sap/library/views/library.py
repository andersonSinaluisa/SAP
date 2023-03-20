from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from library.services.library import createLibrary

from core.shared.permission import UserPermission
from rest_framework import serializers, status
from library.models import Library
from core.shared.pagination import Pagination
import difflib
import docx2txt
import PyPDF2

class LibraryCreate(APIView):

    permission_classes = (IsAuthenticated,)

    parser_classes = (MultiPartParser, )

    class InputSerializer(serializers.Serializer):
        author = serializers.CharField()
        description = serializers.CharField()
        file = serializers.FileField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Library
            fields = '__all__'

    def post(self, request):

        data = request.data

        serializer = self.InputSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        author = serializer.validated_data['author']
        description = serializer.validated_data['description']
        file = serializer.validated_data['file']
        user_id = request.user.id
        type_doc = file.name.split('.')[-1]

        library = createLibrary(author, file, description, user_id, type_doc)

        serializer = self.OutputSerializer(library)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LibraryList(APIView):

    permission_classes = (IsAuthenticated, UserPermission)
    model = Library
    permission_required = 'library.view_library'

    class InputSerializer(serializers.Serializer):
        perPage = serializers.IntegerField()
        page = serializers.IntegerField()

    class OutputSerializer(serializers.ModelSerializer):
        documento = serializers.FileField()

        class Meta:
            model = Library
            fields = '__all__'

    def get(self, request):
        paginator = Pagination()
        libraries = Library.objects.all().order_by('-fecha_subida')
        result_page = paginator.paginate_queryset(libraries, request)
        serializer = self.OutputSerializer(result_page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LibraryCompare(APIView):

    permission_classes = (IsAuthenticated,UserPermission)
    model = Library
    permission_required = 'library.view_library'

    def readPdf(self, file):
        text = ""
        documentoLectorBiblioteca = PyPDF2.PdfFileReader(file)
        numero_paginas_biblioteca_doc = documentoLectorBiblioteca.numPages
        for numero_de_pagina in range(numero_paginas_biblioteca_doc):
                # OBTENGO LA PAGINA POR NUMERO DE PAGINA
            pageobj = documentoLectorBiblioteca.getPage(numero_de_pagina)
                # EXTRIGO EL TEXTO DE ESA PAGINA
            text += pageobj.extractText()
        return text

    def readDoc(self, file):

        text = docx2txt.process(file)
        return text

    class InputSerializer(serializers.Serializer):
        file1 = serializers.FileField()
        file2 = serializers.FileField()

    class OutputSerializer(serializers.Serializer):
        percent = serializers.FloatField()
        text = serializers.CharField()

    def post(self, request):
            
        data = request.data

        serializer = self.InputSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        file1 = serializer.validated_data['file1']
        file2 = serializer.validated_data['file2']

        

        if file1.name.split('.')[-1] == 'pdf':
            text1 = self.readPdf(file1)
        else:
            text1 = self.readDoc(file1)

        if file2.name.split('.')[-1] == 'pdf':
            text2 = self.readPdf(file2)
        else:
            text2 = self.readDoc(file2)
        
        author = "Comparacion"
        description = file1.name
        user_id = request.user.id
        type_doc = file1.name.split('.')[-1]
        
        createLibrary(author, file1, description, user_id, type_doc)


        #save file2
        type_doc = file2.name.split('.')[-1]
        description = file2.name

        createLibrary(author, file2, description, user_id, type_doc)

        percent = difflib.SequenceMatcher(None, text1, text2).ratio()

        text_final = ""
        matcher = difflib.SequenceMatcher(None, text1, text2)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                text_final += text1[i1:i2]
        #transform percent 0 a 1 to 0 a 100
        percent = percent * 100
        serializer = self.OutputSerializer({'percent': percent, 'text': text_final})

        return Response(serializer.data, status=status.HTTP_200_OK)
