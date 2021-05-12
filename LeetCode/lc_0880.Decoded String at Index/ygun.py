#!/usr/local/bin/python3
#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        q = []
        acc = [0]
        answerIdx = -1
        
        for c in s:
            if c.isdigit():
                acc.append(acc[-1] * int(c))
            else:
                acc.append(acc[-1] + 1)

        for i in reversed(range(len(s))):
            # print(acc[-1],k,i, s[i])
            if (k==0 and not s[i].isdigit()) or (acc[-1] == k and not s[i].isdigit()):
                answerIdx = i
                break

            cur = s[i]
            if cur.isdigit():
                acc.pop()
                k = k % acc[-1]
            else:
                acc.pop()
        if answerIdx == -1:
            answerIdx = 0


        return s[answerIdx]


# @lc code=end
