class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        mapping = {i:[] for i in range(n)}
        for source, target in edges:
            mapping[source].append(target)
            mapping[target].append(source)

        visited = set()
        cycle = set()
        def dfs(node,parent):
            
            if node in cycle:
                return True
            if node in visited:
                return False
            
            cycle.add(node)
            next_target = mapping.get(node,None)
            for target in next_target:
                if target == parent:
                    continue
                if dfs(target, node):
                    return True
            cycle.discard(node)
            visited.add(node)
            return False

        if dfs(0,-1):
            return False
        
        return len(visited) == n
            




