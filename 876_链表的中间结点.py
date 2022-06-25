'''
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

 

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 解题思路1
# 遍历链表转化为数组，用数组 // 2 得出结果，从而返回序列
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a = [head]
        while a[-1].next:
            a.append(a[-1].next)
        return a[ len(a)//2 ]
# 疑惑点1，链表是怎么生成的? 疑惑点2，链表不能直接计算长度？ 疑惑点3，return一个节点值就能返回剩下的序列，而不需要切片

# 解题思路2
# 快慢指针，创建头节点相同的两个指针，slow一次走一步，fast一次走两步，fast走到链表末尾，那slow必然在中间
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# 后话：对链表属性完全不熟悉，目前能知道的是链表不能用下标获取属性，要获取下一个属性只能用 x.next的方法，类似于生成器