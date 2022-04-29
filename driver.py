import node as n
import operators as op
class problem:
    def find_index_blank(state):
        for r,vrow in enumerate(state):
            for c,vcol in enumerate(vrow):
                if(vcol==None):
                    return (r,c)

    initial_state=[[7,2,4],
                 [5,None,6], 
                 [8,3,1]]
    goal_state = None
    row_blank, col_blank = find_index_blank(initial_state)
    #Move Blank {Up,Down,Left,Right}
    operators = [op.up,op.down,op.left,op.right]
    search_algorithm = None
p=problem
print(p.initial_state)
op.up(p)
op.right(p)
print(p.initial_state)