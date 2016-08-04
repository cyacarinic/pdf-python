# -*- coding: utf-8 -*-

import pdfkit

try:
    pdfkit.from_url("http://google.com","url.pdf")
except Exception, e:
    print "Error al crear -- URL>"
    print str(e)

try:
    pdfkit.from_file('test.html', 'html.pdf')
except Exception, e:
    print "Error al crear --> FILE"
    print str(e)

try:
    pdfkit.from_string('Hello!', 'string.pdf')
except Exception, e:
    print "Error al crear --> STRING"
    print str(e)
