 #coding=GB18030
import  urllib.request
from bs4 import BeautifulSoup
import re

url="http://www.duanwenxue.com/article/673911.html"
a=urllib.request.urlopen(url)

htmlstr=a.read().decode('GB18030')

soup=BeautifulSoup(htmlstr,'html.parser')

y=re.compile(r'<p>([\s\S]*?)</p>')
text=y.findall(str(soup))      #��һ��������ʽɸѡ����<p></p>�е�����

x=''

for i in range(0,len(text)):
     x=x+text[i]

text1=re.sub("</?\w+[^>]*>",'',x)  #ȥ��html��ǩ

text2=text1.replace("��",'��\n\n\0\0')  #���ı����ÿ�
print(text2)