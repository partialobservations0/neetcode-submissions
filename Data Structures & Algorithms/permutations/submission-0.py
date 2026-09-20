class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # define a operation that takes in one number and a list of lists
        # for each list in lists the number should be appended to every
        # possible location 

        def get_all_perm_from_list_and_num(num, existing):
            if not existing:
                return [[num]]
 
            solution = [] 
            for asol in existing:
                itsol = [] 
                for i,e in enumerate(asol):
                    solution.append(asol[:i] + [num] + asol[i:])
                solution.append( asol +  [num])
            return solution
        print(get_all_perm_from_list_and_num(12, [[1,2], [2,1]]))

        currsol = []
        for i in range(0,len(nums)):
            num = nums[i]
            sol = get_all_perm_from_list_and_num(num,currsol)
            print(sol)
            currsol = sol
        return currsol
