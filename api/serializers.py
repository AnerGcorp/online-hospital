from rest_framework import serializers
from hospital.models import Hospital_Information, Patient, User
from doctor.models import Doctor_Information

# Serialization --> convert python data (from our database models) to JSON data

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Information
        fields = "__all__"

class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Information
        fields = "__all__"

class HospitalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital_Information
        fields = '__all__'

class HospitalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital_Information
        fields = "__all__"

# class ProjectSerializer(serializers.ModelSerializer):
#     owner = ProfileSerializer(many=False)
#     tags = TagSerializer(many=True)
#     reviews = serializers.SerializerMethodField()

#     class Meta:
#         model = Project
#         fields = '__all__'

#     def get_reviews(self, obj):
#         reviews = obj.review_set.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return serializer.data
