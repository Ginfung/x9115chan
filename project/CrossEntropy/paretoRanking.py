import pdb

def dominate(list1, list2):
    N = len(list1)
    equal = True
    for i in range(N):
        if list1[i] > list2[i]: return False
        if equal and list1[i] != list2[i]: equal = False
    if not equal: return True
    else: return False

def paretoRank(WORK, eliteratio, n, m):
    # Elements in WORK list should be formatted as
    # [decs,objs,rank]
    # 0..n-1-> decs
    # n..n+m-1-> objs
    # n+m -> rank
    """
    N = len(WORK)
    for i in WORK:
        i[n+m] = 0 # initial rank is 0
    for j in range(n, n+m):
        WORK = sorted(WORK, key=lambda x:x[j])
        rp = 0
        ri = rp
        while ri < N-1:
            if WORK[rp][j+1] <= WORK[ri+1][j+1]:
                WORK[rp][n+m] += 1
            ri += 1
        rp += 1

    pdb.set_trace()
    # fetching the elites
    elite = [i for i in WORK if i[n+m] <= th]
    return elite
    """
    # Slow algorithm
    # TODO apply fast sort at NSGA-II algorithm
    N = len(WORK)
    for i in range(N):
        for j in range(i+1,N):
            if dominate(WORK[j][n:n+m], WORK[i][n:n+m]):
                WORK[i][n+m] += 1

    e = int(N*eliteratio)
    return sorted(WORK, key=lambda x:x[n+m])[:e]


#WORK = [[1,8,5,12,0],[2,7,7,14,0],[3,6,11,10,0],[4,3,8,9,0],[4,7,7,13,0]]
#paretoRank(WORK,2,1,3)
