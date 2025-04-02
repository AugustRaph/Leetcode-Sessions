class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans=0
        maxDiff=0 #max(nums[i]-nums[j])
        maxNum=0 #max(nums[i])

        for num in nums:
            ans=max(ans,maxDiff*num)
            maxDiff=max(maxDiff,maxNum-num)
            maxNum=max(maxNum,num)
        return ans