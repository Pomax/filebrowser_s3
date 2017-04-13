# filebrowser_s3: an AWS S3 fix for Mezzanine's media manager

This app overrides the default Mezzanine filebrowser to do "the same but then using AWS S3".

## Installation

Use pip:

```
$> pip install filebrowser_s3
```

## Using filebrowser_s3 with Mezzanine

In your Mezzanine settings.py (or local settings file), add filebrowser_s3 as an installed app:

```
INSTALLED_APPS = [
   ...,
   'filebrowser_s3',
]
```

You will need to make sure that the correct storage class is used as `DEFAULT_FILE_STORAGE`. You could do this with a straight assignment, but conditional switching is recommended, as in the following example code assumes an `env()` function for intelligently fetching environment variables):

```
# Determine which storage solution to use. Typically, you
# want filesystem storage for local dev work, but S3 storage
# for staging/production instances.
USE_S3 = env('USE_S3')

if USE_S3:
    # use filebrowser_s3 rather than plain filebrowser_safe
    DEFAULT_FILE_STORAGE = 'filebrowser_s3.storage.S3MediaStorage'

    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    
    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')
    AWS_LOCATION = env('AWS_STORAGE_ROOT', default=None)

    MEDIA_URL = 'https://' + AWS_S3_CUSTOM_DOMAIN + '/'
    MEDIA_ROOT = ''
    
    # Make sure to explicitly set this to an empty string
    FILEBROWSER_DIRECTORY = ''

else:
    # Otherwise leave Mezzanine to use the default filesystem storage
    MEDIA_ROOT = ...
    MEDIA_URL = ...
```

Note that `FILEBROWSER_DIRECTORY` should typically be fixed to be an empty string. This variable is preassigned a value in default Mezzanine installations, but needs to be cleared explicitly when interfacing with S3. If you don't, its value will end up injected into your AWS bucket/file location and things will probably go wrong.
