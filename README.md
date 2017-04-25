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
    DEFAULT_FILE_STORAGE = 'filebrowser_s3.storage.S3MediaStorage'

    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

    AWS_LOCATION = env('AWS_LOCATION')
    FILEBROWSER_DIRECTORY = AWS_LOCATION

    MEDIA_ROOT = ''

    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN', default=None)
    if AWS_S3_CUSTOM_DOMAIN is None:
        MEDIA_URL = '...your public AWS bucket URL with protocol and trailing slash'
    else:
        MEDIA_URL = 'https://' + AWS_S3_CUSTOM_DOMAIN + '/'


else:
    MEDIA_ROOT = ...
    MEDIA_URL = ...
```

## Variables documentation

When using the s3 storage class, required setting variables are:

- `DEFAULT_FILE_STORAGE`- This must be `filebrowser_s3.storage.S3MediaStorage` for obvious reasons.
- `AWS_ACCESS_KEY_ID` - Your AWS access key.
- `AWS_SECRET_ACCESS_KEY` - Your AWS secret.
- `AWS_STORAGE_BUCKET_NAME` - The bucket name to use on your AWS account.
- `AWS_S3_CUSTOM_DOMAIN` - Whatever custom domain you need used, such as "assets.mydomain.com".
- `MEDIA_ROOT` - The Mezzanine filesystem root. When using the S3 storage class this should be set to `''`.
- `MEDIA_URL` - The fully qualified domain URL that Mezzanine can link to. This includes the protocol and trailing slash, and so will typically be of the form `'https://' + AWS_S3_CUSTOM_DOMAIN + '/'`.

There are also two fairly special variables that must be specified:

- `AWS_LOCATION` - Used by django-storages as your S3 "top level" directory for uploads.
- `FILEBROWSER_DIRECTORY` - Used by filebrowser_safe as the "top level" directory in which to browse. 

You typically want these two values to be the same. So that the media browser looks for uploaded images in the same top level "directory" that botos3 treats as top level upload path.
