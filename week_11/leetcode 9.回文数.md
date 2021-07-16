---

title: 9.回文数(简单)

tags:
- 字符串

---

判断一个数字是否正反读都一样

---

直接转化为字符串，但是要占用新的空间.

python实现

'''
    
    class Solution(object):
        def isPalindrome(self, x):
            """
            :type x: int
            :rtype: bool
            """
            if x<0:
                return False
            x=str(x)
            return x==x[::-1]
'''

时间复杂度O(1)    
空间复杂度O(n)
