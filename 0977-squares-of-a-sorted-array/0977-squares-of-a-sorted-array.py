class Solution(object):
    def sortedSquares(self, nums):
        
        neg = []
        pos = []
        res = []
        # Separating negative and positive
        for num in nums:
            if num < 0:
                neg.append(num * num)
            else:
                pos.append(num * num)
        # Negative squares are currently in decreasing order
        neg.reverse()
        i = 0
        j = 0
        # Merge two sorted arrays
        while i < len(neg) and j < len(pos):

            if neg[i] < pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1
        # Remaining positive squares
        while j < len(pos):
            res.append(pos[j])
            j += 1
        # Remaining negative squares
        while i < len(neg):
            res.append(neg[i])
            i += 1
        return res
            
        