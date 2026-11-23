class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        #1. Create two empty list.
        neg = []
        pos = []

        #2. Separate the neg and pos while doing square.
        for i in nums:
            if i < 0:
                neg.append(i * i)
            else:
                pos.append(i * i)

        #3. Reverse the negative sqaure list
        neg.reverse()

        #4. Merge two sorted list
        res = []
        i,j = 0,0
        while i<len(neg) and j<len(pos):
            if neg[i]<pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1

        while i<len(neg):
            res.append(neg[i])
            i += 1

        while j<len(pos):
            res.append(pos[j])
            j += 1
         
        return res