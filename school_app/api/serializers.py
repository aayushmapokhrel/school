from rest_framework import serializers
from school_app.models import School, Student, Teacher


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_age(self, value):
        if value < 5 or value > 20:
            raise serializers.ValidationError("Age must be between 5 and 20")
        return value

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
