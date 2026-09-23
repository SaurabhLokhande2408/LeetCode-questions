class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        max_diff = float('inf')
        for i  in range(n-2):
            
            j=i+1
            k=n-1
            while j < k:
                total= nums[i]+nums[j]+ nums[k]
                diff = abs(target - total)
                if max_diff > diff:
                    max_diff = diff
                    sum = total
                if target == total:
                    return sum 
                elif target> total:
                    j+=1
                else:

                    k-=1
                
        return sum


                