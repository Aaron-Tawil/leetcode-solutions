# Problem: 423 – reconstruct original digits from english
# Difficulty: Medium
# Link: https://leetcode.com/problems/reconstruct-original-digits-from-english/


from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        # strnum = ['zero','one','two','three','four','five','six','seven','eight','nine']
        # uniq = ['z','_','w','_','u','_','x','_','g','_']
        # strnum2 = ['_','one','_','three','_','five','_','seven','_','nine']
        # uniq2 = ['_','o','_','t','_','f','_','s','_','_']
        # strnum3 = ['_','_','_','_','_','_','_','_','_','nine']
        # uniq3 = ['_','_','_','_','_','_','_','_','_','n']
        cnt = Counter(s)
        out = [0]*10

        # 1) unique letters
        out[0] = cnt['z']
        out[2] = cnt['w']
        out[4] = cnt['u']
        out[6] = cnt['x']
        out[8] = cnt['g']

        # 2) letters now unique after subtracting above
        out[3] = cnt['h'] - out[8]          # three
        out[5] = cnt['f'] - out[4]          # five
        out[7] = cnt['s'] - out[6]          # seven

        # 3) 'o' only in one now
        out[1] = cnt['o'] - out[0] - out[2] - out[4]

        # 4) everything else is nine
        # method A: use leftover 'i'
        out[9] = cnt['i'] - out[5] - out[6] - out[8]
        # (alternatively, out[9] = (cnt['n'] - out[1] - out[7]) // 2)

        # build result string
        return ''.join(str(i)*out[i] for i in range(10))

            