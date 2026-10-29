class Solution:
    def isHappy(self, n: int) -> bool:
        repeat = set()

        def get_digits_sum(n):
            nstr = str(n)
            sum_num = 0
            for i in nstr:
                sum_num += int(i)**2
            
            return sum_num

        if get_digits_sum(n) == 1:
            return True
        else:
            repeat.add(get_digits_sum(n))

        while True: 
            n = get_digits_sum(n)
            if get_digits_sum(n) == 1:
                return True
            elif get_digits_sum(n) in repeat:
                return False
            else:
                repeat.add(get_digits_sum(n))


                
