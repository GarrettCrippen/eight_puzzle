import operators as op
import helper
operators = [op.up,op.down,op.left,op.right]
class node:
    def __init__(self,state):
        node.state=state
        node.parent=None
        node.children=None
        node.last_action="initial_state"
    def populate(self,nf):
        if nf>0:
            row_blank,col_blank = helper.find_index_blank(self.state)
            new_state=-1
            for operator in operators:
                if(operator.__name__=='down' and self.last_action=='up' or \
                    operator.__name__=='up' and self.last_action=='down' or \
                    operator.__name__=='left' and self.last_action=='right' or \
                    operator.__name__=='right' and self.last_action=='left' ):
                    new_state=-1
                else:
                    new_state=operator(self.state,row_blank,col_blank)
                if(new_state!=-1):
                    child= node(new_state)
                    child.parent = self
                    child.last_action = operator.__name__
                    if (self.children):
                        self.children.append(child)
                    else:
                        self.children=[child]
                    print(f'parent.state:{self.state}, child.state: {child.state}')
                    child.populate(nf-1)
            else:
                return -1
t=node([[1,2,None],[4,5,3],[7,8,6]])
t.populate(15)
                    