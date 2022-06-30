'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 解题思路
# 双指针
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None # pre 节点指向null
        cur = head # cur 节点指向head

        while cur: # 遍历 cur ，直到 cur 为null 结束循环
            tmp = cur.next  # tmp 指向 cur 的下一个节点 cur.next
            cur.next = pre  # 用pre 赋值到 cur.next，完成指针反转
            # 推进 cur 和 pre 向前一位
            pre = cur 
            cur = tmp
        return pre

# 解题思路2
# 迭代法
