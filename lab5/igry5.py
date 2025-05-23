from sympy import *
import numpy as np

def parse(a,b,c):
    print('____')
    print(a)
    print('_____')
    a_parsed = np.array([int(x.strip()) for x in a.split()])
    b_parsed = np.array([int(x.strip()) for x in b.split()])
    c_parsed = [x.strip() for x in c.split()]
    print('___________')
    print(a_parsed)
    print(b_parsed)
    print('___________')
    a = np.array(a_parsed)
    b = np.array(b_parsed)
    A=np.reshape(a,(2,2))
    B=np.reshape(b,(2,2))
    return A,B,c_parsed

# A=np.array([7,2,4,6])
# B=np.array([2,3,5,4])

# A=np.reshape(A,(2,2))
# B=np.reshape(B,(2,2))
def check5(a,b,c):
    A, B, C = parse(a,b,c)
    p11,p21,p12,p22= symbols('p11,p21,p12,p22')

    p11=Integer(B[1,1]-B[1,0])/Integer(B[0,0]+B[1,1]-B[0,1]-B[1,0])
    p21=1-p11
    p12=Integer(A[1,1]-A[0,1])/Integer(A[0,0]+A[1,1]-A[0,1]-A[1,0])
    p22=1-p12

    s=Matrix([[p11,p12],[p21,p22]])
    print('s =\n')
    pprint(s)

    M1=A[0,0]*p11*p12+A[0,1]*p11*p22+A[1,0]*p21*p12+A[1,1]*p21*p22
    M2=B[0,0]*p11*p12+B[0,1]*p11*p22+B[1,0]*p21*p12+B[1,1]*p21*p22

    print('\nM1 =',M1,'  M2 =',M2)
    if len(C) !=2:
        print(C)
        return 'Что то не так с вводом ответа'
    if C[0] != str(M1):
        return 'Не правильно'
    if C[1] != str(M2):
        return 'Не правильно'
    return 'Правильно'