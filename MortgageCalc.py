import sys

L = float(sys.argv[1])
r = float(sys.argv[2])
c = r/12
n = float(sys.argv[3])

P = L*(c*(1+c)**n) / ((1+c)**n-1)
print("P = " + str(P))
