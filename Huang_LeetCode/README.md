# LeetCode刷题-----Python3


1. [Two Sum](https://leetcode-cn.com/problems/two-sum)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if n in d: return [d[n], i]
            d[target - n] = i
```
- 用字典记录 { 需要的值:当前索引 } 时间复杂度:O(n)

2. [Add Two Number](https://leetcode-cn.com/problems/add-two-numbers)
```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        if not (l1 or l2):
            return ListNode(1) if carry else None
        l1, l2 = l1 or ListNode(0), l2 or ListNode(0)
        val = l1.val + l2.val + carry
        l1.val, l1.next = val % 10, self.addTwoNumbers(l1.next,l2.next,al > 9)
        return l1
```
- 用carry记录进位

3. [Longest Substring Without Repeating Characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters)


4. [MedianofTwoSortedArrays](https://leetcode-cn.com/problems/median-of-two-sorted-arrays)
```python
class Solution:
    def findKth(self, nums1: List[int], nums2: List[int], k: int):

        # 边界条件
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)
        elif len(nums1) == 0:
            return nums2[k - 1]
        elif k == 1:
            return min(nums1[0], nums2[0])

        first = min(k // 2, len(nums1))
        second = k - first

        if nums1[first - 1] < nums2[second - 1]:
            return self.findKth(nums1[first:], nums2, k - first)
        elif nums1[first - 1] > nums2[second - 1]:
            return self.findKth(nums1, nums2[second:], k - second)
        else:
            return nums1[first - 1]

    def findMedianSortedArrays(self, nums1: List[int],nums2: List[int]) -> float:

        length = len(nums1) + len(nums2)

        if (length & 0x1):
            return self.findKth(nums1, nums2, length // 2 + 1)
        else:
            return ((self.findKth(nums1, nums2, length // 2) +
                     self.findKth(nums1, nums2, length // 2 + 1)) / 2)
```
- 从K入手,利用有序这个条件,每次排除一半的元素。假设A和B的元素个数都大于K/2,因为K的奇偶性不影响结论,假设K为偶数。将A[k/2-1]与B[k/2-1]进行比较：
    * A[k/2-1] == B[k/2-1]  直接返回A[k/2-1]或者B[k/2-1]
    * A[k/2-1]  < B[k/2-1]  删除A中的k/2个元素
    * A[k/2-1]  > B[k/2-1]  删除B中的k/2个元素
- 函数终止条件：
    * 当A或B是空时:直接返回B[k-1]或A[k-1]
    * 当k=1时,返回min(A[0],B[0])
    * 当A[k/2-1] == B[k/2-1]时,返回A[k/2-1]或B[k/2-1]

5. [Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/)
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = ''
        for i, j in [(i, j) for i in range(len(s)) for j in (0, 1)]:
            while i > -1 and i + j < len(s) and s[i] == s[i + j]:
                i, j = i - 1, j + 2
            r = max(r, s[i + 1:i + j], key=len)
        return '' if not s else r
```
- 字符串的中心可能是一个字符也可能是两个字符,例如字符串abcbd,回文子串bcb,中心字符为c。字符串abccbd,回文子串bccb,中心字符为cc。所以j的取值为0或1。
- i 遍历字符串中的每一个字符,通过j的取值判断回文子串的中心字符取值情况。j为0时,子串假设为一个中心字符。j为1时，子串假设为两个中心字符。
- r保存每次确定中心字符情况后的最大子串

8. [String to Integer(atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi)
```python
class Solution:
    def myAtoi(self, str: str) -> int:
        return max(
            min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1),
            -2**31)
```
- 使用正则表达式 ^：匹配字符串开头，[\+\-]：代表一个+字符或-字符，?：前面一个字符可有可无，\d：一个数字，+：前面一个字符的一个或多个，\D：一个非数字字符，*：前面一个字符的0个或多个
- max(min(数字, 2 ** 31 - 1), -2 ** 31) 用来防止结果越界

10. [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/)
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        if len(p) > 1 and p[1] == '*':  # 下一个字符为*
            if s and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
        elif s and p and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        return False
```
- '.' 匹配任意单个字符, '*' 匹配零个或多个前面的那一个元素
- 当模式中第二个字符是'*'时：
    -  如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
        1. 模式后移2位字符,即模式前两位被忽略（*匹配0个字符）
        2. 字符串后移1字符,模式不变,*可以匹配多位
        3. 字符后移1字符,模式后移2字符
    发现情况3可以被情况1和情况2包含,即执行一次情况2,再执行一次情况1。所以情况3不用判断
- 当模式中第二个字符不是'*'时:
    - 如果字符串第一个字符和模式中的第一个字符相匹配,字符串和模式都后移一个字符。
    - 如果字符串第一个字符和模式中的第一个字符不匹配,直接返回False




14. [Longest Common Prefix](https://leetcode-cn.com/problems/longest-common-prefix/)
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][:r.index(0)] if strs else ''
```
- 用set()函数去重判断是否为公共前缀,0作为标志位
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        import os
        return os.path.commonprefix(strs)
```
- os中存在库函数求公共前缀
```python
def commonprefix(m):
    if not m: return ''
    if not isinstance(m[0], (list, tuple)):
        m = tuple(map(os.fspath, m))
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1     
```
- commonprefix()函数通过max(),min()计算出ascii码最大,最小的字符串进行比较。如果s1和s2有共同前缀,其他字符串都有。如果s1和s2没有,其它有也没用

15.  [3Sum](https://leetcode-cn.com/problems/3sum)
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, r = sorted(nums), set()
        # 对前n-2个非重复数的下标进行遍历
        for i in [
                i for i in range(len(nums) - 2)
                if i < 1 or nums[i] > nums[i - 1]
        ]:
            # 字典d保存第三个数大小和索引
            d = {-(nums[i] + n): j for j, n in enumerate(nums[i + 1:])}
            r.update([(nums[i], n, -nums[i] - n) for j, n in enumerate(nums[i + 1:])
                                                            if n in d and d[n] > j])
        return list(map(list, r))
```
- sort避免重复,使得输出结果都是升序,用字典记录{需要的值:当前索引},字典会记录比较大的那个索引,用d[n]>j来避免重复选择一个元素,(nums[i], n, -nums[i] - n)保证列表升序

18. [4Sum](https://leetcode-cn.com/problems/4sum)
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        import collections
        from itertools import combinations as com
        # 将两个索引组合存入l中
        dic, l = collections.defaultdict(list), [*com(range(len(nums)), 2)]
        # 将剩下的两数之和作为索引存入dic
        for a, b in l:
            dic[target - nums[a] - nums[b]].append((a, b))
        # 如果nums[c]+nums[d]存在,从字典中取出对应a,b索引
        r = [(*ab, c, d) for c, d in l for ab in dic[nums[c] + nums[d]]]
        return [
            *set(
                tuple(sorted(nums[i] for i in t))
                for t in r if len(set(t)) == 4)
        ]
```
- 与2Sum相似,先将总和与任意两数之和的差存入字典,再获得其余任意两个数字,寻找匹配值
- combinations(iterable, r) 创建一个迭代器,返回iterable中所有长度为r的子序列。combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

19. [Remove Nth Node From End of List](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list)
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = q = head
        for i in range(n):
            q = q.next
        if not q:
            return head.next
        while q.next:
            q = q.next
            p = p.next
        p.next = p.next.next
        return head
```
- 双指针,q先走n步,然后p和q一起走,直到q走到尾节点

24. [Swap Nodes in Pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs)
```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
```
25. [Reverse Nodes in k-Group](https://leetcode-cn.com/problems/reverse-nodes-in-k-group)
```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:  # 翻转
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
```
- 用count变量控制节点翻转范围,注意各种边界条件

28. [Implement strStr()](https://leetcode-cn.com/problems/implement-strstr)
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
```
- 暴力破解,更高效的算法有KMP,Boyer-Mooer算法和Rabin-Karp算法


44. [Wildcard Matching](https://leetcode-cn.com/problems/wildcard-matching/)
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False] * length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]
```
- '?' 可以匹配任何单个字符。'*' 可以匹配任意字符串（包括空字符串）。

65. [Valid Number](https://leetcode-cn.com/problems/valid-number/)
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True
```
66. 

67. [Add Binary](https://leetcode-cn.com/problems/add-binary/)
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return bin(a + b)[2:]

```
- 将2进制字符串转为int,相加后再转成二进制,注意对bin结果切片
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r, p = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2
        return '1' + r if p else r

```
- 模拟二进制加法

80. [Remove Duplicates from Sorted Array II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii)
- 加入一个变量记录元素出现次数

138. 复制带随机指针的链表
- 难点在于random可能指向还未创建的节点
     1. 通过字典记录对应的节点,第二次遍历添加next和random指向 
     2. 或者通过在原链表上添加节点,最后拆分的方法完成题目要求
   

141. Linked List Cycle
- 快慢指针
  

142. Linked List Cycle II
- 设环的起始节点为 E，快慢指针从 head 出发，快指针速度为 2，设相交节点为 X，head 到 E 的距离为 H，E 到 X 的距离为 D，环的长度为 L，那么有：快指针走过的距离等于慢指针走过的距离加快指针多走的距离（多走了 n 圈的 L） 2(H + D) = H + D + nL，因此可以推出 H = nL - D，这意味着如果我们让俩个慢指针一个从 head 出发，一个从 X 出发的话，他们一定会在节点 E 相遇

