import numpy as np


class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


angles = [float(ang) for ang in input('Enter numbers: ').split()]
#angles_paradigm = [12.319, 15.103, 17.456, 19.536, 21.421, 24.784]
Q2_list = []
for i in angles:
    theta = (i / 2) * np.pi / 180
    x1 = np.sin(theta)
    x2 = x1 ** 2

    # set Q and Q squared
    Q = (4 * np.pi / 1.5406) * x1
    Q2 = Q ** 2
    Q2_list.append(Q2)
    # r is ratio

    # 0.7659702482122027(example), Q squared value of the first itteration as denominator for r formula
    r = Q2 / Q2_list[0]
    r2 = r * 2
    r3 = r * 3
    #r4 = r * 4
    print('Q2 =', Q**2)
    print("x2 =", x2)
    print('theta =', theta)
    print('Q =', Q)
    print('/'*40)
    print(colour.GREEN + 'RATIO.1__for angle of{} = {}'.format((i), int(r)) + colour.END)
    print(colour.PURPLE +
          'RATIO.2__for angle of {} = {}'.format((i), int(r2)) + colour.END)
    print(colour.RED + 'RATIO.3__for angle of {} = {}'.format((i), int(r3)) + colour.END)
    # print(r4) CAN ADD MORE RATIOS IF REQUIRED
    print('/'*40)
# 12.319 15.103 17.456 19.536 21.421 24.784 

