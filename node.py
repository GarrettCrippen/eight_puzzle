from cmath import inf
import operators as op
import helper
operators = [op.up,op.down,op.left,op.right]
created = set()
class node:
    def __init__(self,state,parent=None,last_action='intial_state',depth=0,cost=-inf):
        self.state=state
        self.parent=parent
        self.children=[]
        self.last_action=last_action
        self.depth=depth
        self.cost=cost
        print(f'child created from:{last_action}')
    def add_children(self,child):
        self.children.append(child)

class Tree:
    def __init__(self,root):
        Tree.root=root
    def create_children(self,current_node):
        states=[]
        row_blank,col_blank = helper.find_index_blank(current_node.state)
        for operator in operators:
            print(f'1)action: {current_node.last_action}')
            #do not repeat the opposite of the last operator
            if(operator.__name__=='down' and current_node.last_action=='up' or \
                operator.__name__=='up' and current_node.last_action=='down' or \
                operator.__name__=='left' and current_node.last_action=='right' or \
                operator.__name__=='right' and current_node.last_action=='left' ):
                #print(f'aciton repeated{operator.__name__,self.last_action}')
                new_state=-1
            else:
                new_state=operator(current_node.state,row_blank,col_blank)
                if(new_state!=-1):
                    child=node(state=new_state,parent=current_node,last_action=operator.__name__,depth=current_node.depth+1)
                    print(f'2)action: {current_node.last_action}')
                    states.append(child)
        current_node.children=states

k=Tree(node([[7,2,4],[5,None,6],[8,3,1]]))
k.create_children(k.root)
print(k.root.state,k.root.children[3].state)
# #print(k.manhattan_distance([[1,2,3],[4,5,6],[7,8,None]]))
# #print(k.eucledian_distance([[1,2,3],[4,5,6],[7,8,None]]))
# k.populate(3)
# for child in k.children:
#     print(child.state)
# #print(k.state,k.children[0].children[1])
# #print(operators[2](k.state,*helper.find_index_blank(k.state)))


