

# 解题思路1
# 先遍历列表每个成员的财富，计算total，将total添加到列表中，在遍历列表，将最大值赋给max_total
class Solution:
    def maximumWealth(self, accounts) -> int:
        total_list = []
        for i in accounts:
            total = 0
            for j in i:
                total += j
            total_list.append(total)
        max_total = 0
        for i in range(len(total_list)):
            if total_list[i] > max_total:
                max_total = total_list[i]
            print(max_total)
        return max_total
            
# 解题思路2
class Solution:
    def maximumWealth(self, accounts) -> int:
        return max(map(sum, accounts))      # map()，获得一个二维整数列表内的总和；max,获得一个整数列表内的最大值

so = Solution()
so.maximumWealth(accounts=[[2,8,7],[7,1,3],[1,9,5]])