class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        st = []

        for i,curr_t in enumerate(temperatures):

            while st and curr_t>temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)
    
        return res
        