class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) < 2: 
            return True

        sd = "".join([i for i in s if i.isalnum()])
        s = sd.lower()

        l = len(s)
        for i in range(0,len(s)//2):
            c = s[i]
            cc = s[l - i - 1]
            if c == cc:
                continue
            else:
                return False
        return True