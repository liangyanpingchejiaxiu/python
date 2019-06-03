import urllib.request
import re


def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
    response = urllib.request.urlopen(req)
    html = response.read().decode('GBK')

    return html


    

def get_imgs(html):
    p=r'<img src="([^"]+\.jpg)" '#加小括号直接获得地址
    imaglist = re.findall(p,html)
    
  
    for each in imaglist:
        filename= each.split('/')[-1]
        urllib.request.urlretrieve(each,filename,None)#第一个为网站 保存地址：f:/ 第三个选填







if __name__=='__main__':
    url = "https://lol.qq.com/data/info-defail.shtml?id=Annie"
    get_imgs(open_url(url))
