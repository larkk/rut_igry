import numpy as np
from scipy.optimize import linprog


def parse_task(task_s):
    task = np.array(task_s.strip().split(), dtype = float)
    # task = np.array([5,8,7,19,21,25,39], dtype = float)
    return task

def check_z(task_cond):
    obj = [1, 1, 1]

    lhs_ineq = [[ -1, 0, 0],  # не меняем
                [ 0, -1, 0],
                [ 0, 0, -1],
                [ -1, -1, 0],
                [ -1, 0, -1],
                [ 0, -1, -1]]

    rhs_ineq = [ -task_cond[0], -task_cond[1], -task_cond[2], #A, B, C
                -task_cond[3], -task_cond[4], -task_cond[5]] #Ab, AC, BC

    bnd = [(0, float("inf")),
        (0, float("inf")),(0, float("inf"))]

    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
                method="highs")

    print(opt.x)
    print(opt.fun)
    return opt.fun

def comp_shepli(task):
    a,b,c, ab,ac,bc,abc = task
    tret = 1/3
    shest = 1/6
    t1 = tret * a + shest * (ab - b) + shest * (ac - c) + tret * (abc - bc)
    t2 = tret * b + shest * (ab - a) + shest * (bc - c) + tret * (abc - ac)
    t3 = tret * c + shest * (ac - a) + shest * (bc - b) + tret * ( abc - ab)
    print('shepli: (', t1, t2, t3, ')')
    return t1, t2, t3

def check_equal(ar1, ar_answer):
    ar_answer = sorted([float(x) for x in ar_answer.strip().split()])
    ar1 = sorted(ar1)
    if len(ar_answer) != len(ar1):
        return False
    for i, el in enumerate(ar1):
        if abs(el- ar_answer[i]) > 0.2:
            return False
    return True

def check(task, z, koor, weight, shepli):
    check_answers = {
        'z' :False, 
        'koor': False, 
        'weight': False, 
        'shepli': False
    }

    task = parse_task(task)
    check_answers['z'] = abs(check_z(task) - float(z)) < 0.1 
    # check_answers['koor'] = check_koor(task) == koor
    # check_answers['weight'] = check_weight(task) == weight
    check_answers['shepli'] = check_equal(comp_shepli(task), shepli)

    #3


    for key in check_answers.keys():
        check_answers[key] = 'Верно' if check_answers[key] else 'Не верно'   
    return check_answers
