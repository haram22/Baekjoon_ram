class Solution:
    def addBinary(self, a: str, b: str) -> str:
        front = '0b'
        finA = int(front + a, 2)
        finB = int(front + b, 2)
        numA = finA + finB
        fin = bin(numA)
        ans = fin[2:]
        return ans
        
        