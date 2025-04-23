from sympy import *
import numpy as np

def parse(a,b):
    print('____')
    print(a)
    print('_____')
    a_parsed = np.array([int(x.strip()) for x in a.split()])
    b_parsed = np.array([int(x.strip()) for x in b.split()])
    if len(a_parsed) != 4 or len(b_parsed) != 4:
        return False, False, True
    print('___________')
    print(a_parsed)
    print(b_parsed)
    print('___________')
    a = np.array(a_parsed)
    b = np.array(b_parsed)
    A=np.reshape(a,(2,2))
    B=np.reshape(b,(2,2))
    return A,B, False

# A=np.array([7,2,4,6])
# B=np.array([2,3,5,4])

# A=np.reshape(A,(2,2))
# B=np.reshape(B,(2,2))
def check5(a,b):
    A, B, err = parse(a,b)
    if err:
        return ('Не правильно', '')
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
    part2 = '\nM1 =%s M2=%s' % (M1, M2)
    return s, part2