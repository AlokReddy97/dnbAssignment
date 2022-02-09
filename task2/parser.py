"""
from urllib.parse import unquote

o = unquote('https://www.certipedia.com/quality_marks/0091005568?locale=en&certificate_number=01+104+110402%2F01')

p = unquote(unquote("https://www.certipedia.com/certificates/01+104+110402%252F01?locale=en"))
print(o)
print(p)

url = "https://www.certipedia.com/quality_marks/0091005568?locale=en&certificate_number=01+104+110402%2F01"


print(parse.parse_qs(parse.urlsplit(url).query)["certificate_number"][0])

certi = dict(parse.parse_qs(parse.urlsplit(url).query))

/quality_marks/9000011537?locale=en&certificate_number=PSO+2315011

from urllib import parse

print("https://www.certipedia.com/certificates/")

certi_no = 'https://www.certipedia.com/certificates/01 400 1610377'

print(parse.urlencode(certi_no))

"""

my_string="/quality_marks/9108641140?locale=en&amp;certificate_number=01+202+IND%2FQ-17+0028"
print(url.split("certificate_number=",1)[1])

from urllib.parse import urlparse

o = urlparse("/quality_marks/9108641140?locale=en&amp;certificate_number=01+202+IND%2FQ-17+0028")

p = urlparse(("/quality_marks/9108641140?locale=en&amp;certificate_number=01+202+IND%2FQ-17+0028"))
print(o)

print(p)