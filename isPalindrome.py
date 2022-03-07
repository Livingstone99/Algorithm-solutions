class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num = str(x)
            if num[::-1] == num:
                return True
            else:
                return False