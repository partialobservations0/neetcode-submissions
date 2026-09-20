class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # lets see permutation is what? 
        # abc -> cab , cba, bac, etc.
        # mainly permutation we can characterize by frequency counts isnt it?
        # abcc -> a:1, b:1, c:2 

        # to return if s2 contains a permutation of s1
        # lets characterize s1 by its freq_count
        # and lets take freq count of s2 and then check if for each char in s1
        # its freq in s2 equal to s1
        # does the permutation need to be contiguous?
        # if contiguous then 
        # for each starting point in s2 we will check if the freq of s2 and s1 match

        # i think we can compute nd match the freq on the go 

        

        def compute_counts(s):
            counts = {}
            for i in range(len(s)):
                counts[s[i]] = counts.get(s[i], 0) + 1
            return counts

        def get_candidate(s,i,j):
            """
            function to check if j is greater than len s
            else return s[i:j]
            """
            if j < len(s):
                return s[i:j]
            else:
                return None 

        def match_counts(count1, count2):
            for c in count1:
                if c in count2:
                    if count2[c] == count1[c]:
                        continue
                    else:
                        return False
                else:
                    return False
            return True

        def update_counts(s,prev_i,new_j,count):
            # to check if prev_i and next_j exists
            count[s[prev_i]] = count[s[prev_i]] - 1
            count[s[new_j]] = count.get(s[new_j],0)+1
            return count

        def main():

            if not s1:
                return False
            if not s2:
                return False
            if len(s1)==1:
                if s1 in s2:
                    return True
                else:
                    return False
            if len(s1) == len(s2):
                if match_counts(compute_counts(s1), compute_counts(s2)):
                    return True
                else:
                    return False

            s1count = compute_counts(s1)
            candidate_count = compute_counts(s2[0:len(s1)])
            #print(candidate_count)
            for i in range(1,len(s2)):
                #candidate = s2[i:i+len(s1)]
                candidate = get_candidate(s2,i,i+len(s1)-1)
                if candidate:
                    print(candidate)
                    candidate_count[s2[i-1]] = candidate_count[s2[i-1]] - 1
                    candidate_count[s2[i+len(s1)-1]] = candidate_count.get(s2[i+len(s1)-1],0) + 1
                    print(candidate_count)                    
                    # replace with update_and_match_count
                    if match_counts(s1count, candidate_count):
                        return True
            return False
        return main()


