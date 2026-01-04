class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        pn0 = 0
        pn2 = n-1
        while pn0<n and nums[pn0]==0:
            pn0+=1
        while pn2>=0 and nums[pn2]==2:
            pn2-=1
        curr = pn0
        while curr<=pn2:
            if nums[curr]==0:
                nums[pn0],nums[curr] = nums[curr],nums[pn0]
                pn0+=1
                curr+=1
            elif nums[curr]==2:
                nums[pn2],nums[curr] = nums[curr],nums[pn2]
                pn2-=1
            elif nums[curr]==1:
                curr+=1