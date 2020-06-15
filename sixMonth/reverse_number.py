class Solution:
    def reverse(self, x: int) -> int:
        # neg or pos
        if x < 0 :
            flag = -1
        else:
            flag = 1
        #
        res = 0
        x = abs(x)
        while(x != 0):
            a = x % 10
            res = res * 10 + a
            x = int(x / 10)
        if -2147483648 < res * flag < 2147483647:
            return res * flag
        else:
            return 0


a = Solution()
result = a.reverse(-123)
print(result)