from storages.backends.s3boto3 import S3Boto3Storage

# To override
class MediaStorage(S3Boto3Storage):
    location = 'media'   # empty the location
    