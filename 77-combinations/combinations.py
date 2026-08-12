class Solution:
    def combine(self, n: int, k: int):
        res= []
        sol=[]
        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return
            left=x
            need=k-len(sol)
            if left>need:
                backtrack(x-1)
            sol.append(x)
            backtrack(x-1)
            sol.pop()
        backtrack(n)
        return res
        
        