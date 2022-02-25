from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee , Department
# Create your views here.

class Employees(APIView):
    def get_data_by_id(self, id):
        try:
            db_data = Employee.objects.get(id=id)
            return db_data
        except:
            return Response({
                "error":"data is not exists !!"
            } , status=status.HTTP_404_NOT_FOUND)

    def get(self , request):
        db_data = Employee.objects.all();
        serializer = EmployeeSerializer(db_data , many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data)
        else:
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        id = self.request.query_params.get('id')
        db_data = self.get_data_by_id(id)
        serializer = EmployeeSerializer(db_data , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    def delete(self ,request):
        db_data = self.get_data_by_id(self.request.query_params.get('id'))
        db_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SingleEmployee(APIView):
    def get(self , request , id):
        db_data = Employees().get_data_by_id(id)
        ser = EmployeeSerializer(db_data)
        return Response(ser.data)
