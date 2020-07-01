""" Problem Description """
"""We have given a 'n' coins. We need to arrange them like a down stairs. 
   Return the number of complete stairs formed using those n coins."""

"""Sample input and output

Example 1 -

n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

Example 2 -

n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        z = n
        if n == 1 or n == 0:
            return n
        for i in range(1,n):
            z = z - i
            if z <= i:
                return i
                