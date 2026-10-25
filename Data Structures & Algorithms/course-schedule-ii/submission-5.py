class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        mapping = {}
        for crs in range(numCourses):
            mapping[crs] = []
        for pr in prerequisites:
            a, b = pr
            mapping[a].append(b)
        visited = []
        done=set()
        def dfs(crs, cycle):
            prs = mapping[crs]
            if crs in cycle: 
                return False
            if crs in done:
                return True

            cycle.add(crs)
            for pre in mapping[crs]:
                if dfs(pre,cycle) == False:
                    return False 
            cycle.remove(crs)
            done.add(crs)
            visited.append(crs)           
            return True
        
        for crs in range(numCourses):
            if not dfs(crs,set()):
                return []

        return visited

            
