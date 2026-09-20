class Solution:
    def isValid(self, s: str) -> bool:
        mylist = []
        brackets = {}
        brackets['['] = ']'
        brackets['{'] = '}'
        brackets['('] = ')'
        for br in s:
            if br in brackets.keys():
                mylist.append(br)
            if br in brackets.values():
                try:
                    obr = mylist.pop()
                except:
                    return False
                if brackets[obr] == br:
                    continue
                else:
                    return False
        if len(mylist) > 0:
            return False
        return True
            