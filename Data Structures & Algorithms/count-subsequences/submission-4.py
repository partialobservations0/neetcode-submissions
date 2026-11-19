class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # we have two string the easiest way to visualize a solution
        # is two consider a 2 D matrix with rows represeting one string
        # and cols represeting the other string
        # after that we have to go over all possible combinations
        # of i,j that is power set of size ixj to determine the solution
        # we need subseq of s equal to t

        # lets write t on col and s on rows
        # we need to first put mark all cs in s
        # those are starting points
        # then the problem is reduced to finding 1 + num(s[x:] and t[1:])

        def countNums(sd,td,memo):

            if not td: 
                return 1
            if not sd: 
                return 0

            if (sd,td) in memo:
                return memo[sd,td]

            mainchar = td[0]
            indices = [i for i,n in enumerate(sd) if sd[i] == mainchar]

            if len(td) == 1:
                return len(indices)
            count = 0
            for ind in indices:
                count += countNums(sd[ind+1:], td[1:], memo)

            memo[(sd,td)] = count
            return count
        return countNums(s,t,{})         