from rest_framework.views import APIView
from stats.models import LogClient
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import serializers
#import Q
from django.db.models import Q
#import settings
from django.conf import settings

class StatsView(APIView):

    model = LogClient
    permission_classes = [IsAuthenticated, ]

    class OutputSerializer(serializers.Serializer):
        type = serializers.CharField()
        data = serializers.JSONField()

    def get(self, request):
        stats = self.model.objects.all()
        # like Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50

        _data_AppWidgetSummary = [
            {
                'name': 'Visitas en windows',
                'type': 'windows',
                'value': stats.filter(agent__contains='Windows').count(),
                'color': 'primary'
            },
            {
                'name': 'Visitas en android',
                'type': 'android',
                'value': stats.filter(agent__contains='Android').count(),
                'color': 'success'
            },
            {
                'name': 'Visitas en ios',
                'type': 'apple',
                'value': stats.filter(agent__contains='Darwin').count(),
                'color': 'secondary'
            }
        ]

        

        _data_AppWebsiteVisits = {
            "chartLabels": ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'],

            "chartData": [
                {
                    "name": "Visitas en windows",
                    "data": [stats.filter(fecha__month=1, agent__contains='Windows').count(), stats.filter(fecha__month=2, agent__contains='Windows').count(),
                             stats.filter(fecha__month=3, agent__contains='Windows').count(), stats.filter(
                                 fecha__month=4, agent__contains='Windows').count(), stats.filter(fecha__month=5, agent__contains='Windows').count(),
                             stats.filter(fecha__month=6, agent__contains='Windows').count(), stats.filter(fecha__month=7, agent__contains='Windows').count()],
                    "fill": 'solid',

                },
                {
                    "name": "Visitas en android",
                    "data": [stats.filter(fecha__month=1, agent__contains='Android').count(), stats.filter(fecha__month=2, agent__contains='Android').count(),
                             stats.filter(fecha__month=3, agent__contains='Android').count(), stats.filter(
                        fecha__month=4, agent__contains='Android').count(), stats.filter(fecha__month=5, agent__contains='Android').count(),
                        stats.filter(fecha__month=6, agent__contains='Android').count(), stats.filter(fecha__month=7, agent__contains='Android').count()],
                    "fill": 'solid',
                },
                {
                    "name": "Visitas en ios",
                    "data": [stats.filter(fecha__month=1, agent__contains='Darwin').count(), stats.filter(fecha__month=2, agent__contains='Darwin').count(),
                                stats.filter(fecha__month=3, agent__contains='Darwin').count(), stats.filter(  
                        fecha__month=4, agent__contains='Darwin').count(), stats.filter(fecha__month=5, agent__contains='Darwin').count(),
                        stats.filter(fecha__month=6, agent__contains='Darwin').count(), stats.filter(fecha__month=7, agent__contains='Darwin').count()],
                    "fill": 'solid',
                }
            ]

        }

        labels = stats.distinct('request_url').exclude(
            Q(request_url__contains=settings.MEDIA_URL) | Q(request_url__contains='static') | Q(request_url__contains='admin')
            
        ).values_list('request_url', flat=True)
        _AppCurrentVisits = []
        for l in labels:
            _AppCurrentVisits.append({
                'label': l,
                'value': stats.filter(request_url=l).count()
            })



        final = [
            {
                'type': 'AppWidgetSummary',
                'data': _data_AppWidgetSummary
            },
            {
                'type': 'AppWebsiteVisits',
                'data': _data_AppWebsiteVisits
            },
            {
                'type': 'AppCurrentVisits',
                'data': _AppCurrentVisits
            }
        ]

        _final = self.OutputSerializer(final, many=True)
        
        return Response(_final.data, status=status.HTTP_200_OK,headers={'Access-Control-Allow-Origin': '*'})
