def sort(nums,target):
    if nums==None or len(nums)==0:
        return 0
    left=0
    right=len(nums)
    while(left<right):
        mid=left+(right-left)//2
        if(nums[mid]==target):
            right=mid
        elif(nums[mid]<target):
            left=mid+1
        else:
            right=mid
    return left

if __name__ == '__main__':
    list=[1,2,2,2,2,3,3,3,3,26]
    res=sort(list,3)
    print(res)
