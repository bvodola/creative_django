import socket

"""
Check Enviroment
"""

DEV_HOST = 'MacBook-Air-de-Brunno.local'
PROD_HOST = 'web540.webfaction.com'

if socket.gethostname() == DEV_HOST:
	from .settings_dev import *
elif socket.gethostname() == PROD_HOST:
	from .settings_prod import *
else:
	raise Exception("Cannot determine execution mode for host '%s'.  Please check DEV_HOST and PROD_HOST in settings_env.py." % socket.gethostname())
