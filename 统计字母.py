import  string
#统计大写字母出现的次数，并按照字母出现次数降序排序输出
def countchar(file):
# *************begin************#
    file1=open(file,"r")
    a=file1.read().replace('\t','').replace('\n','').replace(' ','').replace('space','');
    list=list(string.ascii_uppercase)

    dict={}
    for x in a:
        dict[x]=0
    for x in a:
        if(x in list):
            dict[x]+=1
    lice=[(key,val) for key,val in dict.items() if(dict[key]!=0)]
    h=sorted(lice,key=lice[1],reverse=True)
    for a in h:
        print(a)

# **************end*************#


file = input();
countchar(file)
# Apple Apple APPLE apple Apple Apple
# Abc
# Admin
# A
# Big Big
# Blue Blue Blue
# Bed
# Cc ddd