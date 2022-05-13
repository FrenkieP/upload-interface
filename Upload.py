#Upload
import os
from pprint import pprint
from google.cloud import storage
credential_path = r"C:\Users\User\Desktop\SerViceKey_GoogleCloud.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

storage_client = storage.Client()

def upload_to_bucket(blob_name,file_path,bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False
file_path = r'C:\Users\User\Desktop'
upload_to_bucket('file11',os.path.join(file_path,'q.txt'),'keygen1_bucket')