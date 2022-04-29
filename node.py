import operators as op
import helper
operators = [op.up,op.down,op.left,op.right]

class node:
    def __init__(self,state,parent=None):
        node.state=state
        node.parent=parent
        node.children=None
        node.last_action="initial_state"
    def manhattan_distance(self,goal_state):
        distance = 0
        state= self.state
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
    def populate(self,nf=10):
        #do not go past nesting factor
        if(nf>0):
            row_blank,col_blank = helper.find_index_blank(self.state)
            for operator in operators:
                #Do not repeat the opposite of the last operator
                if(operator.__name__=='down' and self.last_action=='up' or \
                    operator.__name__=='up' and self.last_action=='down' or \
                    operator.__name__=='left' and self.last_action=='right' or \
                    operator.__name__=='right' and self.last_action=='left' ):
                    new_state=-1
                else:
                    new_state = operator(self.state,row_blank,col_blank)
                #valid state
                if(new_state!=-1):     
                    child = node(new_state,parent=self)
                    child.last_action=operator.__name__
                    if new_state == [[1,2,3],[4,5,6],[7,8,None]]:
                        return child 
                    #print(f'creating child: {child},from parent: {self} using operater:{operator}')  
                    if self.children is None:
                        self.children = [child]
                    else:
                        self.children.append(child)
                    nf=nf-1
                    child.populate(nf)
        #not a valid state
        else:
            return -1

t=node([[1,2,None],[4,5,3],[7,8,6]])
h=t.populate(15)
print(h.state,h.parent.state)
# while(h != h.parent):
#     print(h.parent.state,h.last_action,h.state)
#     h=h.parent


