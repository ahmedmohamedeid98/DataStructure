# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                       #
#                                           'Searching Algorithm'                                       #
#                                       /                      \                                        #
#                                      /                        \                                       #
#                                'Uniformed'                 'Informed'--------------                   #
#                              /            \               /          \             \                  #
#                             /              \             /            \             \                 #
#                          ["BFS"]          'DFS'       'Gready       'A* Search'   'Recursive          #
#                           /               /   \           BFS'                        BFS'            #
#                          /               /     \                                                      #
#                       'UCS'            'DLS'  'Iterative                                              #
#                                                   Deeping'                                            #
#                                                                                                       #
#                                                                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# BFS Algorithm
# Implementation : Queue First In First Out (FIFO)
# Properities
# Complete: allways find Goal.
# Optimal: Find the first Goal.
# Time Complexity: O(b^d), b is a branch factor, d is a level.
# Space Complexity: O(b^d).

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

def bfs(graph, frm, to):
    visited = []
    queue = [frm]
    while queue:
        s = queue.pop(0)
        visited.append(s)
        print(s, end=" ")
        if s == to:
            print('')
            break
        for neighbour in graph[s]:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)

bfs(graph, 'Arad', 'Bucharest')


# output #
# Arad Zerind Sibiu Timisoara Oradea Fegaras Rimnicu Vilcea Lugoj Bucharest