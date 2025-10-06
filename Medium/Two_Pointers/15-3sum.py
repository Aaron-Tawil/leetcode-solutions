from collections import defaultdict
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []
        for i in range(n - 2):
            # If current number > 0, no triple can sum to 0 - since we use only greater indices and the array is sorted
            if nums[i] > 0:
                break
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates for second and third elements
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res


        #second way
        n = len(nums)
        if n < 3:
            return []

        # Map sum -> set of index pairs (i, j) with i < j
        two_sum = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                two_sum[nums[i] + nums[j]].add((i, j))

        res = set()
        for k in range(n):
            target = -nums[k]
            if target not in two_sum:
                continue
            for (i, j) in two_sum[target]:
                # must use three distinct indices
                if k == i or k == j:
                    continue
                # Deduplicate by values (sorted tuple)
                trip = tuple(sorted((nums[k], nums[i], nums[j])))
                res.add(trip)

        return [list(t) for t in res]

        