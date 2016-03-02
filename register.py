#!/usr/bin/env python

import cgi
import cgitb
import json
import re

cgitb.enable()

form = cgi.FieldStorage()

if 'name' not in form or 'email' not in form:
    print json.dumps({ 'status' : False, 'msg' : 'Name or e-mail not in form' })
    exit(0)

name = form['name']
email = form['email']

print 'Content-Type: application/json'     # HTML is following
print                               # blank line, end of headers

name = re.sub('[\W ]+', '', name.value)
email = re.sub('[\W_@\.]+', '', email.value)

f = open('/var/www/data/register_log', 'a')
f.write('{0}, {1}\n'.format(name, email))
f.close()

print json.dumps({ 'status' : True, 'msg' : 'Entry {0}, {1}'.format(name, email) })
