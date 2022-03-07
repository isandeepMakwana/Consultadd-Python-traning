
from minio import Minio
from minio.error import S3Error 
import os

def getMinioClient(access , secret):
    return Minio(
        'localhost:9000',
        access_key=access,
        secret_key=secret,
        secure =False
    )


if __name__ == '__main__':
    minioClient = getMinioClient('testkey','testsecretkey')

    if (not minioClient.bucket_exists('testbucket')):
        try:
            minioClient.make_bucket('testbucket')
        except :
            raise

# # add file in bucket
    try:
        with open ('requirments.txt','rb') as testfile:
            statdata = os.stat('requirments.txt')
            minioClient.put_object(
                'testbucket',
                'miniotest.txt',
                testfile,
                statdata.st_size
            )
    except Exception as e:
        raise


# remove file from bucket

    # try:
    #     minioClient.remove_object('testbucket','miniotest.txt')
    # except Exception as e:
    #     pass