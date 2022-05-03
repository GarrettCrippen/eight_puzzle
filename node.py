import heuristics
import operators as op
import helper
operators = [op.up,op.down,op.left,op.right]
answers=[]
goal_state=[[1,2,3],[4,5,6], [7,8,None]]
class node:
    def __init__(self,state,parent=None,last_action='intial_state',depth=0,cost=0,total_nodes=1,visited_set=set()):
        self.state=state
        self.parent=parent
        self.children=[]
        self.last_action=last_action
        self.depth=depth
        self.cost=cost
        node.total_nodes=total_nodes
        node.visited_set=visited_set
        #print(f'child created from:{last_action}')    
    #creates tree and runs algorithm at the same time
    #Returns a priority queue of goal states
    def run_algorithm(self,nf=10,heuristic=heuristics.uniform_cost):
        if(nf > 0):
            #add current state to visited_set
            
            #add node to visited set
            if tuple(map(tuple,self.state)) not in self.visited_set:
                self.visited_set.add(tuple(map(tuple,self.state)))
                #print(f'added:{tuple(map(tuple,self.state))}')
            
            #Create a Priority Queue
            q=[]
            row_blank,col_blank = helper.find_index_blank(self.state)
            for operator in operators:
                #do not repeat the opposite of the last operator
                if(operator.__name__=='down' and self.last_action=='up' or \
                    operator.__name__=='up' and self.last_action=='down' or \
                    operator.__name__=='left' and self.last_action=='right' or \
                    operator.__name__=='right' and self.last_action=='left' ):
                    new_state=-1
                else:
                    new_state=operator(self.state,row_blank,col_blank)
                    #check if state is already visited
                    if(new_state!=-1 and tuple(map(tuple,new_state)) not in self.visited_set):
                        child=node(state=new_state,parent=self,last_action=operator.__name__,depth=self.depth+1,cost=self.depth+heuristic(new_state,goal_state),total_nodes=self.total_nodes+1,visited_set=self.visited_set)
                        self.children.append(child)
                        q.append((child.cost,child))
            
            #Check if state is a goal_state
            q=sorted(q, key = lambda x:x[0])
            while len(q):
                c=q.pop(0)
                if(c[1].state==[[1,2,3],[4,5,6], [7,8,None]]):
                    #save the answer, but keep looking because we may find a better path
                    #print(f'goal state found at depth:{c[1].depth}')
                    answers.append(c)
                else:
                    #Create children with the best cost
                    c[1].run_algorithm(nf-1,heuristic)

        return sorted(answers, key = lambda x:x[0])

    #prints the state in a readable way
    def print_pretty(self):
        print('----------------------------')
        for row in self.state:
            for col in row:
                print(f'|    {str(col).replace("None","*")}   ',end='')
            print('|')
            print('----------------------------')
        print('\n')

    #traces the answer from a goal state
    def trace_path(self):
        stack = []
        temp=self
        print(f'depth: {self.depth}\nexpanded: {self.total_nodes}\nmax nodes in queue: {len(self.visited_set)}\n')
        total_nodes=1
        while(temp):
            stack.append(temp)
            temp=temp.parent
        
        while(len(stack)):
            step = stack.pop()
            print(f'parent:{hex(id(step.parent))} ')
            print(f'child:{hex(id(step))}')
            print(f'move:{step.last_action}')
            step.print_pretty()



