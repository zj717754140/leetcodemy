
class Solution:
    def maxScoreSightseeingPair(self, A):
        max_res = 0
        A_add_i = A[0] + 0
        for j in range(1, len(A)):
            max_res = max(max_res, A_add_i+A[j] - j)
            A_add_i = max(A_add_i, A[j]+j)
        return max_res

if __name__=="__main__":
    A = [8, 1, 5, 2, 6]
    S = Solution()
    print(S.maxScoreSightseeingPair(A))