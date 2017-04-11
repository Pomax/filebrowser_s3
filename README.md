# filebrowser-s3: an AWS S3 fix for Mezzanine's media manager

This app overrides the default Mezzanine filebrowser to do "the same but then using AWS S3".

## Installation

Use pip:

```
$> pip install filebrowser-s3
```

## Using filebrowser-s3 with Mezzanine

In your Mezzanine settings.py (or local settings file), add filebrowser_s3 as an installed app:

```
INSTALLED_APPS = [
   ...,
   'filebrowser-s3',
]
```

You will also need to update the templates settings to make Mezzanine aware of the `s3thumbnails` template directive:

```
TEMPLATES = [
    {
    	...
        'OPTIONS': {
            ...
            'libraries': {
            	...
                's3thumbnails': 'filebrowser-s3.templatetags.s3thumbnails'
            }
        },
    },
]
```

Finally, you will need to make sure that s3 storage is used as default storage option (the following example code assumes an `env()` function for intelligently fetching environment variables):

```
# Storage for user generated files
USE_S3 = env('USE_S3')

if USE_S3:
    # Use S3 to store user files if the corresponding environment var is set.
    DEFAULT_FILE_STORAGE = 'networkapi.filebrowser_s3.storage.S3MediaStorage'

    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')
    AWS_LOCATION = env('AWS_STORAGE_ROOT', default=None)

    MEDIA_URL = 'https://' + env('AWS_S3_CUSTOM_DOMAIN') + '/'
    MEDIA_ROOT = ''
    FILEBROWSER_DIRECTORY = ''


else:
    # Otherwise use the default filesystem storage with whatever local settings necessary.
    MEDIA_ROOT = ...
    MEDIA_URL = ...
```
