
#*Not Part of Project Requirements*
def manhattan_distance(state,goal_state):
    distance = 0
    #Intuition to calculate the manhattan distance:
    #1-(0,0), 2-(0,1), 3-(0,1), 4(1,0), 5(1,1), 6(1,2), 7(2,0), 8(2,1), None(2,2)
    #So, each number should have row = (number-1)//num_rows, col = (number-1)%num_cols

    num_rows = len(state)
    num_cols = len(state[0])
    for r,row in enumerate(state):
        for j,value in enumerate(row):
            #Calculate how far it is from the correct position
            if(value!=goal_state[r][j]):
                if(value):
                    desired_row=(value-1)//num_rows
                    desired_col=(value-1)%num_cols
                    # print(f'value\'s row:{value} is off by {abs(desired_row-r)}')
                    # print(f'value\'s col:{value} is off by {abs(desired_col-j)}')
                    distance+=abs(desired_row-r)
                    distance+=abs(desired_col-j)
                #None Case
                else:
                    pass
    return distance
#For A* Algorithm: cost_function = [g(n)=depth of tree] + [h(n) = sum of squared distances]
def eucledian_distance(state,goal_state):
    distance = 0
    #Intuition to calculate the eucledian distance:
    #Modify the manhattan distance to take the sum of squared distances

    num_rows = len(state)
    num_cols = len(state[0])
    for r,row in enumerate(state):
        for j,value in enumerate(row):
            #Calculate how far it is from the correct position
            if(value!=goal_state[r][j]):
                if(value):
                    desired_row=(value-1)//num_rows
                    desired_col=(value-1)%num_cols
                    distance+=pow(pow((desired_row-r),2) +pow((desired_col-j),2),.5)
                
                #None Case
                else:
                    pass
    return distance

    return distance

#For A* Algorithm: cost_function = [g(n)=depth of tree] + [h(n) = # of misplaced tiles]
def misplaced_tile(state,goal_state):
    distance = 0
    for r,row in enumerate(state):
        for j,value in enumerate(row):
            if value is not None and value != goal_state[r][j]:
                distance+=1
    return distance

#cost_function = [g(n)=depth of tree] + 0
def uniform_cost(state,goal_state):
    return 0