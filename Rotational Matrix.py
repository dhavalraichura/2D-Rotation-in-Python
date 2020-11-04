from math import cos,sin
n = int(input("Enter the number of rows & columns for matrices:")) 
x = []
y = []
result = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(0)
    result.append(a)
def matinp():
    matrix=[]
    print("Enter the entries rowwise:") 
    for _ in range(n):
        a=[]
        for _ in range(n):
            a.append(float(input()))
        matrix.append(a)
    return(matrix)
x = matinp()
y = matinp()
def matmult(mat1 , mat2):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                result[a][b] += mat1[a][c] * mat2[c][b]
    return(result)
xy = matmult(x,y)
ang = float((3.142/180)*float(input("Enter Angle in Degrees: ")))
angcos = float(cos(ang))
angsin = float(sin(ang))
def transline():
    transformationMat = [[float(angcos) , float(-angsin)] , [float(angcos) , float(angsin)]]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                result[a][b] += transformationMat[a][c] * xy[c][b]
    return(result)
def transtri():
    transformationMat = [[1.0 , 0.0 , 0.0] , [0.0 , float(angcos) , -float(angsin)] , [0.0 , float(angcos) , float(angsin)]]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                result[a][b] += transformationMat[a][c] * xy[c][b]
    return(result)
if n == 2:
    print(transline())
elif n == 3:
    print(transtri())
else:
    print("Wrong Input")