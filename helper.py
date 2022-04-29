def find_index_blank(state):
    for r,vrow in enumerate(state):
        for c,vcol in enumerate(vrow):
            if(vcol==None):
                return (r,c)
