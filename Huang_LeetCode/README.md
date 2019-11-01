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
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        useChar = {}  # 保存非重复字符串
        for i, ch in enumerate(s):
            if ch in useChar and start <= useChar[ch]:
                start = useChar[ch] + 1  # start 移动到字典重复字符所在的后一位
            else:
                maxLength = max(maxLength, i - start + 1)
            useChar[ch] = i  # 当前遍历字符所在索引存入字典

        return maxLength
```
- 滑动窗口问题

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


11. [Container With Most Water](https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode/)
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height) - 1
        while left < right:
            res, left, right = (max(res, height[left] * (right - left)),
                                left + 1,
                                right) if height[left] < height[right] else (
                                    max(res, height[right] * (right - left)),
                                    left, right - 1)
        return res
```
- 双指针，从两端向中间遍历，用res存贮最大面积，较短指针移向较长指针


12. [Integer to Roman](https://leetcode-cn.com/problems/integer-to-roman/)
```python
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"] #[0,1000,2000,3000]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # [0,100,200,300,400,500,600,700,800,900]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # [0,10,20,30,40,50,60,70,80,90]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # [0,1,2,3,4,5,6,7,8,9]

        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) //
                                                           10] + I[num % 10]
```

13. [Roman to Integer](https://leetcode-cn.com/problems/roman-to-integer/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china)
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'IV': 3,
            'V': 5,
            'IX': 8,
            'X': 10,
            'XL': 30,
            'L': 50,
            'XC': 80,
            'C': 100,
            'CD': 300,
            'D': 500,
            'CM': 800,
            'M': 1000
        }
        r = d[s[0]]
        for i in range(1, len(s)):
            r += d.get(s[i - 1:i + 1], d[s[i]])
        return r
```
- 构建一个字典记录所有罗马数字子串,长度为2的子串记录的值(实际值-子串左边的罗马数字的值)
- 遍历s,判断当前位置和前一个位置是否在字典内,如果在就记录值,不在就直接记录当前位置字符对应值
- 例如CD为400,先遍历到C记录为100,在遍历到CD,记录为300。相加,正好为正确值400

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


17. [Letter Combinations of a Phone Number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from itertools import product
        l = '- - abc def ghi jkl mno pqrs tuv wxyz'.split()
        return [''.join(c)
                for c in product(*[l[int(i)]
                                   for i in digits])] if digits else []
```



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

20. [Valid Parentheses](https://leetcode-cn.com/problems/valid-parentheses/)
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '[': ']', '{': '}'}
        for k in s:
            if k in '{([':
                stack.append(k)
            else:
                if not stack or d[stack.pop()] != k:
                    return False
        return not stack
```
21. [Merge Two Sorted Lists](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
```

22. [Generate Parentheses](https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode/)
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(S="", left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                generate(S + "(", left + 1, right)
            if right < left:
                generate(S + ")", left, right + 1)

        generate()
        return ans
```



23. [Merge k Sorted Lists](https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode/)
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = p = ListNode(0)
        for k in lists:
            while k:
                self.nodes.append(k.val)
                k = k.next
        for x in sorted(self.nodes):
            p.next = ListNode(x)
            p = p.next
        return head.next
```


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

26. [Remove Duplicates from Sorted Array](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index + 1
```
27. [Remove Element](https://leetcode-cn.com/problems/remove-element/)
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index
```

28. [Implement strStr](https://leetcode-cn.com/problems/implement-strstr)
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
```
- 暴力破解,更高效的算法有KMP,Boyer-Mooer算法和Rabin-Karp算法

31. [Next Permutation](https://leetcode-cn.com/problems/next-permutation/)
```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        # 从右到左遍历,找到交换点索引
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            return nums.reverse()  # 如果完全递减,将数字排成最小的序列
        else:
            nums[i:] = sorted(nums[i:])  # 交换点后的数字进行升序排列
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]  # 交换
                    break
```

32. [Longest Valid Parentheses](https://leetcode-cn.com/problems/longest-valid-parentheses/)
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0
        stack = [-1]

        for k, ch in enumerate(s):
            if ch == '(':
                stack.append(k)
            else:
                stack.pop()
                if stack:
                    maxLength = max(maxLength, k - stack[-1])
                else:
                    stack.append(k)
        return maxLength
```
33. [Search in Rotated Sorted Array](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums)
        while first != last:
            mid = first + (last - first) // 2
            if nums[mid] == target:
                return mid
            elif nums[first] <= nums[mid]:
                if nums[first] <= target and target < nums[mid]:
                    last = mid
                else:
                    first = mid + 1
            else:
                if nums[mid] < target and target <= nums[last - 1]:
                    first = mid + 1
                else:
                    last = mid
        return -1
```

35. [Search Insert Position](https://leetcode-cn.com/problems/search-insert-position/)
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target, 0, len(nums))
```
- 调用库函数
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
```

36. [Valid Sudoku](https://leetcode-cn.com/problems/valid-sudoku/)
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[x for x in y if x != '.'] for y in board]
        col = [[x for x in y if x != '.'] for y in zip(*board)]
        pal = [[
            board[i + m][j + n] for m in range(3) for n in range(3)
            if board[i + m][j + n] != '.'
        ] for i in (0, 3, 6) for j in (0, 3, 6)]
        return all(len(set(x)) == len(x) for x in (*row, *col, *pal))
```

37. [Sudoku Solver](https://leetcode-cn.com/problems/sudoku-solver/)
```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:  # row、col、block中均有val可用
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False

        backtrack()
```

38. [Count and Say](https://leetcode-cn.com/problems/count-and-say/)
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        return '1' * (n is 1) or re.sub(
            r'(.)\1*', lambda m: str(len(m.group())) + m.group(1),
            self.countAndSay(n - 1))
```
- re.sub(正则,替换字符串或函数,被替换字符串,是否区分大小写)
- '.'可匹配任意一个除了'\n'的字符。(.) 匹配任意一个除了\n的字符并把这个匹配结果放进第一组。(.)\1 匹配一个任意字符的二次重复并把那个字符放入数组。(.)\1* 匹配一个任意字符的多次重复并把那个字符放入数组
- group(default=0)可以取匹配文本。group(1)取第一个括号内的文本

39. []()
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)
```

40. [Combination Sum II](https://leetcode-cn.com/problems/combination-sum-ii/)
```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []

        self.__dfs(candidates, size, 0, [], target, res)
        return res

    def __dfs(self, candidates, size, start, path, residue, res):
        if residue == 0:
            res.append(path[:])
            return
        for index in range(start, size):
            if candidates[index] > residue:
                break
            # 剪枝的前提是数组升序排序
            if index > start and candidates[index - 1] == candidates[index]:
                continue

            path.append(candidates[index])
            # 传入index+1,当前元素不能被重复使用
            self.__dfs(
                candidates, size, index + 1, path, residue - candidates[index], res
            )
            path.pop()
```




41. [First Missing Positive](https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode/)
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
```
- 桶排序 负数、零和大于N的正数不用考虑。将1~n之内的数映射到0~n-1,最后遍历找出缺失数



42. [Trapping Rain Water](https://leetcode-cn.com/problems/trapping-rain-water/)
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # 找到最高的柱子,处理左边一半,处理右边一半
        max = 0
        for i in range(len(height)):
            if height[i] > height[max]:
                max = i
        water, peak, top = 0, 0, 0
        for i in range(max):
            if height[i] > peak:
                peak = height[i]
            else:
                water += peak - height[i]
        for i in range(len(height) - 1, max, -1):
            if height[i] > top:
                top = height[i]
            else:
                water += top - height[i]
        return water
```



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

45. [Jump Game II](https://leetcode-cn.com/problems/jump-game-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-10/)
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step
```
46. []

47. [Permutations](https://leetcode-cn.com/problems/permutations/)
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[n] + sub for i, n in enumerate(nums)
                for sub in self.permute(nums[:i] + nums[i + 1:])] or [nums]
```

- 每次固定第一个数字递归地排列数组剩余部分

```python
 class Solution:
     def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(permutations(nums))
```
- 用内置函数直接实现


47. [Permutations II](https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/)
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(set(permutations(nums)))
```

48. [Rotate Image](https://leetcode-cn.com/problems/rotate-image/)
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        for i in range(m):  # 沿着副对角线翻折
            for j in range(m - i):
                matrix[i][j], matrix[m - 1 - j][m - 1 -
                                                i] = matrix[m - 1 - j][m - 1 - i], matrix[i][j]
        for i in range(m//2):  # 沿着水平中线翻折
            for j in range(m):
                matrix[i][j], matrix[m-1-i][j] = matrix[m-1-i][j], matrix[i][j]
```

50. [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
```


51. [N-Queens](https://leetcode-cn.com/problems/n-queens/solution/hui-su-fa-by-jason-2/)
```python
class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):  # q是每列坐标
                if (
                    q not in queens and p - q not in xy_dif and p + q not in xy_sum
                ):  # 斜边条件检查(斜边坐标相减为定值,反斜边坐标相加为定值)
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
```

52. [N-Queens II](https://leetcode-cn.com/problems/n-queens-ii/)
```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):  # q是每列坐标
                if (
                    q not in queens and p - q not in xy_dif and p + q not in xy_sum
                ):  # 斜边条件检查(斜边坐标相减为定值,反斜边坐标相加为定值)
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        return len(result)
```

53. [Maximum Subarray](https://leetcode-cn.com/problems/maximum-subarray/)
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)
```
54. []()


55. [Jump Game](https://leetcode-cn.com/problems/jump-game/)
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True
```


58. [Length of Last Word](https://leetcode-cn.com/problems/length-of-last-word/)
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip(' ').split(' ')[-1])
```


60. [Permutation Sequence](https://leetcode-cn.com/problems/permutation-sequence/)
```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 0-9的阶乘
        self.fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 康托编码
        res = ''
        k -= 1
        for i in reversed(range(n)):
            cur = self.nums[k // self.fac[i]]
            res += str(cur)
            self.nums.remove(cur)
            if i != 0:
                k %= self.fac[i]
                self.fac[i] //= i
        return res
```
61. [Rotate List](https://leetcode-cn.com/problems/rotate-list/)
```python
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        len = 1
        p = head
        while p.next:
            len += 1
            p = p.next
        k = len - k % len
        # 首尾相连
        p.next = head
        step = 0
        while step < k:
            p = p.next
            step += 1
        head = p.next
        p.next = None
        return head
```

62. [Unique Paths](https://leetcode-cn.com/problems/unique-paths/)
```python
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(
            math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1)
        )
```
- 一个m行,n列的矩阵,机器人从左上走到右下需要的步数为m+n-2,其中向下走的步数是m-1。将问题转化为求组合数$C_{m+n-2}^{m-1}$


63. [Unique Paths II](https://leetcode-cn.com/problems/unique-paths-ii/)
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])  # 行和列数
        cur = [0] * c
        cur[0] = 1 - obstacleGrid[0][0]  # 判断起始点是否有障碍(障碍处设为0,无障碍处设为1)
        for i in range(1, c):  # 依次填充第一列
            cur[i] = cur[i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):  # 从上到下按行填充每一列
            cur[0] *= 1 - obstacleGrid[i][0]
            for j in range(1, c):
                cur[j] = (cur[j - 1] + cur[j]) * (
                    1 - obstacleGrid[i][j]
                )  # 每一个格子的路径等于它上方和左方的路径之和,是障碍处则设为零
        return cur[-1]
```
- 动态规划,机器人只可以向下和向右移动,因此每一个格子的路径等于它上方和左方的路径之和。用cur存储每一行的路径值,依次向下递推


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
66. [Plus One](https://leetcode-cn.com/problems/plus-one/)
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
```

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



69. [Sqrt(x)](https://leetcode-cn.com/problems/sqrtx/)
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r+x/r)//2
        return int(r)
```
- 基本不等式$(a+b)/2>=\sqrt{ab}$

70. [Climbing Stairs](https://leetcode-cn.com/problems/climbing-stairs/)
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import reduce
        return reduce(lambda r, _: (r[1], sum(r)), range(n), (1, 1))[0]
```

71. [Simplify Path](https://leetcode-cn.com/problems/simplify-path/)
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split('/'):
            if token in ('', '.'):
                pass
            elif token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)
```

73. [Set Matrix Zeroes](https://leetcode-cn.com/problems/set-matrix-zeroes/)
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix) and len(matrix[0])
        row_has_zero = False
        col_has_zero = False

        for i in range(n):
            if matrix[0][i] == 0:
                row_has_zero = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                col_has_zero = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_has_zero:
            for i in range(n):
                matrix[0][i] = 0
        if col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
```

74.  [Search a 2D Matrix](https://leetcode-cn.com/problems/search-a-2d-matrix/)
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, cols - 1
        while (i < rows and j >= 0):
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False
```

75. [Sort Colors](https://leetcode-cn.com/problems/sort-colors/)
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
```
- 双指针，两边向中间走


77. [Combinations](https://leetcode-cn.com/problems/combinations/)
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations(range(1, n + 1), k))
```


78. [Subsets](https://leetcode-cn.com/problems/subsets/)
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        return sum([list(combinations(nums, i)) for i in range(len(nums) + 1)],
                   [])
```

79. [Word Search](https://leetcode-cn.com/problems/word-search/)
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(
                board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
```


80. [Remove Duplicates from Sorted Array II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii)
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        index = 2
        for i in range(2, len(nums)):
            if nums[index - 2] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index

``` 
- 加入一个变量记录元素出现次数

81. [Search in Rotated Sorted Array II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        first, last = 0, len(nums)
        while first != last:
            mid = first + (last - first) // 2
            if nums[mid] == target:
                return True
            elif nums[first] < nums[mid]:
                if nums[first] <= target and target < nums[mid]:
                    last = mid
                else:
                    first = mid + 1
            elif nums[first] > nums[mid]:
                if nums[mid] < target and target <= nums[last - 1]:
                    first = mid + 1
                else:
                    last = mid
            else:
                first += 1
        return False
```

82. [Remove Duplicates from Sorted List II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)
```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(-1)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next
        return dummy.next
```

83. [Remove Duplicates from Sorted List](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)
```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = head
        while prev:
            while prev.next and prev.val == prev.next.val:
                prev.next = prev.next.next
            prev = prev.next
        return head
```
84. [Largest Rectangle in Histogram](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
```python
class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        ans = 0
        for k, height in enumerate(heights):
            while height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = k - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(k)
        heights.pop()
        return ans
```


86. [Partition List](https://leetcode-cn.com/problems/partition-list/)
```python
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_dummy = ListNode(-1)
        right_dummy = ListNode(-1)

        left_cur = left_dummy
        right_cur = right_dummy
        cur = head
        while cur:
            if cur.val < x:
                left_cur.next = cur
                left_cur = cur
            else:
                right_cur.next = cur
                right_cur = cur
            cur = cur.next
        left_cur.next = right_dummy.next
        right_cur.next = None
        return left_dummy.next
```

88. [Merge Sorted Array](https://leetcode-cn.com/problems/merge-sorted-array/)
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m and nums1[m - 1] > nums2[n - 1]:
                nums1[n + m - 1], m = nums1[m - 1], m - 1
            else:
                nums1[n + m - 1], n = nums2[n - 1], n - 1
```


89. [Gray Code](https://leetcode-cn.com/problems/gray-code/)
```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ i >> 1 for i in range(1 << n)]
```

90. [Subsets II](https://leetcode-cn.com/problems/subsets-ii/solution/tong-ji-pin-ci-zai-zu-he-fa-by-mai-mai-mai-mai-zi/)
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        c = Counter(nums)
        res = [[]]
        for i, v in c.items():
            temp = res.copy()
            for j in res:
                temp.extend(j + [i] * (k + 1) for k in range(v))
            res = temp
        return res
```


92. [Reverse Linked List II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)
```python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummyNode = ListNode(-1)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next
```

93. [Restore IP Addresses](https://leetcode-cn.com/problems/restore-ip-addresses/solution/bao-li-he-hui-su-by-powcai/)
```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return
        for i in range(1, 4):
            if i <= len(s):  # i要小于s的长度
                if i == 1:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                elif i == 2 and s[0] != "0":  # 选择两个数字时,不能以0开头
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
```


94. [Binary Tree Inorder Traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        r = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root.val)
                root = root.right
        return r
```

95. [Unique Binary Search Trees II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/zi-ding-xiang-xia-by-powcai/)
```python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node

        def trees(first, last):
            return [
                node(root, left, right) for root in range(first, last + 1)
                for left in trees(first, root - 1)
                for right in trees(root + 1, last)
            ] or [None]

        if n == 0:
            return []
        return trees(1, n)
```
- 递归，root遍历取完1到n，左子树为[1,root-1]的组合可能，右子树为[root+1,n]的组合可能


96. [Unique Binary Search Trees](https://leetcode-cn.com/problems/unique-binary-search-trees/)
```python
class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n]
```
- 动态规划，遍历1-n，个数为左右子树的乘积
```python
def numTrees(self, n):
    return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
```
- 公式法，[卡特兰数](https://baike.baidu.com/item/catalan/7605685?fr=aladdin) $C_0=1,C_{n+1} = \frac{2(2n+1)}{n+2}C_n$



98. []()
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        self.inOrder(root, output)

        return all([a > b for a, b in zip(output[1:], output)])

    def inOrder(self, root, output):
        if root is None:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
```
- 中序遍历结果为升序



99. [Recover Binary Search Tree](https://leetcode-cn.com/problems/recover-binary-search-tree/)
```python
class Solution:
    def __init__(self):
        self.res = []

    def recoverTree(self, root):
        self.mid(root)
        node1 = None
        node2 = None
        for i in range(len(self.res) - 1):
            if self.res[i].val > self.res[i + 1].val and node1 == None:
                node1 = self.res[i]
                node2 = self.res[i + 1]
            elif self.res[i].val > self.res[i + 1].val and node1 != None:
                node2 = self.res[i + 1]

        node1.val, node2.val = node2.val, node1.val

    def mid(self, root):
        if root is not None:
            self.mid(root.left)
            self.res.append(root)
            self.mid(root.right)
```
- 中序遍历，如果有一个降序对，交换这两个node；若有两个降序对，说明第一对的前一个node和第二对的后一个node需要交换。

100. [Same Tree](https://leetcode-cn.com/problems/same-tree/)
```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(
                p.right, q.right)
        else:
            return p is q
```
101. [Symmetric Tree](https://leetcode-cn.com/problems/symmetric-tree/)
```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L, R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False

        return isSym(root, root)
```
102. [Binary Tree Level Order Traversal](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans
```
103. [Binary Tree Zigzag Level Order Traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)
```python
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        ans = [k if i % 2 == 0 else k[::-1] for i, k in enumerate(ans)]
        return ans
```
- 层次遍历，对结果进行列表推导，反转奇数层


105. [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        n = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:n + 1], inorder[:n])
        root.right = self.buildTree(preorder[n + 1:], inorder[n + 1:])

        return root
```




107. [Binary Tree Level Order Traversal II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans[::-1]
```

108. [Convert Sorted Array to Binary Search Tree](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/dfsdi-gui-er-fen-fa-by-chencyudel/)
```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
```

- 平衡二叉搜索树：每个节点的左右子树都高度差在1以内，每个节点左子树小于右子树
- 每个节点当做根节点的时候，左子树形成的数组一定比它小，右子树形成的数组一定比他大


109. [Convert Sorted List to Binary Search Tree](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-pyt/)
```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return
        node_arr = []
        while head:
            node_arr.append(head.val)
            head = head.next

        def buildBST(nums):
            if len(nums) == 0:
                return
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            root.left = buildBST(nums[:mid])
            root.right = buildBST(nums[mid + 1:])
            return root

        return buildBST(node_arr)
```
- 链表转化为数组后,采用108题的做法

110. [Balanced Binary Tree](https://leetcode-cn.com/problems/balanced-binary-tree/)
```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1
```

111. [Minimum Depth of Binary Tree](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/er-cha-shu-de-zui-xiao-shen-du-by-leetcode/)

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        if root.left == None or root.right == None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1

        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
```
- 注意叶子结点的定义:没有子节点的节点

112. [Path Sum](https://leetcode-cn.com/problems/path-sum/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-26/)
```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```

113. [Path Sum II](https://leetcode-cn.com/problems/path-sum-ii/solution/lu-jing-zong-he-iipython-by-fei-ben-de-cai-zhu-uc4/)
```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        stack = []
        if not root:
            return []

        def help(root, sum, tmp):
            if not root:
                return []
            if not root.left and not root.right and sum - root.val == 0:
                tmp += [root.val]
                stack.append(tmp)
            sum -= root.val
            help(root.left, sum, tmp + [root.val])
            help(root.right, sum, tmp + [root.val])

        help(root, sum, [])
        return stack
```


114. [Flatten Binary Tree to Linked List](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/submissions/)
```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root is not None:
            if root.left is not None:   # 如果左子树不为空,那么找到左子树最右节点
                pre_rigth = root.left
                while pre_rigth.right is not None:
                    pre_rigth = pre_rigth.right
                pre_rigth.right = root.right # 将左子树的最右节点的指向root的右孩子
                root.right = root.left
                root.left = None
            root = root.right   # 继续下一个节点
```
- 递归的将root的左子树链接到右子树上

116. [Populating Next Right Pointers in Each Node](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)
```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left:
            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)

        return root
```
- 任意一次递归，只需要考虑子节点的 next 属性：
    1. 将左子节点连接到右子节点
    2. 将右子节点连接到 root.next 的左子节点
    3. 递归左右节点

117. [Populating Next Right Pointers in Each Node II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)
```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and (root.left or root.right):
            if root.left and root.right:
                root.left.next = root.right
            node = root.right or root.left
            head = root.next
            while head and not (head.left or head.right):
                head = head.next
            node.next = head and (head.left or head.right)

            self.connect(root.right)
            self.connect(root.left)

        return root
```
- 任意一次递归,设置子节点的next属性有三种情况:
    1. 没有子节点:直接返回
    2. 一个子节点：将这个子节点的 next 属性设置为同层的下一个节点，即为 root.next 的最左边的一个节点，如果 root.next 没有子节点，则考虑 root.next.next，依次类推
    3. 两个子节点:左子节点指向右子节点，然后右子节点同第二种情况的做法



120. [Triangle](https://leetcode-cn.com/problems/triangle/)
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        res = triangle[-1]  # 保存每行结果

        # 自底向上，从倒数第二行开始遍历
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]
```

121. []()



122. [Best Time to Buy and Sell Stock](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            max_profit, min_price = max(max_profit, price - min_price), min(
                min_price, price)
        return max_profit
```

1.   [Best Time to Buy and Sell Stock II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(b - a for a, b in zip(prices, prices[1:]) if b > a)
```
- 把连续上升拆分成多个上升,当明天的价格大于今天的价格就会产生利润，循环内计算的就是每次变化获取到的利润。

1.   [Best Time to Buy and Sell Stock III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 状态转移方程 dp[k][i]:到底i天经过k次交易得到的最大利润
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):  # k 为交易次数
            pre_max = -prices[0]  # 处理边界情况
            for i in range(1, n):  # i 为交易天数
                pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
        return dp[-1][-1]
```


1.   [Binary Tree Maximum Path Sum](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)
```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxend(node):
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0)

        self.max = float('-inf')
        maxend(root)
        return self.max
```


1.     [Valid Palindrome](https://leetcode-cn.com/problems/valid-palindrome/)
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
```

1.   [Word Ladder II](https://leetcode-cn.com/problems/word-ladder-ii/solution/bfs-level-order-traverse-by-matrix95/)
```python
import collections
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)  # 转化为set实现O(1)的in判断
        if endWord not in wordList:
            return []
        level = {beginWord}
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = node[:i] + char + node[i + 1:]
                        if n in wordList and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res
```
- 注意要把wordList转化为set,实现O(1)的in判断,否者超时
- 递归输出res


1.   [Word Ladder](https://leetcode-cn.com/problems/word-ladder/solution/dan-ci-jie-long-by-leetcode/)
```python
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(wordList or set([beginWord, endWord]))
        return bfs_words(beginWord, endWord, d)
```
- 将问题抽象在一个无向无权图中，每个单词作为节点，差距只有一个字母的两个单词之间连一条边。问题变成找到从起点到终点的最短路径
- 算法中最重要的步骤是找出相邻的节点，也就是只差一个字母的两个单词。为了快速的找到这些相邻节点，我们对给定的 wordList 做一个预处理，将单词中的某个字母用 '-' 代替

1.     [Longest Consecutive Sequence](https://leetcode-cn.com/problems/longest-consecutive-sequence/)
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        used = {x: False for x in nums}
        longest = 0
        for i in used:
            if used[i] == False:
                curr, lenright = i + 1, 0
                while curr in used:
                    lenright += 1
                    used[curr] = True
                    curr += 1
                curr, lenleft = i - 1, 0
                while curr in used:
                    lenleft += 1
                    used[curr] = True
                    curr -= 1
                longest = max(longest, lenleft + 1 + lenright)
        return longest
```

1.   [Sum Root to Leaf Numbers](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)
```python
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += val
                if node.left:
                    stack.append((node.left, val * 10 + node.left.val))
                if node.right:
                    stack.append((node.right, val * 10 + node.right.val))
        return res
```


1.   [Surrounded Regions](https://leetcode-cn.com/problems/surrounded-regions/)
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return

        m, n = len(board), len(board[0])
        save = [
            ij for k in range(m + n) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))
        ]
        # 遍历边界坐标
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "S"
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

        # 把'S'转化为'O',其他字符统一变换成'X'
        board[:] = [["XO"[c == "S"] for c in row] for row in board]
```

1.   [Palindrome Partitioning](https://leetcode-cn.com/problems/palindrome-partitioning/)
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]
```
- 分治,将大问题分解为小问题。在遍历切割字符串的过程中,递归求的回文串。

1.   [Palindrome Partitioning II](https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-3-8/)
```python
class Solution:
    def minCut(self, s: str) -> int:
        cut = [x for x in range(-1, len(s))]
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
        return cut[-1]
```


1.     [Gas Station](https://leetcode-cn.com/problems/gas-station/)
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0  # 判断整个数组是否有解
        sum = 0  # 判断当前指针的有效性
        j = -1
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sum < 0:
                j = i
                sum = 0
        return j + 1 if total >= 0 else -1
```


1.     [Candy](https://leetcode-cn.com/problems/candy/)
```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n

        # 从左到右
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        # 从右到左
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                res[i - 1] = max(res[i - 1], res[i] + 1)

        return sum(res)
```

1.     [Single Number](https://leetcode-cn.com/problems/single-number/submissions/)
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for k in nums:
            x ^= k
        return x
```

1.     [Single Number II](https://leetcode-cn.com/problems/single-number-ii/)
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
```



1.     [Copy List with Random Pointer](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)
```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d, node = {None: None}, head
        while node:
            d[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            d[node].next = d[node.next]
            d[node].random = d[node.random]
            node = node.next
        return d[head]
```
- 难点在于random可能指向还未创建的节点
     1. 通过字典记录对应的节点,第二次遍历添加next和random指向 
     2. 或者通过在原链表上添加节点,最后拆分的方法完成题目要求
   

1.     [Linked List Cycle](https://leetcode-cn.com/problems/linked-list-cycle/)
```python
class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
```
- 快慢指针
```python  
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head and head.val != None:
            head.val, head = None, head.next

        return head != None
```
1.     [Linked List Cycle II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)
```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = {None}
        while head not in s:
            s.add(head)
            head = head.next
        return head
```

```python
class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
            else:
                return None
        while head is not slow:
            head = head.next
            slow = slow.next
        return head
```
- 设环的起始节点为 E，快慢指针从 head 出发，快指针速度为 2，设相交节点为 X，head 到 E 的距离为 H，E 到 X 的距离为 D，环的长度为 L，那么有：快指针走过的距离等于慢指针走过的距离加快指针多走的距离（多走了 n 圈的 L） 2(H + D) = H + D + nL，因此可以推出 H = nL - D，这意味着如果我们让俩个慢指针一个从 head 出发，一个从 X 出发的话，他们一定会在节点 E 相遇

1.     [Reorder List](https://leetcode-cn.com/problems/reorder-list/)
```python
class Solution:
    def _splitList(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        middle = slow.next
        slow.next = None

        return head, middle

    def _reverseList(self, head):
        last = None
        currentNode = head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = last
            last = currentNode
            currentNode = nextNode

        return last

    def _mergeLists(self, a, b):

        tail = a
        head = a

        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a

        return head

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        a, b = self._splitList(head)
        b = self._reverseList(b)
        head = self._mergeLists(a, b)
```

1.     [Binary Tree Preorder Traversal](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
```python
def preorderTraversal(self, root):
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            ret.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ret
```
- 用栈模拟递归
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return root and sum(
            ([root.val],
             *map(self.preorderTraversal, [root.left, root.right])), []) or []
```
- 使用map对左右孩子分别调用,sum对list进行相加操作


1.     [Binary Tree Postorder Traversal](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        r, stack = [], root and [root] or []
        while stack:
            root = stack.pop()
            r.append(root.val)
            stack += root.left and [root.left] or []
            stack += root.right and [root.right] or []
        return r[::-1]
```
1.       [LRU Cache](https://leetcode-cn.com/problems/lru-cache/)
```python
class LRUCache:
    def __init__(self, capacity: int):
        self.od, self.cap = collections.OrderedDict(), capacity

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            del self.od[key]
        elif len(self.od) == self.cap:
            self.od.popitem(False)  # 先进先出
        self.od[key] = value
```

1.   [Insertion Sort List](https://leetcode-cn.com/problems/insertion-sort-list/solution/jia-ge-tailsu-du-jiu-kuai-liao-by-powcai/)
```python
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next
```

1.   [Sort List](https://leetcode-cn.com/problems/sort-list/)
```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(h1, h2):
            dummy = tail = ListNode(None)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next, tail, h1 = h1, h1, h1.next
                else:
                    tail.next, tail, h2 = h2, h2, h2.next
            tail.next = h1 or h2
            return dummy.next

        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return merge(*map(self.sortList, (head, slow)))
```


1.       [Evaluate Reverse Polish Notation](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for k, v in enumerate(tokens):
            if v in '+-*/':
                b, a = stack.pop(), stack.pop()
                v = eval('a' + v + 'b')
            stack.append(int(v))
        return stack.pop()
```
- 用栈模拟求解步骤
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t, f = tokens.pop(), self.evalRPN
        if t in '+-*/':
            b, a = f(tokens), f(tokens)
            t = eval('a' + t + 'b')
        return int(t)
```
- 递归地返回左右表达式操作后结果。eval 函数将字符串看作代码得到输出值


1.     [Two Sum II - Input array is sorted](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1
        while numbers[first] + numbers[last] != target:
            if numbers[first] + numbers[last] > target:
                last -= 1
            else:
                first += 1
        return [first + 1, last + 1]

```

1.     [Array Partition I](https://leetcode-cn.com/problems/array-partition-i/)
```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
```