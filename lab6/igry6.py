import numpy as np
from scipy.optimize import linprog


def min_char_fun(a, b, c, ab, ac, bc, abc):
    obj = [1, 1, 1]

    lhs_ineq = [[ -1, 0, 0],  # не меняем
              [ 0, -1, 0],
              [ 0, 0, -1],
              [ -1, -1, 0],
              [ -1, 0, -1],
              [ 0, -1, -1]]

    rhs_ineq = [ -a, -b, -c, #A, B, C
              -ab, -ac, -bc] #Ab, AC, BC

    bnd = [(0, float("inf")),
        (0, float("inf")),(0, float("inf"))]

    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
                method="highs")
    return opt.x, opt.fun

def print_points(unique_vertices):
    # --- Вывод координат вершин ---
    print("Вершины допустимой области:") # Выводим заголовок
    for x, y, z in unique_vertices:                # Перебираем все вершины
        x_rounded = round(x, 2)
        y_rounded = round(y, 2)
        z_rounded = round(z, 2)
        print(f"({x_rounded}, {y_rounded}, {z_rounded})") # Выводим координаты вершины


def center_of_gravity(unique_vertices):
    x1, x2, x3 = 0, 0, 0
    for x, y, z in unique_vertices:
        x1 += x
        x2 += y
        x3 += z
    x1 = round(float(x1/len(unique_vertices)),2)
    x2 = round(float(x2/len(unique_vertices)),2)
    x3 = round(float(x3/len(unique_vertices)),2)
    return x1, x2, x3

def comp_shepli(a,b,c, ab,ac,bc,abc):
    tret = 1/3
    shest = 1/6
    t1 = tret * a + shest * (ab - b) + shest * (ac - c) + tret * (abc - bc)
    t2 = tret * b + shest * (ab - a) + shest * (bc - c) + tret * (abc - ac)
    t3 = tret * c + shest * (ac - a) + shest * (bc - b) + tret * ( abc - ab)
    return round(float(t1),2), round(float(t2)), round(float(t3))

def find_points(a, b, c, ab, ac, bc, abc, ):
    abc_minus_bc = abc - bc 
    abc_minus_ac = abc - ac  
    abc_minus_c = abc - c    
    def line_x_plus_y_eq_ab(x):           # Линия x + y = ab  =>  y = ab - x
        return ab - x
    def line_x_plus_y_eq_abc_minus_c(x): # Линия x + y = abc - c  =>  y = abc - c - x
        return abc_minus_c - x


    def intersection_linear(m1, b1, m2, b2):
        """Находит точку пересечения двух линейных функций (y = mx + b).
        Если линии параллельны, возвращает None."""
        if m1 == m2:  # Параллельные линии не пересекаются
            return None
        x = (b2 - b1) / (m1 - m2)  # Вычисляем x координату точки пересечения
        y = m1 * x + b1          # Вычисляем y координату точки пересечения
        return x, y               # Возвращаем кортеж (x, y)

    def intersection_vertical(x_val, func):
        """Находит точку пересечения вертикальной линии (x = x_val) с функцией."""
        y = func(x_val)          # Вычисляем y координату точки пересечения
        return x_val, y           # Возвращаем кортеж (x, y)

    def intersection_horizontal(y_val, func):
        """Находит точку пересечения горизонтальной линии (y = y_val) с функцией."""
        # Решаем уравнение func(x) = y_val для x.
        # В нашем случае, func - это y = mx + b  =>  x = (y - b) / m
        if func == line_x_plus_y_eq_ab:      # Если функция - это линия x + y = ab
            x = ab - y_val               # Вычисляем x координату
        elif func == line_x_plus_y_eq_abc_minus_c: # Если функция - это линия x + y = abc - c
            x = abc_minus_c - y_val        # Вычисляем x координату
        else:
            return None  # Не должны сюда попадать

        return x, y_val              # Возвращаем кортеж (x, y)

    # --- Определение допустимой области решения ---
    # Функция is_within_bounds определяет, находится ли точка (x, y) внутри
    # допустимой области решения системы неравенств.
    def is_within_bounds(point):
        x, y = point  # Распаковываем координаты точки
        return (x >= a and          # x должен быть больше или равен a
                x <= abc_minus_bc and # x должен быть меньше или равен abc - bc
                y >= b and          # y должен быть больше или равен b
                y <= abc_minus_ac and # y должен быть меньше или равен abc - ac
                x + y >= ab and      # x + y должно быть больше или равно ab
                x + y <= abc_minus_c) # x + y должно быть меньше или равно abc - c


    # --- Поиск всех точек пересечения ---
    # Создаем пустой список для хранения всех точек пересечения
    intersections = []

    # 1. Пересечения вертикальных и горизонтальных линий
    # Добавляем координаты пересечения каждой вертикальной линии с каждой горизонтальной линией
    intersections.append((a, b))                # x = a и y = b
    intersections.append((a, abc_minus_ac))      # x = a и y = abc - ac
    intersections.append((abc_minus_bc, b))          # x = abc - bc и y = b
    intersections.append((abc_minus_bc, abc_minus_ac)) # x = abc - bc и y = abc - ac

    # 2. Пересечения диагональных линий с вертикальными и горизонтальными линиями
    # Добавляем координаты пересечения каждой диагональной линии с каждой вертикальной и горизонтальной линией
    # Диагональ с вертикальными
    intersections.append(intersection_vertical(a, line_x_plus_y_eq_ab))        # x = a и y = ab - x
    intersections.append(intersection_vertical(a, line_x_plus_y_eq_abc_minus_c))  # x = a и y = abc - c - x
    intersections.append(intersection_vertical(abc_minus_bc, line_x_plus_y_eq_ab))   # x = abc - bc и y = ab - x
    intersections.append(intersection_vertical(abc_minus_bc, line_x_plus_y_eq_abc_minus_c)) # x = abc - bc и y = abc - c - x

    # Диагональ с горизонтальными
    intersections.append(intersection_horizontal(b, line_x_plus_y_eq_ab))        # y = b и x + y = ab
    intersections.append(intersection_horizontal(b, line_x_plus_y_eq_abc_minus_c))  # y = b и x + y = abc - c
    intersections.append(intersection_horizontal(abc_minus_ac, line_x_plus_y_eq_ab))   # y = abc - ac и x + y = ab
    intersections.append(intersection_horizontal(abc_minus_ac, line_x_plus_y_eq_abc_minus_c)) # y = abc - ac и x + y = abc - c

    # 3. Пересечения двух диагональных линий
    # Линии параллельны, поэтому точки пересечения нет
    # Вычисляем параметры первой линии
    m1 = -1 # Угловой коэффициент line_x_plus_y_eq_ab (y = ab - x)
    b1 = ab  # Свободный член line_x_plus_y_eq_ab
    # Вычисляем параметры второй линии
    m2 = -1 # Угловой коэффициент line_x_plus_y_eq_abc_minus_c (y = abc_minus_c - x)
    b2 = abc_minus_c # Свободный член  line_x_plus_y_eq_abc_minus_c
    intersection = intersection_linear(m1,b1, m2, b2) # Вычисляем точку пересечения
    if intersection: # Если точка найдена
      intersections.append(intersection) # Добавляем в список точек

    # --- Фильтрация вершин внутри допустимой области ---
    # Создаем новый список, в котором будут только те точки пересечения,
    # которые находятся внутри допустимой области решения.
    vertices = [point for point in intersections if is_within_bounds(point)]

    # --- Удаление дубликатов ---
    # Используем множество для хранения уникальных вершин.
    unique_vertices = set()

    # Преобразуем вершины в кортежи (tuple), так как множества могут содержать только неизменяемые объекты.
    for x, y in vertices:
        unique_vertices.add((round(x, 2), round(y, 2), round(abc - x - y, 2)))

    # Преобразуем множество обратно в список кортежей
    unique_vertices = list(unique_vertices)

    return unique_vertices

def parse_task(task_s):
    task = np.array(task_s.strip().split(), dtype = float)
    # task = np.array([5,8,7,19,21,25,39], dtype = float)
    return task

def check_equal(ar1, ar_answer: str):
    ar_answer = sorted([float(x) for x in ar_answer.strip().split()])
    ar1 = sorted(ar1)
    if len(ar_answer) != len(ar1):
        return False
    for i, el in enumerate(ar1):
        if abs(el- ar_answer[i]) > 0.2:
            return False
    return True

def compute(task_cond):
    print(f"Условие: {task_cond}")
    a, b, c, ab, ac, bc, abc = task_cond

    optX, z = min_char_fun(a, b, c, ab, ac, bc, abc)
    print(f"x1, x2, x3 = {optX}")
    print(f"z* = {z}") 
    unique_vertices, cg, shepli  = 0,0,0
    zabc = False
    if z > abc:
        zabc = True
        shepli = comp_shepli(a,b,c, ab,ac,bc,abc)
        print("z > abc")
        print(f"Проверка: сумма координат вектора Шепли равна v(ABC)? \n{shepli[0]+shepli[1]+shepli[2]} = {abc}") #для меня, не на сайт (можно сделать внутреннюю проверку, без вывода)
        print(f"\nПопробуем увеличить v(ABC), пусть v(ABC) равняется минимальному значению характеристической функции максимальной коалиции, при котором ядро ещё существует")
        print(f"v(ABC) = {z}")
        abc = z

    unique_vertices = find_points(a, b, c, ab, ac, bc, abc) # в этой переменной хранятся точки
    cg = center_of_gravity(unique_vertices)
    shepli = comp_shepli(a,b,c, ab,ac,bc,abc)
    
    print_points(unique_vertices)
    print(f"Координаты центра тяжести: {cg}")
    print(f"Проверка: сумма координат центра тяжести равна v(ABC)? \n{cg[0]+cg[1]+cg[2]} = {abc}") #для меня, не на сайт (можно сделать внутреннюю проверку, без вывода)
    print('Вектор Шепли: (', round(float(shepli[0]),2), round(float(shepli[1]),2), round(float(shepli[2]),2), ')')
    print(f"Проверка: сумма координат вектора Шепли равна v(ABC)? \n{shepli[0]+shepli[1]+shepli[2]} = {abc}") #для меня, не на сайт (можно сделать внутреннюю проверку, без вывода)
    return z, unique_vertices, cg, shepli, zabc

def check_vert(unique_vertices, vert_stud):
    # vert_stud = "(8 16 12)(8 11 17)(10 16 10)(14 12 10)(14 11 11)"
    print("\n\ndebug")
    print(vert_stud)
    vert_stud = vert_stud[1:-1].replace(') (',')(').split(')(') 
    vert_stud = [[float(x) for x in line.split()] for line in vert_stud]
    vert_stud = sorted(vert_stud)

    vert = []
    for line in unique_vertices:
        vert.append([float(x) for x in line])
    vert = sorted(vert)
    
    print(vert)
    print(vert_stud)
    print("debug\n\n")
    for ind_x, line in enumerate(vert):
        for ind_y, item in enumerate(line):
            if abs(vert_stud[ind_x][ind_y] - item) > 0.5:
                return False
    return True


def check(task, z_stud, vert_stud, cg_stud, shepli_stud):
    check_answers = {
        'z' :False, 
        'vert': False, 
        'cg': False, 
        'shepli': False
    }

    task = parse_task(task)
    z, unique_vertices, cg, shepli, zabc = compute(task)

    check_answers['z'] = abs(z - float(z_stud)) < 0.1 
    if zabc and vert_stud in ('нет','-'):
        check_answers['vert'] = True
    else:
        check_answers['vert'] = check_vert(unique_vertices, vert_stud)
    if zabc and cg_stud in ('нет','-'):
        check_answers['cg'] = True
    else:
        check_answers['cg'] = check_equal(cg, cg_stud)
    check_answers['shepli'] = check_equal(shepli, shepli_stud)


    for key in check_answers.keys():
        check_answers[key] = 'Верно' if check_answers[key] else 'Не верно'   
    return check_answers

