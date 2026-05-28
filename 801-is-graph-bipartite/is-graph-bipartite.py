class Solution:
    def dfs(self, graph, visited, color, node):
        visited[node] = color
        for adj_node in graph[node]:
            if visited[adj_node] != -1:
                if visited[adj_node] == color:
                    return False
            else:
                if color == 1:
                    ans = self.dfs(graph, visited, 0, adj_node)
                else:
                    ans = self.dfs(graph, visited, 1, adj_node)

                if ans == False:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        total_nodes = len(graph)
        visited = [-1] * total_nodes
        for i in range(total_nodes):
            if visited[i] == -1:
                ans = self.dfs(graph, visited, 0, i)

                if ans == False:
                    return False
        
        return True