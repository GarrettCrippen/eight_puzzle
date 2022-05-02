import operators as op
import helper
operators = [op.up,op.down,op.left,op.right]
created = set()
class node:
    def __init__(self,state):
        node.state=state
        node.parent=None
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
    def eucledian_distance(self,goal_state):
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
                        distance+=pow(pow((desired_row-r),2) +pow((desired_col-j),2),.5)
                    
                    #None Case
                    else:
                        pass
        return distance

        return distance
    def misplaced_tile(self,goal_state):
        distance = 0
        for r,row in enumerate(self.state):
            for j,value in enumerate(row):
                if value is not None and value != goal_state[r][j]:
                    #print(f'{value} != {goal_state[r][j]}')
                    distance+=1
        return distance
    def populate(self,nf):
        #do not go past nesting factor
        if(nf>0):
            row_blank,col_blank = helper.find_index_blank(self.state)
            for operator in operators:
                #do not repeat the opposite of the last operator
                if(operator.__name__=='down' and self.last_action=='up' or \
                    operator.__name__=='up' and self.last_action=='down' or \
                    operator.__name__=='left' and self.last_action=='right' or \
                    operator.__name__=='right' and self.last_action=='left' ):
                    new_state=-1
                else:
                    new_state = operator(self.state,row_blank,col_blank)
                #valid state
                if(new_state!=-1):   
                    #create the child
                    print(self.state,operator.__name__,new_state)  
                    child = node(new_state)
                    child.parent=self
                    child.last_action=operator.__name__
                    #print(f'calling {child.state} from {self.state}')
                    #child.populate(nf-1)
                    # if new_state == [[1,2,3],[4,5,6],[7,8,None]]:
                    #     return child 
                    #print(f'creating child: {child},from parent: {self} using operater:{operator.__name__}')  
        #not a valid state
        else:
            return -1

k=node([[7,2,4],[5,None,6],[8,3,1]])
print(k.manhattan_distance([[1,2,3],[4,5,6],[7,8,None]]))
print(k.eucledian_distance([[1,2,3],[4,5,6],[7,8,None]]))
#k.populate(3)
#print(operators[2](k.state,*helper.find_index_blank(k.state)))


