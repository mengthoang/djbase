'''
Created on May 17, 2020

@author: User
'''
from django.core.files.base import ContentFile
import base64, secrets

class FileUtil(object):
    
    @classmethod
    def get_file_from_data_url(cls, data_url):
        # getting the file format and the necessary dataURl for the file
        file_format, dataurl       = data_url.split(';base64,')
        # file name and extension
        filename, extension   = secrets.token_hex(20), file_format.split('/')[-1]
        # generating the contents of the file
        file = ContentFile( base64.b64decode(dataurl), name=f"{filename}.{extension}")
        # file and filename
        return file, ( filename, extension )