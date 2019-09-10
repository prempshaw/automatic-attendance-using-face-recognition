
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
#print  response_body
b=()
b=response_body.split(":")
c=b[3]
d=c.split(",")
a="Ankit_Sinha"
b="Anurag_Kumar"
if a in response_body :
    print ("Attendance Updated.")
    print ("Ankit Sinha Found.")
    print ("Confidence: "+d[0])
elif b in response_body :
    print ("Attendance Updated.")
    print ("Anurag Kumar Found.")
    print ("Confidence: "+d[0])
else :
    print ("Not Found.")
    print ("Authentication Failure.")
