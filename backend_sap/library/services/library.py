from library.models import Library

import datetime

def createLibrary(author, file, description, user_id,type_doc):

    """Create a new library.

    Returns:

        Library: The created library.

    """

    library = Library.objects.create(
        autor= author,
        descripcion= description,
        fecha_subida= datetime.date.today().strftime("%Y-%m-%d"),
        documento = file,
        id_usuario_id= user_id,
        type_doc = type_doc
    )


    return library