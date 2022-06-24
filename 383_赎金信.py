'''
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ransom-note
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 解题思路1，遍历需要对照的字符串，如果在被遍历的字符串上存在字符，则删除被遍历的字符串中的字符，直到需要遍历的字符串被遍历完才算成功
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            elif ransomNote[i] in magazine and i == len(ransomNote) - 1:
                return True
            elif ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i], "", 1)

# 解题思路2，将 ransomNote 和 magazine 的字符串用collections.Counter()计算出每个字符出现次数，然后两个字符串相减，当是负数的时候证明ransomeNote的字符全部
# 此处利用了python一个特性，return 或 if 后面接一个 空的字符串，我们可以用于判断 bool值，比如这里collections.Counter()返回的是一个空的Counter()对象，return Counter()我们可以用于拿来判断bool()值
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
