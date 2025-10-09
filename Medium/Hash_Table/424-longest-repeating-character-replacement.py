from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ans = k
        # cnt = Counter(s[:k])
        # n = len(s)
        # l,r = 0,k

        # # print(help(Counter))
        # while l<n-k and r<n:
        #     cnt[s[r]]+=1
        #     if (r-l+1)- cnt.most_common(1)[0][1] >k :#we can not replace 
        #         cnt[s[l]]-=1
        #         l+=1
        #     ans = max(ans,r-l+1)
        #     r+=1
        # return ans
        

        cnt = [0] * 26
        l = 0
        max_freq = 0
        ans = k

        for r, ch in enumerate(s):
            idx = ord(ch) - 65  # 'A' -> 0
            cnt[idx] += 1
            max_freq = max(max_freq, cnt[idx])

            # If we need more than k changes to unify this window, shrink
            if (r - l + 1) - max_freq > k:
                cnt[ord(s[l]) - 65] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
        