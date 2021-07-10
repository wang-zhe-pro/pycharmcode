import requests
html=requests.get("https://v.guet.edu.cn/http/77726476706e69737468656265737421f9e00f9b32357c1e7b0c9ce29b5b/info/1033/66506.htm")
print(html.content)