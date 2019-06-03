Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request
>>> response = urllib.request.urlopen('http://www.fishc.com')
>>> html = response.read()
>>> print(html)
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="keywords" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4|\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Python\xe6\x95\x99\xe5\xad\xa6|Web\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|\xe5\x85\xa8\xe6\xa0\x88\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|C\xe8\xaf\xad\xe8\xa8\x80\xe6\x95\x99\xe5\xad\xa6|\xe6\xb1\x87\xe7\xbc\x96\xe6\x95\x99\xe5\xad\xa6|Win32\xe5\xbc\x80\xe5\x8f\x91|\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86|Linux\xe6\x95\x99\xe5\xad\xa6">\n    <meta name="description" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4\xe4\xb8\xba\xe5\xa4\xa7\xe5\xae\xb6\xe6\x8f\x90\xe4\xbe\x9b\xe6\x9c\x80\xe6\x9c\x89\xe8\xb6\xa3\xe7\x9a\x84\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6\xe3\x80\x82">\n    <meta name="author" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4">\n    <title>\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4-\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Python\xe6\x95\x99\xe5\xad\xa6|Web\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|\xe5\x85\xa8\xe6\xa0\x88\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|C\xe8\xaf\xad\xe8\xa8\x80\xe6\x95\x99\xe5\xad\xa6|\xe6\xb1\x87\xe7\xbc\x96\xe6\x95\x99\xe5\xad\xa6|Win32\xe5\xbc\x80\xe5\x8f\x91|\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86|Linux\xe6\x95\x99\xe5\xad\xa6</title>\n    <link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico">\n    <link rel="stylesheet" href="css/styles.css">\n    <script src="js/jq.js"></script>\n    <script src="https://cdn.bootcss.com/timelinejs/2.36.0/js/storyjs-embed.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/timelinejs/2.36.0/js/storyjs-embed.js" defer></script>\n    <!-- <script src="https://fishc.oss-cn-hangzhou.aliyuncs.com/Web/js/embed.js"></script> -->\n    <script>\n        $(document).ready(function() {\n            var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;\n\n            createStoryJS({\n                type:       \'timeline\',\n                width:      \'auto\',\n                height:     windowHeight,\n                source:     \'data.json\',\n                start_at_end:true,                          //OPTIONAL START AT LATEST DATE\n                embed_id:   \'my-timeline\'\n            });\n\n        });\n    </script>\n    <!-- END TimelineJS -->\n</head>\n<body>\n<div id="my-timeline"></div>\n</body>\n</html>\n'
>>> html = html.decode('utf-8')
>>> print(html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="鱼C工作室|免费编程视频教学|Python教学|Web开发教学|全栈开发教学|C语言教学|汇编教学|Win32开发|加密与解密|Linux教学">
    <meta name="description" content="鱼C工作室为大家提供最有趣的编程视频教学。">
    <meta name="author" content="鱼C工作室">
    <title>鱼C工作室-免费编程视频教学|Python教学|Web开发教学|全栈开发教学|C语言教学|汇编教学|Win32开发|加密与解密|Linux教学</title>
    <link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="stylesheet" href="css/styles.css">
    <script src="js/jq.js"></script>
    <script src="https://cdn.bootcss.com/timelinejs/2.36.0/js/storyjs-embed.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/timelinejs/2.36.0/js/storyjs-embed.js" defer></script>
    <!-- <script src="https://fishc.oss-cn-hangzhou.aliyuncs.com/Web/js/embed.js"></script> -->
    <script>
        $(document).ready(function() {
            var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;

            createStoryJS({
                type:       'timeline',
                width:      'auto',
                height:     windowHeight,
                source:     'data.json',
                start_at_end:true,                          //OPTIONAL START AT LATEST DATE
                embed_id:   'my-timeline'
            });

        });
    </script>
    <!-- END TimelineJS -->
</head>
<body>
<div id="my-timeline"></div>
</body>
</html>

>>> 
