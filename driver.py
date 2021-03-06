import node as n
import operators as op
import helper as h
import node
import heuristics
import copy

class problem:

    #Init with initial_state and goal_state
    #If you want to change the goal_state, change it at the top of node.py aswell
    def __init__(self,initial_state=[[7,2,4],[5,None,6], [8,3,1]],goal_state=[[1,2,3],[4,5,6], [7,8,None]]):
        self.initial_state=initial_state
        self.goal_state = goal_state

    sample_states=[('Trivial',[[1,2,3],[4,5,6],[7,8,None]]),('Very Easy',[[1,2,3],[4,5,6],[7,None,8]]),('Easy',[[1,2,None],[4,5,3],[7,8,6]]),\
    ('doable',[[None,1,2],[4,5,3],[7,8,6]]),('Oh Boy',[[8,7,1],[6,None,2],[5,4,3]]),('IMPOSSIBLE',[[1,2,3],[4,5,6],[8,7,None]])]

    #able to move the blank up, down, left or right
    operators = [op.up,op.down,op.left,op.right]
    search_algorithms = [heuristics.uniform_cost, heuristics.eucledian_distance, heuristics.manhattan_distance]

    #create menu to test test_cases
    def menu(self):
        algo=-1
        t=-1
        custom=None
        print('Select a test_case you would like to use: ')
        for i in range(len(self.sample_states)):
            print(f'{i+1}: {self.sample_states[i][0]}')
        print('7: Custom <e.g. 123456780>')
        t= int(input())
        if(t in range(1,8)):
            #not checking for invalid inputs
            if t == 7:
                print(f'input test_case: ',end='')
                custom=str(input())
            print('Please select search algorithm: ')
            print('1) Uniform-Cost Search')
            print('2) A* Search with Misplaced Tile Heuristic')
            print('3) A* Search with Eucledian Distance Heuristic')
            algo=int(input())
            print('Press any key to continue...')
            input()
        if(algo in range(1,4)):
            #User selected one of the sample test-cases
            if t != 7:
                k= node.node(self.sample_states[t-1][1])
            #User Selected custom user test-case
            else:
                custom_state= copy.deepcopy(self.initial_state)
                #just replace initial state entries with custom values
                for r,row in enumerate(custom_state):
                    for j,col in enumerate(row):
                        if(int(custom[:1])!=0):
                            custom_state[r][j]=int(custom[:1])
                        else:
                            custom_state[r][j]=None
                        custom =custom[1:]
                k=node.node(custom_state)
            #Trivial Case = Already Solved
            if t== 1:
                k.trace_path()
            #Run Algorithm
            else:
                #NF default = 10, change this for harder problems
                solutions=k.run_algorithm(25,self.search_algorithms[algo-1])
                if len(solutions):
                    solutions=solutions.pop(0)[1]
                    solutions.trace_path()
                else:
                    print('Solution Not Found: try changing the nf in source code or not intial_state is impossible')

p=problem()
p.menu()

#-----------Example solutions for 4)doable with nf = 10-----------

#Uniform Cost Search
# depth: 4
# expanded: 586
# max nodes in queue: 333

#Misplaced Tile
# depth: 4
# expanded: 574
# max nodes in queue: 325

#Eucledian Distance
# depth: 4
# expanded: 574
# max nodes in queue: 325

# =>intial_state
# ----------------------------
# |    *   |    1   |    2   |
# ----------------------------
# |    4   |    5   |    3   |
# ----------------------------
# |    7   |    8   |    6   |
# ----------------------------


# =>right
# ----------------------------
# |    1   |    *   |    2   |
# ----------------------------
# |    4   |    5   |    3   |
# ----------------------------
# |    7   |    8   |    6   |
# ----------------------------


# =>right
# ----------------------------
# |    1   |    2   |    *   |
# ----------------------------
# |    4   |    5   |    3   |
# ----------------------------
# |    7   |    8   |    6   |
# ----------------------------


# =>down
# ----------------------------
# |    1   |    2   |    3   |
# ----------------------------
# |    4   |    5   |    *   |
# ----------------------------
# |    7   |    8   |    6   |
# ----------------------------


# =>down
# ----------------------------
# |    1   |    2   |    3   |
# ----------------------------
# |    4   |    5   |    6   |
# ----------------------------
# |    7   |    8   |    *   |
# ----------------------------