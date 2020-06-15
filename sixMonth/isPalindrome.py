


class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = []
        if x < 0:
            return False
        while(x != 0):
            mod = int(x % 10)
            a.append(mod)
            x = int(x / 10)
        l = len(a)
        if l == 0 or l==1:
            return True
        for i in range(int(l/2)):
            if a[i] != a[l-i-1]:
                return False
            if i == int(l/2-1):
                return True


S = Solution()
temp = S.isPalindrome(10)
print(temp)