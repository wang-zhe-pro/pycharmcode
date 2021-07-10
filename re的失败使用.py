import re
import  requests

url="https://www.guet.edu.cn/info/1151/56384.htm"
headers={
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
}
r=requests.get(url,headers)
r.encoding = "utf8"
wen=re.sub('<strong>|</strong>',"",r.text)

lists=re.findall(r'<p.*?>([^<>©]*?)</p>',wen,re.S)
for list in lists:
    print(list)



