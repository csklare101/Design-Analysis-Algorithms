import random
def c_hanoi(n):
    c_hanoiH(n,0,2)

def c_hanoiH(n,a,b):
    count = 0
    if n == 0:
        return count
    c = 3-a-b
    if b == (a+1) % 3:
        count += c_hanoiH(n-1,a,c)
        print('Move disk from {} to {}'.format(a,b))
        count += 1
        count += c_hanoiH(n-1,c,b)
    else:
        count += c_hanoiH(n-1,a,b)
        print('Move disk from {} to {}'.format(a,c))
        count += 1
        count += c_hanoiH(n-1,b,a)
        print('Move disk from {} to {}'.format(c,b))
        count += 1
        count += c_hanoiH(n-1,a,b)
    return count

def invert(lst):
    return inversions(lst)[1]
def inversions(lst):
    if len(lst) <= 1:
        return lst, 0
    mid = len(lst)//2
    L, l = inversions(lst[:mid])
    R, r = inversions(lst[mid:])
    

    i, j = 0, 0
    out = []
    count = 0 + l + r;
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            out.append(L[i])
            i += 1
        else:
            out.append(R[j])
            j += 1
            count+= (len(L)-i)
    if i == len(L):
        out += R[j:]
    else: 
        out += L[i:]
    #print(count)
    return out, count
    
def merge(L, R):
    'merge two sorted lists L and R into one sorted list'
    
    i, j = 0, 0
    out = []
    count = 0;
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            out.append(L[i])
            i += 1
        else:
            out.append(R[j])
            j += 1
            count+= (len(L)-i)
    if i == len(L):
        out += R[j:]
    else: 
        out += L[i:]
    print(count)
    return out

def mergesort(lst):
    'mergesort lst'

    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    L = mergesort(lst[:mid])
    R = mergesort(lst[mid:])
    return merge(L,R)


