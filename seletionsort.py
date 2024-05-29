def selectionsort(nums):
    n=len(nums)
    fixindex=n-1
    while fixindex>0:
        maxeleindex=fixindex
        for index in range(fixindex):
            if nums[index]>nums[maxeleindex]:
                maxeleindex=index
        if maxeleindex!=fixindex:
            temp=nums[maxeleindex]
            nums[maxeleindex]=nums[fixindex]
            nums[fixindex]=temp
        print(nums)
        fixindex=fixindex-1
nums=[18,12,10,5,13]
print("beforesorting",nums)
selectionsort(nums)
print("aftersort",nums)