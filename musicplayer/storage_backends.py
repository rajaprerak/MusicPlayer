from storages.backends.s3boto3 import S3Boto3Storage 

class MediaStorage(S3Boto3Storage):    
    bucket_name = 'music-player-bucket'
    location = 'media'    
    file_overwrite = False
    default_acl = 'public'
    
# class StaticStorage(S3Boto3Storage):
#     bucket_name = 'music-player-bucket'
#     location = 'static'
#     default_acl = 'public'