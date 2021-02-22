
import string
import random
from rest_framework import serializers
from .models import Schools, Students


class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = ('sc_name', 'sc_max_st')

    def create(self, validated_data):
        """Create and return a new patient"""

        if int(validated_data["sc_max_st"]) > 0:
            patient = Schools(
                sc_name=validated_data["sc_name"],
                sc_max_st=validated_data["sc_max_st"]
            )
            patient.save()
            return patient
        else:
            raise serializers.ValidationError("Maximum number of student should be Positive")


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('st_first_name', 'st_last_name',  'st_school')

    def create(self, validated_data):
        """Create and return a new patient"""

        def check_max():
            max_std = Schools.objects.get(id=validated_data["st_school"].id).sc_max_st
            cur_std = Students.objects.filter(st_school=validated_data["st_school"].id).count()
            return True if cur_std <= max_std else False

        if check_max():

            patient = Students(
                st_first_name=validated_data["st_first_name"],
                st_last_name=validated_data["st_last_name"],
                st_ident=''.join(random.choices(string.digits, k=6)),
                st_school=validated_data["st_school"]
            )
            patient.save()
            return patient

        else:
            raise serializers.ValidationError("Number of students in this school is maximum")
