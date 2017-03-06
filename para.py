import math
from contextlib import redirect_stderr

import matplotlib.pyplot as plt
import os
# import matplotlib.pyplot as plt
from sympy import *
import numpy as np

#from para import allr2

Eps = np.array([0.577, 1, 1.732, 3.732, 11.43])
R2 = 288.3

R1 = 287
z1 = 1
z2 = 1
r1 = 1
k1 = 1.4
k2 = 1.33

# fc_min = 0.01
# fc_max = 1.1
# fc_d = 0.01
# fc = 0.27
# fc = 0.25
# fc = 0.213
# fc = 0.16
res_fcs = []
lst = []
m_fz = []

resr2 = []
Mzms = [0,1]
allM1 = []
allPiks = []
allr2 =[]

def run():

    '''нет rm '''
    res_fcs = []
    lst = []

    writeF()




def calc_part():

    # if self.wnd.radioButton.isChecked():
    #     epsi = Eps[0] #30
    # elif self.wnd.radioButton_2.isChecked():
    #     epsi = Eps[1] #45
    # elif self.wnd.radioButton_3.isChecked():
    #     epsi = Eps[2] #60
    # elif self.wnd.radioButton_4.isChecked():
    #     epsi = Eps[3] #75
    # elif self.wnd.radioButton_5.isChecked():
    #     epsi = Eps[4] #85

    # epsi = Eps[3] #75
    epsi = Eps[4]  # 75
    pi0_min = 1.1
    pi0_max = 4

    piks_min = 1.001
    piks_max = 1.121

    theta2_min = 1
    theta2_max = 2

    rm_min = 0.8
    rm_max = 0.95

    r2_min = 0.5
    r2_max = 0.8

    piks_d = 0.01

    pi0_d = 0.2

    theta2_d = 0.1

    r2_d = 0.001

    rm_d = 0.001

    r_d = 0.05

    #res_fcs = []




    # piks = piks_min
    # while piks <= piks_max:
    #
    #     r2 = r2_min
    #     rm0 = (1 + r2_min) / 2
    #     rm = rm0 + 0.001
    #     while r2 <= r2_max:
    #
    #         # r = r2
    #
    #
    #         '''theta2 = theta2_min'''
    #         theta2 = 1.01
    #         # while r <= 1:
    #         pi0 = pi0_min
    #         res = main_calc(piks, pi0, theta2, r2, epsi, rm)
    #         # pi0 = pi0_min
    #         # while pi0 <= pi0_max:
    #         #     res = main_calc(piks, pi0, theta2, r2, epsi, rm)
    #         #
    #         #
    #         #     pi0 += pi0_d
    #         #     # r += r_d
    #         rm += rm_d
    #
    #
    #         r2 += r2_d
    #
    #
    #
    #     piks += piks_d

    piks = piks_min
    # while piks <= piks_max:

    r2 = 0.5
    rm0 = (1 + r2) / 2
    rm = rm0 + 0.001
    # r = r2


    '''theta2 = theta2_min'''
    theta2 = 1.01
    # while r <= 1:
    pi0 = pi0_min
    res = main_calc(piks, pi0, theta2, r2, epsi, rm)
    # pi0 = pi0_min
    # while pi0 <= pi0_max:
    #     res = main_calc(piks, pi0, theta2, r2, epsi, rm)
    #
    #
    #     pi0 += pi0_d
    #     # r += r_d
    # rm += rm_d

    # r2 += r2_d

    # piks += piks_d



def comparefc( ):
    pass


def writeF():
    f = open('delta2r205fc01.txt', 'w')
    # f.write(str(m_fz))
    for item in lst:
        f.write(str(item) + '\n')

    f.close()

def main_calc(piks, pi0, theta2, r2, epsi, rm):
    ''' not finished '''

    r2 = round(r2, 3)
    rm = round(rm, 3)

    b = (-2 * rm) / ((1 - r2) * ((2 * rm) - r2 - 1))
    # b = (2 * rm) / ((r2 ** 2) - (2 * rm * r2) - 1 + 2 * rm)

    a = -1 * (b / (2 * rm))

    c = 1 - a - b

    # m = (np.log(r2 * ( R1 /  R2) * (1 / theta2))) / np.log (r2)
    # m = round(m, 3)

    m = 1.04
    #
    # M1 = np.sqrt(2 * (((piks ** (1 / ( k1 - 1) /  k1)) - 1) / ( k1 - 1)))
    allM1 = np.arange(0, 0.89, 0.01)

    # for i,M1 in enumerate(allM1):
    #     # for i in allM1:

    # M1 = allM1[i]
    M1 = 0.79
    # M1 = round(M1, 3)

    # M1 = 0.2
    # M1 = M1
    # M1 = 0.9

    A = (( k1 - 1) / (2 * m)) * ((M1 ** 2) / (1 + (1 / epsi ** 2)))

    mf1 = M1 / ((1 + (1 / (epsi ** 2))) ** 0.5)

    rmf1 = round(mf1, 3)

    mz1 = (((M1 ** 2) / (1 + epsi ** 2)) ** 0.5)
    rmz1 = round(mz1, 3)

    #  m_fz.append({'mf1 = ',rmf1, 'mz1 = ',rmz1})

    # Fi2 = 1 - A * ((1 / (r2 ** (2 * m))) - 1)
    #
    # gamma = (( k1 * ( k2 - 1) *  z1 *  R1) / (2 *  k2 *  z2 *  R2)) * \
    #         ((M1 ** 2) / ((1 + (1 / epsi ** 2)) * (r2 ** (2 * m)) * theta2 * Fi2) *
    #          (1 - ((1 / pi0) ** (( k2 - 1) /  k2))) * (
    #          1 / (Fi2 ** (( k1 * ( k2 - 1)) / ( k2 * ( k1 - 1))))))
    #
    # B = ( k1 * ( k2 - 1) * (M1 ** 2) *  z1 *  R1) / \
    #     (2 *  k2 * (1 + (1 / (epsi ** 2))) * (r2 ** (2 * m)) * theta2 * Fi2 *  z2 *  R2)

    # fiSt3 = (( 1 - ((0.2 * M1 ** 2) / (1 + (1/ (epsi ** 2))) * m) * (( 1 / ( r2 ** (2 * m) )) - 1) )**3)

    # fiSt3 = Fi2 ** 3
    #


    # _Mzm = a * (rm ** 2) + b * rm + c
    n = 0.05
    Mz1 = M1 / ((1 + epsi ** 2)** 0.5)
    Mzm = Mz1 + n * Mz1

    _Mzm = Mzm/Mz1

    #
    # _Mz = a * (r ** 2) + b * r + c

    # fc =  fc_min

    # funct = fiSt3 * _Mz * r
    #
    # dr = symbols('r')
    #
    # integr = integrate(funct, (dr, r2, 1))

    # res_fc = integr / (0.5 * M1)
    # res_fc = round(res_fc, 3)
    res_fc = 0.1
    res_fcs.append(res_fc)

    I1 = 1/4 * (1 - r2 ** 4)
    I2 = 1/3 * (1 - r2 ** 3)
    I3 = 1/2 * (1 - r2 ** 2)
    I4 = 1/(4 - 2 * m) * (1 - r2 ** ( 4 - 2 * m))
    I5 = 1/(3 - 2 * m) * (1 - r2 ** ( 3 - 2 * m))
    I6 = 1/(2 - 2 * m) * (1 - r2 ** ( 2 - 2 * m))
    I7 = 1/(2 - 4 * m) * (1 - r2 ** ( 2 - 4 * m))
    I8 = 1/(3 - 4 * m) * (1 - r2 ** ( 3 - 4 * m))
    I9 = 1/(4 - 4 * m) * (1 - r2 ** ( 4 - 4 * m)) #правка
    I10 = 1/(4 - 6 * m) * (1 - r2 ** ( 4 - 6 * m))
    I11 = 1/(3 - 6 * m) * (1 - r2 ** ( 3 - 6 * m))
    I12 = 1/(2 - 6 * m) * (1 - r2 ** ( 2 - 6 * m))

    f1 = (1 + 3 * A + 3 * A ** 2 + A ** 3) * (a * I1 + b * I2 + c * I3)
    f2 = (3 * A + 6 * A ** 2 + 3 * A ** 3) * (a * I4 + b * I5 + c * I6)
    f3 = (3 * A ** 2 + 3 * A ** 3) * (a * I7 + b * I8 + c * I9)
    f4 = A ** 3 * (a * I10 + b * I11 + c * I12)



    #  compare()

    # res_fc = round(res_fc, 3)
    # m = round(m, 3 )
    # M1 = round(M1, 3)

    # funct2 = fiSt3 * M1 * ((a * r ** 2 + b * r + c) / (1 + epsi ** 2)) * r

    # integ = integrate(funct2, (dr, r2, 1))

    delta2 = 0.5 * res_fc * (f1 - f2 + f3 - f4)
    delta2= round(delta2, 5)
    # print(m)
    # print(delta2)
    # print (rm , 'r2 = ',r2)

    r3 = delta2 + r1



    allr2.append(r2)
    allr2.append(rm)
    allr2.append(r3)

    Mzms.append(_Mzm)
    # lst.append({
    #     #     'Pikc': piks,
    #     'r2': r2,
    #     'M1': M1,
    #     'delta': delta2
    # })

    # if (delta2 >= 0) and (delta2 <= 0.001):
    #     print('delta = ', delta2)
    #     allr2.append (r2)
    #     lst.append({
    #     #     'Pikc': piks,
    #         'r2': r2,
    #         'M1': M1,
    #         'delta': delta2,
    #         '_Mzm': _Mzm
    #     })

    # allr2.append (r2)
    # lst.append({
    # #     'Pikc': piks,
    #     'r2': r2,
    #     'M1': M1,
    #     'delta': delta2,
    #     'fc': res_fc
    # })
    # allM1.append (M1)
    allPiks.append(piks)
    # allr2.append(r2)


    # lst.append({
    #     'Pikc': piks,
    #     'r2': r2,
    #     'rm': rm,
    #     'r': r,
    #     'res_fc': res_fc,
    #     'M1': M1,
    #     'm': m,
    #     'fi': 75,
    #     'mz1': rmz1,
    #     'mf1': rmf1
    # })


    # s_m1 = 'M1 = {};rmz1 = {};rmf1 = {}'.format(M1,rmz1,rmz1)
    # lst.append ({
    #     s_m1, rmz1, rmf1
    # })
    # if r_vnesh is not None:
    #     mf_vnesh = M1 /\
    #                ((1 + 1 / epsi ** 2) ** 0.5 * (1 - A * (1 / (r_vnesh ** (2 * m)) - 1)) ** 0.5 * r_vnesh ** (2 * m))
    #
    #
    #     return mf_vnesh
    #
    #
    #
    # if r_vnutr is not None:
    #     mf_vnutr = (1 / r2 ** m) * ((r_vnutr / r2) ** 2) * (((k1 * R1) / (k2 * R2)) ** 0.5) * \
    #                (M1 / (((1 + (1 / epsi ** 2)) ** 0.5) * ((1 - B * (1 - ((r_vnutr / r2) ** (2 * gamma)))) ** 0.5)))
    #     return mf_vnutr
    return (_Mzm)

def vis(allPiks, allM1):
    plt.plot(allPiks, allM1)
    plt.xlabel(r'$Piks$')  # Метка по оси x в формате TeX
    plt.ylabel(r'$M1$')  # Метка по оси y в формате TeX
    # plt.title(r'$y=x^2$')  # Заголовок в формате TeX
    plt.grid(True)  # Сетка
    plt.show()  # Показать график


def vis1(allr2, allM1):
    plt.plot(allM1, allr2)
    plt.xlabel(r'$M1$')  # Метка по оси x в формате TeX
    plt.ylabel(r'$r2$')  # Метка по оси y в формате TeX
    # plt.title(r'$y=x^2$')  # Заголовок в формате TeX
    plt.grid(True)  # Сетка
    plt.show()  # Показать график

def vis2(allr2, allPiks):
    plt.plot(allPiks, allr2)
    plt.xlabel(r'$Piks$')  # Метка по оси x в формате TeX
    plt.ylabel(r'$r2$')  # Метка по оси y в формате TeX
    # plt.title(r'$y=x^2$')  # Заголовок в формате TeX
    plt.grid(True)  # Сетка
    plt.show()  # Показать график

def vis3(allr2, Mzms):
    #print(allr2, Mzms)s,
    plt.plot(Mzms,allr2,"*")
    # plt.plot(allr2)
    # plt.contour(allr2)
    # plt.plot(allr2)
    # plt.plot(Mzms, 'r--')
    plt.xlabel(r'$Mzms$')  # Метка по оси x в формате TeX
    plt.ylabel(r'$r2$')  # Метка по оси y в формате TeX
    # plt.title(r'$y=x^2$')  # Заголовок в формате TeX
    plt.grid(True)  # Сетка
    plt.show()  # Показать график

if __name__ == '__main__':

    calc_part()
    # run()
    vis3(allr2, Mzms)
    # vis(allPiks, allM1)
    # vis1(allr2, allM1)
    # vis2(allr2, allPiks)