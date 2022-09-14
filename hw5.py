def numberMaze(l):
    lbag =  [(0,0)]
    marked= []
    while len(lbag) > 0:
        (x,y) = lbag.pop()
        s = l[x][y]
        marked.append((x,y))
        for (x2,y2) in [(-s,0),(0,s),(s,0),(0,-s)]:
            x3 = x+x2
            y3 = y+y2
            if (x3,y3) not in marked and 0 <= x3 < len(l) and 0 <= y3 < len(l):
                marked.append((x3,y3))
                lbag.append((x3,y3))
    if((len(l)-1,len(l)-1) in marked):
        return True
    else:
        return False
