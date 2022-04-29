def up(self):
    row_blank = self.row_blank
    col_blank = self.col_blank
    state=self.initial_state
    if(row_blank>0):
        print('swaping')
        state[row_blank][col_blank],state[row_blank-1][col_blank] = \
        state[row_blank-1][col_blank],state[row_blank][col_blank]
        self.row_blank-=1
        return 1
    else:
        return -1
def down(self):
    row_blank = self.row_blank
    col_blank = self.col_blank
    state=self.initial_state
    if(row_blank<len(state)-1):
        state[row_blank][col_blank],state[row_blank+1][col_blank] = \
        state[row_blank+1][col_blank],state[row_blank][col_blank]
        self.row_blank+=1
        return 1
    else:
        return -1
def left(self):
    row_blank = self.row_blank
    col_blank = self.col_blank
    state=self.initial_state
    if(col_blank>0):
        state[row_blank][col_blank],state[row_blank][col_blank-1] = \
        state[row_blank][col_blank-1],state[row_blank][col_blank]
        self.col_blank-=1
        return 1
    else:
        return -1
def right(self):
    row_blank = self.row_blank
    col_blank = self.col_blank
    state=self.initial_state
    if(col_blank<len(state[0])-1):
        state[row_blank][col_blank],state[row_blank][col_blank+1] = \
        state[row_blank][col_blank+1],state[row_blank][col_blank]
        self.col_blank+=1
        return 1
    else:
        return -1