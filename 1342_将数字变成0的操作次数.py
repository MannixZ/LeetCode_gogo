'''
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

 

示例 1：

输入：num = 14
输出：6
解释：
步骤 1) 14 是偶数，除以 2 得到 7 。
步骤 2） 7 是奇数，减 1 得到 6 。
步骤 3） 6 是偶数，除以 2 得到 3 。
步骤 4） 3 是奇数，减 1 得到 2 。
步骤 5） 2 是偶数，除以 2 得到 1 。
步骤 6） 1 是奇数，减 1 得到 0 。
示例 2：

输入：num = 8
输出：4
解释：
步骤 1） 8 是偶数，除以 2 得到 4 。
步骤 2） 4 是偶数，除以 2 得到 2 。
步骤 3） 2 是偶数，除以 2 得到 1 。
步骤 4） 1 是奇数，减 1 得到 0 。
示例 3：

输入：num = 123
输出：12

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-steps-to-reduce-a-number-to-zero
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 解题思路1
# 创建一个新的变量保存操作次数，如果num为0结束循环，否则，当num 求余为0，num为偶数，需要/2，num求余不为0，num为奇数需要-1
class Solution1:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while True:
            if not num:
                return i
            elif num%2 == 0:
                num //= 2
                i += 1
            elif num%2 == 1:
                num -= 1
                i += 1

# 解题思路2
# 先判断 num 是否为奇数，是奇数的情况下+1，否则则对 num/2 绝对值，并操作数 ans += 1加一
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            print(ans, num)
            ans += num & 1  # 判断num是否为奇数或偶数，如果num为奇数则操作数ans + 1
            print(f"ans : {ans}")
            if num > 1:
                ans += 1
            num >>= 1  # 对 num进行 [num/2]
            print(f"num >>= 1: {num}")
        return ans

so = Solution()
so.numberOfSteps(num=14)