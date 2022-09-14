from itertools import permutations 
words = open('words.txt','r').read().split()
def is_word(w):
    return w in words

def all_segments(s):
    split = all_segments_r(s,0)
    if split != []:
        print(split)


def all_segments_r(s,i):
    segments = []
    if i == len(s):
        return [] #return origianl word
    for j in range(i+1,len(s)+1):
        if is_word(s[i:j]):
            split = all_segments_r(s,j)
            #print(split)
            if split != None:
                segments.append(s[i:j])
                segments += split                              
    return segments

def countct_seg_r(s,i):
    count = 0;
    if i == len(s):
        return 1;
    for j in range(i+1, len(s)+1):
        if is_word(s[i:j]):
            split = countct_seg_r(s, j)
            if split > 0:
                count += 1  
    return count

#from week3 python file
def segment(s):
    'segment s into words'

    split = segment_r(s, 0)
    if split != None:
        print(' '.join(split))

def segment_r(s, i):
    'segment s[i:] into words'

    if i == len(s):
        return [] #empty word
    for j in range(i+1, len(s)+1):
        if is_word(s[i:j]):
            split = segment_r(s, j)
            if split != None:
                return [s[i:j]] + split
    return
#from week3 python file


#able to get down to #5 on hw3 DNA
def bf_seq(p):
    per = permutations(p)
    for perm in per:
        test = True
        for i in range(1,len(perm)):
            if not(perm[i-1][-2:] == perm[i][:2]):
                test = False
        if(test == True):
            return perm

#able to get to #2 on hw3 DNA
def seq(p):
    w = p[:1]
    w2 = w[0]
    return seq_r(p[1:],w2)

##def seq_r(p,w):
##    if(p[0] == w):
##        return p
##    for i in p:
##        for j in range(1,len(i)):
##            test = True
##            if not(p[j-1][-2:] == p[j][:2]):
##                test = False
##                p = p[:j]+p[j+1:]
##                seq_r(p)
##            if test:
##                return
##    return p

def seq_r(p,w):
    #print('p[0]: {}'.format(p[0]))
    #print('w: {}'.format(w))
    lst = []
    for i in p:
        test = True
        if not(w[-2:] == i[:2]):
            test = False
        if test:           
            lst.append(w)
            #print('lst: {}'.format(lst))
            #print('p: {}'.format(p))
            se = seq_r(p[1:],i)
            if se != None or se != []:
                lst.append(se)
        else:
            lst = []
            return
    return lst

def find_seq(p):
    w = p[:1]
    w2 = w[0]
    return find_seq_r(p[1:],w2)

def find_seq_r(p,w):
        #print('p[0]: {}'.format(p[0]))
    #print('w: {}'.format(w))
    lst = []
    for i in p:
        test = True
        if not(w[-2:] == i[:2]):
            test = False
        if test:           
            lst.append(w)
            #print('lst: {}'.format(lst))
            #print('p: {}'.format(p))
            se = seq_r(p[1:],i)
            if se != None or se != []:
                lst.append(se)
        else:
            return test
    return lst
