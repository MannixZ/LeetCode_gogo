'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 递归法
# 解题思路：
# 这道题需要用抽象一点的思路思考
# 1.递归需要一个结束条件：
#   - 当 list1.next() 为 null,证明list1已经遍历完，返回list2
#   - 当 list2.next() 为 null,证明list1已经遍历完，返回list1
# 2.当list.val() 意思是 list的头节点的值，所以：
#   - 当 list1.val() < list2.val() ,那么 list1 = list[1](这里是用列表的方法来做解释表示链表的第一个，实际上链表不能用下标的方式标识) + list.next() + list2;所以 list1.next = self.mergeTwoLists(list1.next, list2) 拆解的意思是，list1.next（list1剔除第一个数后剩下的数） 和 list2 抽象成一大块包裹， 将这块大的包裹丢给 list1.next，因为已经将 list2也拼接上去了，所以最终还要 return list1 ，返回一个排序后的结果。
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:return list2
        if not list2:return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2