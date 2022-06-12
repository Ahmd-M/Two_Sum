
def twoSum(nums, target):

    n = 0
    answer = [0,0]

    while (answer==[0,0]):
        n+=1
        for i in range(0,len(nums)-n):
            if(nums[i]+nums[i+n]==target):
                answer = [i,i+n]
                break

    return answer

answer = twoSum([1,2,9,6,3,4],5)
print(answer)