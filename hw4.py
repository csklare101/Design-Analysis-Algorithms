words = open('words.txt', 'r').read().split()

def is_word(w):
    return w in words

def find_split(s):
    split = []

    for i in range(len(s)-1,-1,-1):
        for j in range(len(s),i,-1):
            if is_word(s[i:j]) and s[i:j] not in split:
                split.append(s[i:j])
    return split

def d2(l):
    lsts = {}
    for i in range(len(l)-1,-1,-1):
            lsts[i] = 1+max([0]+[lsts[j] for j in range(i+1, len(l)) if l[j][0] == l[i][-1:]])
    return max(lsts.values())
##def shared_DNA(s,t):
##    counts = {}
##    strin = ''
##    count = 0
##    hicount = 0
##    for i in range(len(s)):
##        for j in range(len(t)):
##            if(s[i] == t[j]):
##                print(s[i])
##                strin += s[i]
##                count += 1
##            else:
##                if(strin != ''):
##                    counts[strin] = count
##                    if(hicount < count):
##                        hcount = count
##                strin = ''
##                count = 0
##    return hicount



def shared_DNA(s,t):
    #sd = {(-1,-1) : 0}
    c = 0
    sd = {}
##    for i in range(len(s)):
##        sd[(i,-1)] = i+1
##    for j in range(len(t)):
##        sd[(-1,j)] = j+1
##    print(sd)
    for i in range(len(s)):
        for j in range(len(t)):
            sd[c] = max(i,j+(1 if s[i] == t[j] else 0))
            c+=1
    return max(sd.values())
    
