'''
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 解题思路
# 字符串s=foo, t=bar, 遍历字符串s, for i in range(len(str))
# s.index(s[i]) t.index(t[i])
# 得出的结果
# 0 0 true
# 1 1 true
# 1 2 false
# 将用 all() 将以上三个结果封装为一个列表，[true, true, false] ,all 的功能是如果列表内有 0、空、None、False ，all都返回False
# 总结：主要处理字符串重复的情况，比如上面的o，当遍历到最后一个o的时候，s.index()发现之前已经有o了，但是t.index()对应映射关系错误，因为一个o只能对应一个t.index()的位置，如果对应不上则为false


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(str)))
            
    
so = Solution()
so.isIsomorphic("foo", "bar")