class Solution:
    def numJewelInStones(self, j, s):
        """
        j:string
        s:string
        return:integer
        """
        return(sum(map(s.count, j)))
