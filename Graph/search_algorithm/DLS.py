# DLS : Depth Limit Search
# Properities
# 1- Incomplete : the goal may be exist after the limit.
# 2- Non-Optimal: DLS is the same as DFS which traferse the whole branch before move to the next.
# 3- Time-Complexity: O(b^l), where b is the branch factor and l is the limit.
# 4- Space-Complexity: O(bl) -> (l-1)*(b-1) + b

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                 #
#                           'A'                          L = 0                    #
#                         /     \                                                 #
#                        /       \                                                #  
#                      'B'       'C'                     L = 1                    #
#                     /   \     /   \                                             #
#                    /     \   /     \                                            #
#                  'D'    'E' 'F'   'G'                  L = 2  (limit)           #
#             -------------------------------                                     #
#                        /   \                                                    #
#                       /     \                                                   #
#                     'H'     'I'                        L = 3                    #
#                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

 
# # # # # # # # # # # # # # # # # # # # # # # # # # #
#                    'A'                            #
#                   /   \                           #
#                  /     \                          #
#                'B'     'C'                        #
#               /   \       \                       #
#              /     \       \                      #
#            'D'     'E'---> 'F'                    #
#                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # 

def DLS(limit, start, goal):
    solution = Recursive_DLS(start, goal, limit, [])

    if solution:
        print("Goal path: ",solution)

    else:
        print("Error")

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



DLS(2, 'A', 'F')

# output
# Goal path:  ['A', 'B', 'D', 'E', 'C', 'F']
