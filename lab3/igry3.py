import numpy as np
def parse(h, u_sol):
    hp = h.split()
    u_sol = u_sol.split()
    return hp, u_sol

def check_answer(U_, u_sol):
    if len(U_) != len(u_sol):
        # print(len(U_), len(u_sol))
        return False
    for i in range(len(u_sol)):
        if int(U_[i]) != int(u_sol[i]):
            return False
    return True

print("test")

def compute(h, u_sol, u_ravn, u_paro):
    h, u_sol = parse(h, u_sol)
    h=np.array(h,int)

    H=np.reshape(h,(12,3))
    p=np.zeros((12,1)).astype(int).astype(str)
    u1=np.hstack(([1]*6,[2]*6))
    u2=np.hstack(([1]*3,[2]*3))
    u2=np.hstack((u2,u2))
    u3=np.hstack(([1,2,3]*4))
    U=np.hstack((u1,u2,u3))
    U=np.reshape(U,(12,3))
    N=np.arange(1, 13, 1, dtype=int)
    N=np.reshape(N,(12,1))

    i=0
    while i < 12:
        if p[i] == '0' or p[i] =='p':
            j=i
            while j < 12:
                if p[j] == '0' or p[j] == 'p':
                    if (H[i]-H[j]).max() > 0 and (H[i]-H[j]).min() >= 0:
                        p[i]='p'
                        p[j]='no'
                    elif  (H[j]-H[i]).max() > 0 and (H[j]-H[i]).min() >= 0:
                        p[j]='p'
                        p[i]='no'
                        break
                j+= 1
        i+= 1
    p=np.where(p == '0', 'p', p)
    U1=np.empty((12,1))
    for i in range(6):
        U1[i] = 1 if H[i][0] >= H[i + 6][0] else -1
        U1[i+6] = -1 if H[i][0] > H[i + 6][0] else 1
    U2=np.empty((12,1))
    for i in range(3):
        U2[i] = 1 if H[i][1] >= H[i + 3][1] else -1
        U2[i+3]= -1 if H[i][1] > H[i + 3][1] else 1
    for i in range(6,9):
        U2[i] = 1 if H[i][1] >= H[i + 3][1] else -1
        U2[i+3]= -1 if H[i][1] > H[i + 3][1] else 1
    U3=np.empty((12,1))
    for i in range(0,12,3):
        U3[i] = 1 if H[i][2] >= H[i + 1][2] and H[i][2] >= H[i + 2][2] else -1
        U3[i+1]= 1 if H[i + 1][2] >= H[i][2] and H[i + 1][2] >= H[i + 2][2] else -1
        U3[i+2]= 1 if H[i + 2][2] >= H[i][2] and H[i + 2][2] >= H[i + 1][2] else -1

    U_=np.hstack((U1,U2,U3))
    # print('u',U_)
    # print(U_.reshape(-1))
    # print('usol', u_sol)

    print('Ситуации равновесия в чистых стратегиях:')
    eq=np.empty((12,1))
    j=0
    ravn = []
    for i in range(12):
        if (np.sum(U_[i])) == 3:
            eq[j]=N[i]
            # print(eq[j])
            ravn.append(int(eq[j]))
            j+=1
    if len(ravn) == 0:
        ravn.append(0)

    print(ravn)
    checkRavn = check_answer(u_ravn.split(), ravn)
    print('Парето-оптимальные ситуации:')
    paro = []
    for i in range(12):
        if p[i] == 'p':
            # print(N[i])
            paro.append(int(N[i]))
    print(paro)
    checkParo = check_answer(u_paro.split(), paro)
    print(np.hstack((N,U,H,U_,p)))
    # isTrue = check_answer(U_.ravel(order='F'), u_sol)
    isTrue = check_answer(U_.reshape(-1), u_sol)
    u_sol_formatted = str(np.hstack((N,np.reshape(h,(12,3)),np.reshape(u_sol,(12,3)))))
    u_sol_formatted = u_sol_formatted.replace('][','\n').replace(']','').replace('[','').replace("'",'')
    # print(u_sol_formatted)
    return isTrue, checkParo, checkRavn, u_sol_formatted