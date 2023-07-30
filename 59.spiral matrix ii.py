class Solution:
    def helper(self,res, i_1, j_1, i_2, j_2, num):
        # return res with outbox filled with num
        # top
        for j in range (j_1, j_2+1):
            res[i_1][j] = num
            num +=1
        # right
        for i in range(i_1+1, i_2+1):
            res[i][j_2] = num
            num += 1
        # bottom
        for j in range(j_2-1, j_1-1, -1):
            res[i_2][j] = num
            num += 1
        # left
        for i in range(i_2-1, i_1, -1):
            res[i][j_1] = num
            num += 1
        return num, res

    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(n)]
        i_1, j_1 = 0, 0
        i_2, j_2 = n-1, n-1
        num = 1

        total_iters = int(n/2)
        for i in range(total_iters):
            num, res = self.helper(res, i_1, j_1, i_2, j_2, num)
            i_1 += 1
            j_1 += 1
            i_2 -= 1
            j_2 -= 1
        if n%2 != 0: 
            res[total_iters][total_iters]=num
        
        return res
        
    

