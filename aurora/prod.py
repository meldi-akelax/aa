import os 
import dj_database_url
from .settings import * 

DATABASES['default'] = dj_database_url.config()
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'