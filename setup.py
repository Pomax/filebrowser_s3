from distutils.core import setup
setup(
  name = 'filebrowser-s3',
  packages = ['filebrowser-s3'], # this must be the same as the name above
  version = '0.0.2',
  description = 'an S3 fix for Mezzanine\'s media manager',
  author = 'Mozilla Foundation',
  author_email = 'pomax@mozillafoundation.org',
  url = 'https://github.com/Pomax/filebrowser-s3',
  download_url = 'https://github.com/Pomax/filebrowser-s3/archive/0.0.2.tar.gz',
  keywords = ['mezzanine', 'filebrowser', 'filebrowser_safe', 'aws', 's3'],
  classifiers = [],
)