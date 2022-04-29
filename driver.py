import node as n
import operators as op
import helper as h

class problem:
    initial_state=[[7,2,4],
                 [5,None,6], 
                 [8,3,1]]

    goal_state = [[1,2,3],
                 [4,5,6], 
                 [7,8,None]]

    #store the index of the blank
    row_blank, col_blank = h.find_index_blank(initial_state)

    #able to move the blank up, down, left or right
    operators = [op.up,op.down,op.left,op.right]
    search_algorithm = None

p=problem
print(p.initial_state)
print(p.operators[2](p))
