class Solution:
    def sortArray(self, nums):
        max_num = min_num = 0
        for num in nums:
            max_num = max(max_num,num)
            min_num = min(min_num,num)
        counter = [0] * (max_num-min_num+1)
        for num in nums:
            counter[num-min_num] +=1 
        i = 0
        for num in range(len(counter)):
            while counter[num] >0:
                nums[i] = num + min_num
                i += 1
                counter[num] -=1
        return nums
            