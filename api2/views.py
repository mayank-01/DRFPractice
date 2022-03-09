from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin



# >>>>>>>>>>>>>>>>>> Generic api_view and Mixins <<<<<<<<<<<<<<<<<<<<

class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# >>>>>>>>>>>>>>>>>> Class Based api_view <<<<<<<<<<<<<<<<<<<<


# class StudentAPI(APIView):
#     def get(self, request, id=None, format=None):
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'})
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

#     def put(self, request, id=None, format=None):
#         stu = Student.objects.get(id=id)
#         serializer =StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, id=None, format=None):
#         stu = Student.objects.get(id=id)
#         serializer =StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data Updated'})
#         return Response(serializer.errors)

#     def patch(self, request, id=None, format=None):
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         return Response({'msg': 'Data Deleted'})



# >>>>>>>>>>>>>>>>>> Function Based api_view <<<<<<<<<<<<<<<<<<<<


# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def studentapi(request, id=None):
#     if request.method == "GET":
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'})
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

#     if request.method == 'PUT':
#         stu = Student.objects.get(id=id)
#         serializer =StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PATCH':
#         stu = Student.objects.get(id=id)
#         serializer =StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data Updated'})
#         return Response(serializer.errors)

#     if request.method == 'DELETE':
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         return Response({'msg': 'Data Deleted'})
