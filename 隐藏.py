
import urllib.request
import urllib.parse
import json
content = input('请输入要翻译的内容：')
url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
head = { } #这是第一种 
head['User - Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
from_data = {'i':content,'doctype':'json','keyfrom':'fanyi.web'}
data=urllib.parse.urlencode(from_data).encode('utf-8')
req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
result=json.loads(html)
result= result['translateResult'][0][0]['tgt']
print('翻译结果为：%s' %result)
#第二种 req = urllib.request.Request(url,data,head) req.add_header('User - Agent',' ')
# 让爬虫像人一样访问  有两种方法 第一种
# while(True): content = input('请输入要翻译的内容（按q推出：')  if content == q  : break导入time模块 最后 time.sleep(秒)
#第二种代理

