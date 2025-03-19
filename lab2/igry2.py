import numpy as np

def parse(A,qq,mul):
    a = np.array([[int(x.strip()) for x in line.split()] for line in A])
    q =[float(x.strip()) for x in qq.split()]
    mul = [float(x.strip()) for x in mul.split()]
    return a,q,mul

def compute(A,q,mul):
    A,q,mul = parse(A,q,mul)
    print(A,q,mul)
    m,u,l = mul[0],mul[1],mul[2]
    b=A.max(axis=0)
    r=b-A
    qa=A*q
    qr=r*q
    # Вальда
    W=(A.min(axis=1)).max()
    w=(A.min(axis=1)).argmax()
    resW=np.where(A.min(axis=1)==W)[0]
    print('W=',W,' A=',resW+1)
    #  Сэвиджа
    S=(r.max(axis=1)).min()
    s=(r.max(axis=1)).argmin()
    resS=np.where(r.max(axis=1)==S)[0]
    print('S=',S,' A=',resS+1)
    #  Гурвица
    H=(m*A.min(axis=1)+(1-m)*A.max(axis=1)).max()
    h=(m*A.min(axis=1)+(1-m)*A.max(axis=1)).argmax()
    resH=np.where(m*A.min(axis=1)+(1-m)*A.max(axis=1)==H)[0]
    print('H=',H,' A=',resH+1)
    # bies
    B=(qa.sum(axis=1)).max()
    resB=np.where(qa.sum(axis=1)==B)[0]
    print('B=',B,' A=',resB+1)
    # Лапласа
    qL=1/A.shape[1]
    L=(qL*(A.sum(axis=1))).max()
    resL=np.where(qL*(A.sum(axis=1))==L)[0]
    print('L=',L,' A=',resL+1)
    #Ходжеса-Лемана
    HL=(u*qa.sum(axis=1)+(1-u)*A.min(axis=1)).max()
    resHL=np.where((u*qa.sum(axis=1)+(1-u)*A.min(axis=1))==HL)[0]
    print('HL=',HL,' A=',resHL+1)
    # Гермейера
    MG=A-A.max()-1
    MG=MG*q #матрица Гермейера
    print(A,'\n',A.max(),'\n',A-A.max()-1,'\n','MG=\n',MG)
    G=(MG.min(axis=1)).max()
    resG=np.where(MG.min(axis=1)==G)[0]
    print('G=',G,' A=',resG+1)
    # Гермейера-Гурвица
    GH=((1-l)*MG.min(axis=1)+l*MG.max(axis=1)).max()
    resGH=np.where(((1-l)*MG.min(axis=1)+l*MG.max(axis=1))==GH)[0]
    print(GH)

    return W, S, H, B, L, HL, G, GH


def ml(A,q):
    b=A.max(axis=0)
    print('b=',b)
    r=b-A
    print('r=\n',r)
    qa=A*q
    print('qa=\n',qa)
    qr=r*q
    return b,r,qa