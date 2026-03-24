from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        for ch in s2[:n]:
            window[ord(ch) - ord('a')] += 1

        if window == need:
            return True

        for i in range(n, m):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - n]) - ord('a')] -= 1

            if window == need:
                return True

        return False


        