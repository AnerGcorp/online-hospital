from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from .serializers import (
    HospitalListSerializer,
    HospitalDetailSerializer,
    DoctorListSerializer,
    DoctorDetailSerializer
    )
from hospital.models import Hospital_Information, Patient, User
from doctor.models import Doctor_Information

@api_view(['GET'])
def getRoutes(request):
    # Specify which urls (routes) to accept
    routes = [
        {'GET': '/api/hospital/'},
        {'GET': '/api/hospital/id'},

        # to test built-in authentication - JSON web tokens have an expiration date
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)

# @permission_classes([IsAuthenticated]) # set up a restricted route

@api_view(['GET'])
def getHospitals(request):
    hospitals = Hospital_Information.objects.all() # query the database (get python object)
    serializer = HospitalListSerializer(hospitals, many=True) # convert python object to JSON object
    # many=True because we are serializing a list of objects
    return Response(serializer.data)


@api_view(['GET'])
def getHospitalProfile(request, pk):
    hospitals = Hospital_Information.objects.get(hospital_id=pk)
    serializer = HospitalListSerializer(hospitals, many=False) # many=False for a single object
    return Response(serializer.data)


class HospitalListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = HospitalListSerializer
    queryset = Hospital_Information.objects.all()

class HospitalDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = HospitalDetailSerializer
    queryset = Hospital_Information.objects.all()

class DoctorListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DoctorListSerializer
    queryset = Doctor_Information.objects.all()

class DoctorDetailView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DoctorDetailSerializer
    queryset = Doctor_Information.objects.all()

