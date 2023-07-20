from django.urls import path
from .views import (
    getRoutes,
    getHospitals,
    getHospitalProfile,
    HospitalListView,
    HospitalDetailView,
    DoctorListView,
    DoctorDetailView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('test/', getRoutes),
    path('hospital/', getHospitals),
    path('hospital/<int:pk>/', getHospitalProfile),

    path('hospitals/', HospitalListView.as_view(), name='hospitals'),
    path('hospitals/<pk>', HospitalDetailView.as_view(), name='hospital-detail'),
    path('doctors/', DoctorListView.as_view(), name='doctors'),
    path('doctors/<pk>', DoctorDetailView.as_view(), name='doctor-detail')
]
