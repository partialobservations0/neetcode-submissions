class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def countChars(mystring):
            charCounts = {}
            for i,char in enumerate(mystring):
                if char in charCounts:
                    charCounts[char] += charCounts[char]
                else:
                    charCounts[char] = 1
            return charCounts

        if len(s) != len(t):
            return False
        sChars = countChars(s)
        tChars = countChars(t)
        
        skeys = sChars.keys()
        tkeys = tChars.keys()

        if len(skeys) != len(tkeys):
            return False

        for k in skeys:
            if k not in tkeys:
                return False
            if sChars[k] != tChars[k]:
                return False
        return True
     