Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request
>>> response= urllib.request.urlopen('http://placekitten.com/g/500/600')
>>> cat_img=response.read()
>>> with open('cat_500_600.jpg','wb') as f:
	f.write(cat_img)

	
36416
>>> response.geturl
<bound method HTTPResponse.geturl of <http.client.HTTPResponse object at 0x03337C30>>
>>> response.geturl()
'http://placekitten.com/g/500/600'
>>> response.info()
<http.client.HTTPMessage object at 0x03423130>
>>> print(response.info())
Date: Tue, 04 Dec 2018 01:15:21 GMT
Content-Type: image/jpeg
Transfer-Encoding: chunked
Connection: close
Set-Cookie: __cfduid=dcd75a9c48398ddd519cd9d00c00115471543886121; expires=Wed, 04-Dec-19 01:15:21 GMT; path=/; domain=.placekitten.com; HttpOnly
Access-Control-Allow-Origin: *
Cache-Control: public, max-age=86400
Expires: Wed, 05 Dec 2018 01:15:21 GMT
CF-Cache-Status: HIT
Vary: Accept-Encoding
Server: cloudflare
CF-RAY: 483a6be4e33353f6-LAX


>>> response.getcode()
200
>>> #200表示正常响应
>>> #cat_500_600随便取 图片不用解码 网页要解码
>>> import urllib.request
>>> import urllib.parse
>>> import json
>>> content = input('请输入要翻译的内容：')
请输入要翻译的内容：i love you
>>> url =ttp://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule#ttp://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule _o 要去掉
SyntaxError: invalid syntax
>>> url =http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
SyntaxError: invalid syntax
>>> url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
>>> from_data = {'i':content,'doctype':'json','keyfrom':'fanyi.web'}
>>> data=urllib.parse.urlencode(from_code).encode('utf-8')#发送的包要转码 等下返回的包也要转码
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data=urllib.parse.urlencode(from_code).encode('utf-8')#发送的包要转码 等下返回的包也要转码
NameError: name 'from_code' is not defined
>>> data=urllib.parse.urlencode(from_data).encode('utf-8')
>>> response = urllib.request.urlopen(url,data)
>>> html = response.read().decode('utf-8')#返回的包转码
>>> result=json.loads(html)
>>> type('result')
<class 'str'>
>>> json.loads(html)
{'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 1, 'translateResult': [[{'src': 'i love you', 'tgt': '我爱你'}]]}
>>> type(result)
<class 'dict'>
>>> result= result['translateResult'][0][0]['tgt']
>>> print('翻译结果为：%s' %result)
翻译结果为：我爱你
>>> 
