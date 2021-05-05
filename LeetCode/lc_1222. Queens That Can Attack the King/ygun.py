#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# @lc app=leetcode id=1222 lang=python3
#
# [1222] Queens That Can Attack the King
#

# @lc code=start
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dr = [-1, 1, 0, 0, -1, -1, 1, 1]
        dc = [0, 0, -1, 1, -1, 1, -1, 1]
        ans = []

        for i in range(8):
            newR = king[0] + dr[i]
            newC = king[1] + dc[i]
            while (newR >= 0 and newC >= 0 and newR < 8 and newC < 8):
                if [newR, newC] in queens:
                    ans.append([newR, newC])
                    break
                newR += dr[i]
                newC += dc[i]
        
        return ans


# @lc code=end
