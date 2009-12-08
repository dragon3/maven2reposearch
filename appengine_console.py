#!/usr/bin/env python
import code
import getpass
import sys
import os

g_path = os.environ['HOME'] + "/google_appengine"
extra_path = [
  g_path,
  os.path.join(g_path, 'lib', 'antlr3'),
  os.path.join(g_path, 'lib', 'webob'),
  os.path.join(g_path, 'lib', 'django'),
  os.path.join(g_path, 'lib', 'yaml', 'lib')
]
sys.path = extra_path + sys.path

from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db

def auth_func():
  return raw_input('Username:'), getpass.getpass('Password:')

if len(sys.argv) < 2:
  print "Usage: %s app_id [host]" % (sys.argv[0],)
app_id = sys.argv[1]
if len(sys.argv) > 2:
  host = sys.argv[2]
else:
  host = '%s.appspot.com' % app_id

remote_api_stub.ConfigureRemoteDatastore(app_id, '/remote_api', auth_func, host)

code.interact('App Engine interactive console for %s' % (app_id,), None, locals())
