def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant
coefficient=[]
constant=[]
res=[]
N=int(input())
for i in range(N):
    lst=list(map(int,input().split()))
    coefficient.append(lst[:N])
    constant.append(lst[-1])
determinant=getMatrixDeternminant(coefficient)
for i in range(N):
    dc = [row[:] for row in coefficient]
    for j in range(N):
        dc[j][i]=constant[j]
    tmp_det=getMatrixDeternminant(dc)
    res.append(int(tmp_det/determinant))
print(*res)
