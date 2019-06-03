Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.search(r'a{3}bc','aaaaabbbc')
>>> re.search(r'^bc','abc')
>>> re.search
<function search at 0x039FB930>
>>> p='[^bc]'
>>> s='aabbcc'
>>> re.search(r'p','s')
>>> re.match(p,s)
<re.Match object; span=(0, 1), match='a'>
>>> g='[abc$]
SyntaxError: EOL while scanning string literal
>>> g='[abc$]'
>>> re.match(g,s)
<re.Match object; span=(0, 1), match='a'>
>>> re.search(r'fish(c|d)','fishcd')
<re.Match object; span=(0, 5), match='fishc'>
>>> p='[a-z]'
>>> re.findall(p,fisnshf.com)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    re.findall(p,fisnshf.com)
NameError: name 'fisnshf' is not defined
>>> re.findall(p,'string')
['s', 't', 'r', 'i', 'n', 'g']
>>> #^是取反 $取末尾
>>> re.search(r'^abc','abcfe')
<re.Match object; span=(0, 3), match='abc'>
>>> re.search(r'^[abcfe]','abcfegdg')
<re.Match object; span=(0, 1), match='a'>
>>> # search里面‘【】’原样输出
>>> re.search(r^'abc','abcfd')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    re.search(r^'abc','abcfd')
NameError: name 'r' is not defined
>>> re.search(r'^bc','abc')
>>> re.findall(r'^bc','abc')
[]
>>> re.findall(r'\bfish\b','fishisfish.isfish__fishc.com')
[]
>>> re.findall(r"\bfish\b","fishc.com.fish.fishcom1__fish")
['fish']
>>> re.search(r"^bc","abc")
>>> re.findall(r"[^bc]",'"abc")
	       
SyntaxError: EOL while scanning string literal
>>> re.findall(r"[^bc]","abc")
	       
['a']
>>> p=re.compile(r'[A-Z]')
	       
>>> p.search('i love you')
	       
>>> p.search('I LOVE YOU')
	       
<re.Match object; span=(0, 1), match='I'>
>>> 
