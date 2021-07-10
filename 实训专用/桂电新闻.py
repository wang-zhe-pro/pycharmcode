import  re
con='共1366条  136/137 '
res=re.findall('共1366条  (.*?)/137',con)
print(res)