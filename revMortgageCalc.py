import sys

P = float(sys.argv[1])
r = float(sys.argv[2])
c = r/12
n = float(sys.argv[3])

L = P*((1+c)**n-1) / (c*(1+c)**n)
print("L = " + str(L))
