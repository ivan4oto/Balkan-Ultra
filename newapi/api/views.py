from .models import Athletes, Racelinks
from .serializers import AthletesSerializer
from .my_mail import my_mail_send
from .messages import success_msg

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from django.core.mail import send_mail


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverview(request):
    api_urls = {
        'List': '/athlete-list/',
        'Create': '/athlete-create/',
    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def athleteList(request):
    athletes = Athletes.objects.filter(approved=True)
    serializer = AthletesSerializer(athletes, many=True, fields=('first_name', 'last_name', 'gender', 'distance'))
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def athleteCreate(request):
    serializer = AthletesSerializer(data=request.data)
    if serializer.is_valid():
        a = serializer.save()
        a.save()
    else:
        return Response(serializer.errors)
    link = request.data.get('link')
    athlete_fullname = a.first_name + ' ' + a.last_name
    racelink = Racelinks(athlete=a, link=link, athlete_name=athlete_fullname)
    racelink.save()
    my_mail_send(a.email, 'BalkanUltra. Your registration is successful.',
                 success_msg.format(athlete_fullname, a.email, a.distance))
    return Response(request.data)