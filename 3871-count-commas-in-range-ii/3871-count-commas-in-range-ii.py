class Solution(object):
    def countCommas(self, n):
        res= 0
        i= 1000
        while i <= n:
            res += n-i+1
            i*= 1000
        return res
        
        