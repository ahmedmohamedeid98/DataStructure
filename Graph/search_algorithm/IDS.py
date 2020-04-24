# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                       #
#                                           'Searching Algorithm'                                       #
#                                       /                      \                                        #
#                                      /                        \                                       #
#                                'Uniformed'                 'Informed'--------------                   #
#                              /            \               /          \             \                  #
#                             /              \             /            \             \                 #
#                           'BFS'          'DFS'       'Gready       'A* Search'   'Recursive           #
#                           /               /   \           BFS'                        BFS'            #
#                          /               /     \                                                      #
#                       'UCS'            'DLS'  ['Iterative                                             #
#                                                   Deeping']                                           #
#                                                                                                       #
#                                                                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IDS : Iterative Depth Search
# Properities
# Complete : traferse for infinity so it allways find the goal.
# Optimal: if the limit = 1, then it will find the first goal then the others.
# Time complexity: O(b^d), b is branch factor and d is a depth level.
# Space complexity: O(bd)

# Idea
# this algorithm is just improvement for the DLS algo.
# DLS = DFS + BFD.
# it find out the best depth limit and does it by gradually increasing the limit until a goal is found.
# the node at the depth limit will treat as it as a leaf.
# it combines the benefits of BFS and DFS search algorithm in terms of fast search and memory efficiency.

# example: find the path from Arad to Bucharest.

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#                                                                                                                 #
#           'Oradea'                                                                                              #  
#          /        \                                                                                             #  
#         /          \                                                                                            #
#     'Zerind'        \                                            'Neamt'                                        #
#        /             \                                              \                                           #
#       /               \                                              \                                          #
#    'Arad'-----------'Sibiu'__                                         \                                         #
#       |                 \    \_______________'Fegaras'               'lasi'                                     #
#       |                  \                            \                 \                                       #                  
#       |                   \                            \                 \                                      #
#    'Timisoara'      'Rimnicu Vilcea'____                \                 \                                     #
#           \                \            \                \                 \                                    #
#            \                \            \               |               'Vaslui'                               #
#             \                \            \              |                    /                                 #
#              \                \            \             |                   /                                  #
#            'Lugoj'             \         'Pitesti'       |                  /                                   #
#               |                 \             /  \       |                 /                                    #
#               |                  \           /    \      |                /                                     #
#           'Mehadia'               \         /      \     |               /                                      #
#               |                    \       /        \    |              /                                       #
#               |                     \     /          \   |          'Urziceni'----------'Hirsova'               #
#               |                      \   /            \  |            /                       \                 #
#           'Drobeta'                   \ /          'Bucharest'________|                        \                #
#                   \________________'Craiova'          /                                         \               #
#                                                      /                                        'Eforie'          #
#                                                     /                                                           #
#                                                 'Giurgiu'                                                       #
#                                                                                                                 #
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #



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

def DLS(limit, start, goal):
    solution = Recursive_DLS(start, goal, limit, [])

    if solution:
        return solution

    else:
        return 0

def Recursive_DLS(current, goal, limit, solution):
    solution.append(current)
    if current == goal:
        return solution
    elif limit == 0:
        return 0
    else:
        for child in graph[current]:
            found = Recursive_DLS(child, goal, limit - 1, solution)
            if found:
                return found
        return 0

# ============ Iterative Depth Search =============== #

def IDS(start, goal):
    limit = 0
    while 1:
        limit += 1
        result = DLS(limit, start, goal)
        if result != 0 :
            return result


print(IDS('Arad', 'Bucharest'))

# output
# 