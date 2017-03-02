import math
from contextlib import redirect_stderr


import os
# import matplotlib.pyplot as plt
from sympy import *
import numpy as np
from fractions import Fraction


class Calc:
	# Eps = np.array([Fraction(0.577), Fraction(1), Fraction(1.732), Fraction(3.732), Fraction(11.43)])
	Eps = np.array([0.577, 1, 1.732, 3.732, 11.43])
	R2 = 288.3

	R1 = 287
	z1 = 1
	z2 = 1

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

	@staticmethod
	def comparefc( ):
		pass

	# @staticmethod
	# def compare():
	# 	for item in Calc.lst:
	# 		if Calc.lst['res_fc']
		#res_fcs = Calc.res_fcs
		# i = 0
		# while i < len(res_fcs):
		# 	j = i + 1
		# 	while j < len(res_fcs):
		# 		if res_fcs[i] == res_fcs[j]: #and rm and r2
		# 			del res_fcs[j]
		# 		else:
		# 			j += 1
        #
		# 	i += 1
		# Calc.res_fcs = res_fcs
		# return Calc.res_fcs


		# return res_fcs


	@staticmethod
	def writeF():
		f = open('test_fcs75(5).txt', 'w')
		# f.write(str(Calc.m_fz))
		for item in Calc.lst:
			f.write(str(item) + '\n')

		f.close()

	@staticmethod
	def main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, epsi, rm, r):
		''' not finished '''





		r2 = round(r2, 3)
		rm = round(rm, 3)

		# b = (2 * rm) / ((1 - r2) * ((2 * rm) - r2 - 1))
		b = (2 * rm) / ((r2 ** 2) - (2 * rm * r2 ) + 1 + 2 * rm)

		a = -1 * (b / (2 * rm))


		c = 1 - a - b



		# m = (np.log(r2 * (Calc.R1 / Calc.R2) * (1 / theta2))) / np.log (r2)
		# r_m = round(m, 3)

		r_m = 1

		M1 = np.sqrt(2 * (((piks ** (1 / (Calc.k1 - 1) / Calc.k1)) - 1) / (Calc.k1 - 1)))
		rM1 = round(M1, 3)

		A = ((Calc.k1 - 1) / (2 * r_m)) * (rM1 ** 2) / (1 + (1 / epsi ** 2))

		mf1 = rM1 / ((1 + (1 / (epsi ** 2))) ** 0.5)

		rmf1 = round(mf1, 3)

		mz1 = (((rM1 ** 2) / (1 + epsi ** 2)) ** (1 / 2))
		rmz1 = round(mz1, 3)

		# Calc.m_fz.append({'mf1 = ',rmf1, 'mz1 = ',rmz1})

		Fi2 = 1 - A * ((1 / (r2 ** 2 * r_m)) - 1)

		gamma = ((Calc.k1 * (Calc.k2 - 1) * Calc.z1 * Calc.R1) / (2 * Calc.k2 * Calc.z2 * Calc.R2)) * \
				((rM1 ** 2) / ((1 + (1 / epsi ** 2)) * (r2 ** (2 * r_m)) * theta2 * Fi2) *
				 (1 - ((1 / pi0) ** ((Calc.k2 - 1) / Calc.k2))) * (1 / (Fi2 ** ((Calc.k1 * (Calc.k2 - 1)) / (Calc.k2 * (Calc.k1 - 1))))))

		B = (Calc.k1 * (Calc.k2 - 1) * (rM1 ** 2) * Calc.z1 * Calc.R1) / \
			(2 * Calc.k2 * (1 + (1 / (epsi ** 2))) * (r2 ** (2 * r_m)) * theta2 * Fi2 * Calc.z2 * Calc.R2)

		# fiSt3 = (( 1 - ((0.2 * rM1 ** 2) / (1 + (1/ (epsi ** 2))) * r_m) * (( 1 / ( r2 ** (2 * r_m) )) - 1) )**3)

		fiSt3 = Fi2 ** 3

		_Mzm = a * ( rm ** 2 ) + b * rm + c

		_Mz = a * (r ** 2) + b * r + c

		# fc = Calc.fc_min

		funct = fiSt3 * _Mz * r

		dr = symbols ('r')

		integr = integrate(funct, (dr, r2, 1))

		# res_fc = integr / (0.5 * rM1)
		# res_fc = round(res_fc, 3)
		res_fc = 0.1
		Calc.res_fcs.append(res_fc)

		# Calc.compare()

		# res_fc = round(res_fc, 3)
		# m = round(m, 3 )
		# rM1 = round(rM1, 3)

		funct2 = fiSt3 * rM1 * ((a * r **2 + b * r + c )/ (1 + epsi ** 2))  * r

		integ = integrate(funct2, (dr, r2, 1))

		delta = 0.5 * res_fc - integ

		if (delta >= 0) and (delta <= 0.1):
			print (delta)


		# m = 0
		# while m <= len(Calc.res_fcs):

		# while Calc.fc <= 0.16:
		# if res_fc == Calc.fc:
		Calc.lst.append({
			'Pikc': piks,
			'r2': r2,
			'rm': rm,
			'res_fc': res_fc,
			'M1': rM1,
			'm': r_m,
			'fi': 75,
			'mz1': rmz1,
			'mf1': rmf1

		})
		# print (str(Calc.lst))

			# else: Calc.fc += 0.01
		# print (Calc.lst)
		# Calc.writing(r2, rm)

		# Calc.lst.append({
		# 	'r2': r2,
		# 	'rm': rm,
		# 	'res_fc': Calc.res_fcs
		# })


		# while fc <= Calc.fc_max:
		# 	if fc == res_fc:
		# 		print('r2 = ', r2 , 'rm = '	, rm)
		# 		print('res = ', res_fc)
        #
		# 		return fc
        #
		# 	else:
		# 		fc += Calc.fc_d
		# 	return fc


		if r_vnesh is not None:
			mf_vnesh = rM1 /\
					   ((1 + 1 / epsi ** 2) ** 0.5 * (1 - A * (1 / (r_vnesh ** (2 * r_m)) - 1)) ** 0.5 * r_vnesh ** (2 * r_m))



			# f = FiSt3 * _Mz * r
            #
			# integr = integrate(f, (r, r2, 1))
            #
			# Fc = integr / (0.5 * (((epsi ** 2) + 1) ** 0.5))



			# print(Fc)



			return mf_vnesh



		if r_vnutr is not None:
			mf_vnutr = (1 / r2 ** r_m) * ((r_vnutr / r2) ** 2) * (((Calc.k1 * Calc.R1) / (Calc.k2 * Calc.R2)) ** 0.5) * \
					   (rM1 / (((1 + (1 / epsi ** 2)) ** 0.5) * ((1 - B * (1 - ((r_vnutr / r2) ** (2 * gamma)))) ** 0.5)))
			return mf_vnutr






	# @staticmethod
	# def writing(r2,rm):
	# 	m = 0
	# 	while m < len(Calc.res_fcs):
	# 		Calc.lst.append({
	# 			'r2': r2,
	# 			'rm': rm,
	# 			'res_fc': Calc.res_fcs[m]
	# 		})
	# 		m += 1
	# 	print(Calc.lst)


		# @staticmethod
	# def visualFc():


	# @staticmethod
	# def compare():
	# 	res_fcs = Calc.res_fcs
	# 	i = 0
	# 	j = 1
	# 	while i < len(res_fcs):
	# 		if res_fcs[i] == res_fcs[j]:
	# 			del res_fcs[j]
	# 		elif j < len(res_fcs):
	# 			j += 1
	# 		else:
	# 			i += 1
    #
    #
	# 	print(Calc.lst)




	# @staticmethod
	# def compare_2():
	# 	fcs = []
	# 	res_fcs = Calc.res_fcs
	# 	i = 0
	# 	j = 0
	# 	while i < len(res_fcs):
	# 		if (res_fcs [i] - res_fcs[i+1]) < 0.0000005 and (res_fcs [i] - res_fcs[i+1]) > -0.0000005:
    #
	# 			if res_fcs[i] == fcs [j]:
	# 				i += 1
	# 				j += 1
    #
	# 			else:
	# 				res_fcs[i] = fcs[j]
	# 				i += 1
	# 				j += 1
    #







		# plt.plot(Calc.lst, r2)
		# plt.xlabel(r'$Fc$')  # Метка по оси x в формате TeX
		# plt.ylabel(r'$r2$')  # Метка по оси y в формате TeX
		# # plt.title(r'$y=x^2$')  # Заголовок в формате TeX
		# plt.grid(True)  # Сетка
		# plt.show()  # Показать график

