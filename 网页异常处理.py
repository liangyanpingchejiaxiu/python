Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.error
>>> req = urllib.request.Request('http://www.gggggggggdgdgd.com')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    req = urllib.request.Request('http://www.gggggggggdgdgd.com')
AttributeError: module 'urllib' has no attribute 'request'
>>> import urllib.request
>>> req = urllib.request.Request('http://www.gggggggggdgdgd.com')
>>> try:
	urllib.request.urlopen(req)

except  urllib.error.URLError as e:
	print(e.reason)

	
[Errno 11001] getaddrinfo failed
>>> 
>>> req = urllib.request.Request('http://www.gggggggggdgdgd.com')
>>> try:
	urllib.request.urlopen(req)

except urllib.error.URLError as e:
	if hasattr(e,'reason')"
	
SyntaxError: EOL while scanning string literal
>>> try:
	urllib.request.Request(req)

except urllib.error.URLError as e:
	if hasattr(e,'reason'):
		print('reason:',e.reason)

		
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    urllib.request.Request(req)
  File "F:\桌面文件\lib\urllib\request.py", line 328, in __init__
    self.full_url = url
  File "F:\桌面文件\lib\urllib\request.py", line 354, in full_url
    self._parse()
  File "F:\桌面文件\lib\urllib\request.py", line 383, in _parse
    raise ValueError("unknown url type: %r" % self.full_url)
ValueError: unknown url type: 'urllib.request.Request object at 0x03E37FF0'
>>> import urllib.request
>>> try:
	urllib.request.Request(req)

except urllib.error.URLError as e:
	if hasattr(e,'reason'):
		print('reason:',e.reason)#reason是url错误 code是http错误
	elif hasattr(e,'code'):
		print('code',e.code)
else:
	everything is fine

	
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    urllib.request.Request(req)
  File "F:\桌面文件\lib\urllib\request.py", line 328, in __init__
    self.full_url = url
  File "F:\桌面文件\lib\urllib\request.py", line 354, in full_url
    self._parse()
  File "F:\桌面文件\lib\urllib\request.py", line 383, in _parse
    raise ValueError("unknown url type: %r" % self.full_url)
ValueError: unknown url type: 'urllib.request.Request object at 0x03E37FF0'
>>> 
