class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTracking(length, visited, res, ans):
            if length is targetLength:
                ans.append([i for i in res])
                return
            else:
                for i in range(targetLength):
                    if not visited[i]:
                        res.append(nums[i])
                        visited[i] = 1
                        backTracking(length + 1, visited, res, ans)
                        visited[i] = 0
                        res.pop()
        ans = []
        targetLength = len(nums)
        visited = [0 for i in range(targetLength)]
        
        backTracking(0, visited, [], ans)
        
        return ans
        
        