import urllib.request
import re


def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
    response = urllib.request.urlopen(req)
    html = response.read().decode('gb2312')

    return html


    

def get_ip(html):
    p=r'(?:(?"[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]) '#加小括号直接获得地址
    iplist = re.findall(p,html)
    
  
    for each in iplist:
        print(each)
        


#只会捕获要的 不需要的不捕获




if __name__=='__main__':
    url = "http://www.66ip.cn"
    get_ip(open_url(url))

# 有可能 00\d 所有 \d 替换2[0-4]\d  25[0-5] 
