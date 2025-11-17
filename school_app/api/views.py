from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from school_api.models import School, Student, Teacher
from school_api.serializers import (
    SchoolSerializer,
    StudentSerializer,
    TeacherSerializer
)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('id')
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("school")
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related("school")
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
