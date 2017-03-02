funct2 = fiSt3 * rM1 * ((a * r ** 2 + b * r + c) / (1 + epsi ** 2)) * r

        integ = integrate(funct2, (dr, r2, 1))
