import boto3


class S3Uploader:
 def __init__(self, aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token=None):
     if aws_session_token:
         self.s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)
     else:
         self.s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
     self.bucket_name = bucket_name

 def upload_file(self, file_name, object_name=None):
     if object_name is None:
         object_name = file_name

     self.s3.upload_file(file_name, self.bucket_name, object_name)
    
    


