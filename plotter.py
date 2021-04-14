import math
# import csv
import pandas as pd
import matplotlib.pyplot as plt

p = int(input("enter a prime number: "))


def quadres(prime, num):#uses Euler's Criterion to compute whether num is a quadratic residue modulo prime
    result = pow(num, int((prime-1)/2), prime)
    if result == 1:
        return 1
    if result == 0:
        return 0
    if result == -1:
        return -1

def elliptic(p,num):#y is in place of y^2
    y = (pow(num,3)+num)%p
    return y
res = []
# res = [ pow(e, 2 ,p) for e in a_list if type(e) == types.IntType ]

for i in range(0, p):#prints quadratic residues from 0 to p
    item = pow(i, 2 ,p)
    res.append(item)

# print(res)
# print(elliptic(7,0))
# print(quadres(7,0))
# res2 = { i : res[i] for i in range(0, len(res) ) }
# def get_key(val):
#     for key, value in res2.items():
#          if val == value:
#              return key
#
#
#
# for i in range(0, (p-1)):
#     if quadres(p, elliptic(p,i)) == 1:
#         if pow(i, 2 ,p) in res:
#             print(str(i)+ ","+str(get_key(i)))
#           # print(str(i)+ ","+str(p - res.index()))

# for i in range(0, (p-1)):
#     if quadres(p, elliptic(p,i)) == 1:
#       if pow(i, 2 ,p) in res:
#           print(str(i)+ ","+str(res.index(i)))
#           # print(str(i)+ ","+str(p - res.index()))
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):#not my code, not sure how it works.
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

list_1 = []
list_2 = []
list_3 = []
list_4 = []



item = pow(i, 2 ,p)
res.append(item)

# with open('data.csv', 'w', newline='') as f:
#     thewriter = csv.writer(f)

for i in range(0, p):
    if quadres(p, elliptic(p,i)) == 1 or quadres(p, elliptic(p,i)) == 0:#if elliptic function is a residue, tonelli finds root of elliptic function
        # print(str(i) + "," + str(tonelli(elliptic(p,i),p)))
        # print(str(i) + "," + str(p - tonelli(elliptic(p,i),p)))
        item1 = i
        list_1.append(item1)
        item2 = tonelli(elliptic(p,i),p)
        list_2.append(item2)
        item3 = i
        list_3.append(item3)
        item4 = p - tonelli(elliptic(p,i),p)#the function is symmetric, so we look at the additive inverse modulo p
        list_4.append(item4)
list_1.extend(list_3)
list_2.extend(list_4)

# dictionary of lists
dict = {'x': list_1, 'y': list_2}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv(str(p)+ 'data.csv')
df.plot(kind='scatter',x='x',y='y',color='blue')
plt.show()
# f.close()
