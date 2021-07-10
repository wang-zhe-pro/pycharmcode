class solution:
    def visited(self,nums: list[int])->list[list[int]]:
        res=[]
        flag={}
        for num in nums:
            flag[num]=False
        self.back(nums,res,flag,[])
        return res
    def back(self,nums,res,flag,lis):
        if len(lis)==3:
            res.append(lis[:])
        for num in nums:
            if not flag[num]:
                lis.append(num)
                flag[num]=True
                self.back(nums,res,flag,lis)
                lis.pop()
                flag[num]=False
if __name__ == '__main__':
    a=solution()
    nums=['莫','小','陈']
    res=a.visited(nums)
    print(res)