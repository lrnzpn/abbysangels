from .models import *
import base64
import mimetypes
import os
import sys

def img_to_data(path):
    """Convert a file (specified by a path) into a data URI."""
    if not os.path.exists(path):
        raise FileNotFoundError
    mime, _ = mimetypes.guess_type(path)
    with open(path, 'rb') as fp:
        data = fp.read()
        data64 = u''.join(base64.encodestring(data).splitlines())
        return u'data:%s;base64,%s' % (mime, data64)