import sys, os
INTERP = "/home/lorger2/hillandgertner.com/venv/bin/python"
#INTERP is present twice so that the new python interpreter knows the actual executable path 
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd)  #You must add your project here

sys.path.insert(0,cwd+'/venv/bin')
sys.path.insert(0,cwd+'/venv/lib/python2.7/site-packages/django')
sys.path.insert(0,cwd+'/venv/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "hillandgertner.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
