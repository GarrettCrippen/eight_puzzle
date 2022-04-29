import copy
def up(state,row_blank,col_blank):
    b=copy.deepcopy(state)
    if(row_blank>0):
        b[row_blank][col_blank] = state[row_blank-1][col_blank]
        b[row_blank-1][col_blank] = state[row_blank][col_blank]
        return b
    else:
        return -1
def down(state,row_blank,col_blank):
    b=copy.deepcopy(state)
    if(row_blank<len(state)-1):
        b[row_blank][col_blank]= state[row_blank+1][col_blank]
        b[row_blank+1][col_blank] = state[row_blank][col_blank]
        return b
    else:
        return -1
def left(state,row_blank,col_blank):
    b=copy.deepcopy(state)
    if(col_blank>0):
        b[row_blank][col_blank] = state[row_blank][col_blank]
        b[row_blank][col_blank-1] = state[row_blank][col_blank-1]
        return b
    else:
        return -1
def right(state,row_blank,col_blank):
    b=copy.deepcopy(state)
    if(col_blank<len(state[0])-1):
        b[row_blank][col_blank] = state[row_blank][col_blank]
        b[row_blank][col_blank+1] = state[row_blank][col_blank+1]
        return b
    else:
        return -1