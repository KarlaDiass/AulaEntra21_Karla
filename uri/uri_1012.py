a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

area_triret = (a*c)/2
area_circ = 3.14159 * (c**2)
area_trap = c * (a+b)/2
area_quad = b**2
area_ret = a * b 

print(f'TRIANGULO: {area_triret:.3f}\nCIRCULO: {area_circ:.3f}\nTRAPEZIO: {area_trap:.3f}\nQUADRADO: {area_quad:.3f}\nRETANGULO: {area_ret:.3f}')