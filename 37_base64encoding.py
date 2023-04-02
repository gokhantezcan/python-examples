# -*- coding: utf-8 -*-

import base64

string = "Python is awesome"
stringAsBytes = string.encode("utf-8")

stringAsBase64 = base64.b64encode(stringAsBytes)

print(stringAsBase64)

string = stringAsBase64.decode("utf-8")
result = base64.b64decode(string)
print(result)