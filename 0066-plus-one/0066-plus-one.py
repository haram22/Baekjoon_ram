class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strNum = ''
        ans = []
        for i in range(len(digits)) :
            strNum += str(digits[i])
        added = str(int(strNum)+1)
        for i in range(len(added)) :
            ans.append(int(added[i]))
        print(ans)
        return ans