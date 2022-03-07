# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from minio import Minio
from minio.error import S3Error
class FileUpload(APIView):
    def getMinioClient(self,access , secret):
        return Minio(
            'localhost:9000',
            access_key=access,
            secret_key=secret,
            secure =False
        )
    def post(self,request):
        try:
            data = request.data
            file_name = data["file"]
            # file_src = data['path']
            file_size =file_name.size
            #now upload to s3 bucket or your media file
            minioClient = self.getMinioClient('testkey','testsecretkey')
            if (not minioClient.bucket_exists('testbucket')):
                try:
                    minioClient.make_bucket('testbucket')
                except :
                    raise
            try:
                # statdata = os.stat('requirments.txt')
                minioClient.put_object(
                    'testbucket',
                    str(file_name),
                    file_name,
                    file_size
                )
            except Exception as e:
                raise
            
        except Exception as e:
            print (e)
            return Response({"error":"error to upload a file"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse({"message":"file added . "} , status=status.HTTP_202_ACCEPTED)





















# from rest_framework.response import Response
# # Create your views here.

# class AddFiles(APIView):
#     parser_classes = [FileUploadParser]

#     def put(self, request, format=None):
#         file_obj = request.data['file']
#         # ...
#         # do some stuff with uploaded file
#         # ...
#         return Response(status=204)

#     # def post(self, request, format='pdf'):
#     #     up_file = request.FILES['file']
#     #     destination = open(up_file.name, 'wb+')
#     #     for chunk in up_file.chunks():
#     #         destination.write(chunk)
#     #     destination.close()  # File should be closed only after all chuns are added

#     #     # ...
#     #     # do some stuff with uploaded file
#     #     # ...
#     #     return Response(up_file.name, status.HTTP_201_CREATED)