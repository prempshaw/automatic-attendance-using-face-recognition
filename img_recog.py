#!/usr/bin/python2

from urllib2 import Request, urlopen

values = """
  {
    "image": "http://35.154.49.223/image/ankit/ankit_enroll2.jpg",
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': 'fe2b1d88',
  'app_key': '622354d3f6cbcfde77192f290ef6e293'
}
request = Request('https://api.kairos.com/recognize', data=values, headers=headers)

response_body = urlopen(request).read()
print (response_body)
