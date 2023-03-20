from stats.models import LogClient
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
from django.utils import timezone

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Aquí puedes procesar la solicitud entrante
        # antes de pasarla a la vista correspondiente
        # por ejemplo, puedes agregar encabezados a la solicitud
        # o verificar si el usuario está autenticado

        # Se crea un registro de log para cada solicitud
        client_ip, is_routable = get_client_ip(request)
        location = None
        ip_type =""
        if client_ip is None:
        # Unable to get the client's IP address
            pass
        else:
            # We got the client's IP address
            if is_routable:
                # The client's IP address is publicly routable on the Internet
                ip_type = "Public"
                pass
            else:
                # The client's IP address is private
                ip_type = "Private"
                pass
        try:
            location = DbIpCity.get(ip_address, api_key='free').to_json()
        except Exception as e:
            response = None
        
        LogClient.objects.create(
            action_type=request.method,
            agent=request.META.get('HTTP_USER_AGENT'),
            ip=client_ip,
            asn=request.META.get('HTTP_X_FORWARDED_FOR'),
            browser=request.META.get('HTTP_USER_AGENT'),
            device=request.META.get('HTTP_CF_DEVICE_TYPE'),
            language=request.META.get('HTTP_ACCEPT_LANGUAGE'),
            user_id=request.user if request.user.is_authenticated else None,
            
            city = location.city if location else '' ,
            region = location.region if location else '',
            country = location.country if location else '',
            latitude = location.latitud if location else '',
            longitude = location.longitude if location else '',
            continent= location.region if location else '',
            domain=request.META.get('HTTP_HOST'),
            endpoint= request.META.get('PATH_INFO'),
            fecha=timezone.now(),
            ip_type=  ip_type,
            isp=  '',
            os=  '',
            request_method=  request.method,
            currency=   '',
            organization=   '',
            timezone=   '',
            page_title= request.path,
            page_url= request.path,
            platform=  request.META.get('HTTP_CF_DEVICE_TYPE'),
            request_url=  request.path,
            status_code=  0,
            status_text=  "",
            type_request=  'API',
            version=  '',


        )


        response = self.get_response(request)

        # Aquí puedes procesar la respuesta de la vista
        # por ejemplo, puedes agregar encabezados a la respuesta
        # o agregar información adicional al cuerpo de la respuesta

        return response