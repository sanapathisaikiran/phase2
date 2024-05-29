def performbubblesort(nums):
    n=len(nums)
    fixindex=n-1

    while fixindex>0:
        for index in range(fixindex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
        fixindex=fixindex-1
nums=[10,8,2,14,12,7]
print("before sorting",nums)
performbubblesort(nums)
print("aftersorting",nums)
