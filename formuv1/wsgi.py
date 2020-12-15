"""
@author: Vanderlino Coelho Barreto Neto

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'formuv1.settings')

application = get_wsgi_application()


"""
@author: Vanderlino Coelho Barreto Neto

"""