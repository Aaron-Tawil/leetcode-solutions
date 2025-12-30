class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        st = []
        for num in nums2:
            while st and st[-1]<num:
                dic[st.pop()]=num
            st.append(num)
        return [dic.get(num,-1) for num in nums1 ]