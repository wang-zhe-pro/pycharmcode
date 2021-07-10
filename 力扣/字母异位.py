class solution:
    def count_1(self,strs:list[str])->list[list[str]]:
        list=[]
        dict={}
        for str in strs:
            a=''.join(sorted(str))
            dict[a]=dict.get(a,[])+[str]
        return dict.values()
    def  count_2(self,strs:list[str])->list[list[str]]:#用数组计算，性质差不多
        dict={}
        for str in strs:
            list = [0] * 26
            for s in str:
                list[ord(s)-ord('a')]+=1
            dict[tuple(list)]=dict.get(tuple(list),[])+[str]
        return dict.values()
if __name__ == '__main__':
    plan=solution()
    list_start=["eat", "tea", "tan", "ate", "nat", "bat"]
    list_after=plan.count_2(list_start)
    print(list_after)

