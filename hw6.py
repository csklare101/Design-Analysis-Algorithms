def undirect(d):
    adj = {}
    for u in d:
        adj[u] = []
    for u in d:
        for v in d[u]:
            adj[u].append(v)
            if v not in adj:
                adj[v] = []
            adj[v].append(u)
    return adj

def is_cut(g,v):
    marked = {}
    nodes = {}
    count = 0
    for v2 in g:
        marked[v2] = False
        nodes[v2] = []
    for w in g[v]:
        if not marked[w]:
            nodes = is_cutr(g,w,marked,nodes)
            
    for i in range(len(nodes)):
        if nodes[i] == v:
            count+=1
    if count >= 2:
        return True
    return False
            
def is_cutr(g,v,marked,nodes):
    marked[v] = True
    for w in g[v]:
        if not marked[w]:
            nodes[w] = v
            is_cutr(g,w,marked,nodes)
    return nodes

def prereqs():
    D = {}
    while True:
        try:
            a,b = input('requires, required: ').split(',')
            a = a.strip()
            b = b.strip()
        except:
            break
        if a in D:
            D[a].append(b)
        else:
            D[a] = [b]
        if b not in D:
            D[b] = []
    return post_order(D)

def post_order(D):
    marked = {}
    prereq = []
    for v in D:
        marked[v] = False
    for v in D:
        if not marked[v]:
            post_orderR(D,v,marked,prereq)
    return prereq

def post_orderR(D,v,marked,prereq):
    marked[v] = True

    for w in D[v]:
        if not marked[w]:
            post_orderR(D,w,marked,prereq)
        if w not in prereq:   
            prereq.append(w)
    if v not in prereq:
        prereq.append(v)
    return prereq
   
            


def prereqs2():
    D = {}
    while True:
        try:
            a,b = input('requires, required: ').split(',')
            a = a.strip()
            b = b.strip()
        except:
            break
        if a in D:
            D[a].append(b)
        else:
            D[a] = [b]
        if b not in D:
            D[b] = []
    if checkCycle(D):
        return post_order(D)
    else:
        return False

def checkCycle(D):
    new = []
    active = []
    finished = []
    for v in D:
        new.append(v)
    for v in D:
        if v in new:
            if checkCycleDFS(D,v,new,active,finished) == False:
                return False
    return True

def checkCycleDFS(D,v,new,active,finished):
    active.append(v)
    for w in D[v]:
        if w in active:
            return False
        elif w in new:
            if checkCycleDFS(D,w,new,active,finished) == False:
                return False
    active.remove(v)
    new.remove(v)
    finished.append(v)
    return True
