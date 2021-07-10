class solution:
    def visited(self,nums:list[int])->list[list[int]]:
        res=[]
        flag={}
        for num in nums:
            flag[num]=False
        self.back(nums,res,flag,[])
        return res
    def back(self,nums,result,flag,ls):
        if len(ls)==3:
            result.append(ls[:])
            return
        for num in nums:
            if not flag[num]:
                ls.append(num)
                flag[num]=True
                self.back(nums,result,flag,ls)
                ls.pop()
                flag[num]=False
if __name__ == '__main__':
    useage=solution()
    nums=[1,2,3]
    lise=useage.visited(nums)
    print(lise)
