# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                       #
#                                           'Searching Algorithm'                                       #
#                                       /                      \                                        #
#                                      /                        \                                       #
#                                'Uniformed'                 'Informed'--------------                   #
#                              /            \               /          \             \                  #
#                             /              \             /            \             \                 #
#                           'BFS'          ["DFS"]        'Gready       'A* Search'   'Recursive         #
#                           /               /   \           BFS'                        BFS'            #
#                          /               /     \                                                      #
#                       'UCS'            'DLS'  'Iterative                                              #
#                                                   Deeping'                                            #
#                                                                                                       #
#                                                                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# DFS: Depth First Search
# Properities
# Incomplete: if there is a cycle in the graph then no way to find Goal.
# Non-Optimal: if there is two Goal the first in the right side and the first level. and
# the second in the last level in left side, then it find the first the the second.
# Time complexity: O(b^m) m the number of leaves.
# Sace complexity: (m-1)*(b-1)+b -> O(bm)  





# Example: find the path from Arad to Bucharest



graph = {
    'Oradea' : ['Zerind', 'Sibiu'],
    'Zerind' : ['Oradea', 'Arad'],
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Sibiu' : ['Arad', 'Oradea', 'Fegaras', 'Rimnicu Vilcea'],
    'Fegaras' : ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea' : ['Sibiu', 'Pitesti', 'Craiova'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia' : ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Pitesti': ['Rimnicu Vilcea', 'Bucharest', 'Craiova'],
    'Bucharest' : ['Pitesti', 'Fegaras', 'Giurhiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni' : ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie' : ['Hirsova'],
    'Vaslui' : ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt' : ['Iasi']
}


def dfs(graph, frm, to):
    visited = []
    stack = [frm]
    while stack:
        s = stack.pop(-1)
        visited.append(s)
        print(s, end=" ")
        if s == to:
            print('')
            break
        for neighbour in reversed(graph[s]):
            if neighbour not in visited and neighbour not in stack:
                stack.append(neighbour)

dfs(graph, 'Arad', 'Bucharest')

# output #
# Arad Zerind Oradea Sibiu Fegaras Bucharest.