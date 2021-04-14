from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

p = int(input("enter a prime number: "))

def quadres(prime, num):
    result = pow(num, int((prime-1)/2), prime)
    if result == p-1:
        return 0
    if result == 1:
        return 1
    # if result == 0:
    #     return "neither (0)"

for i in range(1, p):
    if quadres(p, i) ==  1:
        print(str(i))

list = []
# res = [ pow(e, 2 ,p) for e in a_list if type(e) == types.IntType ]

for i in range(1, p):
    item = quadres(p, i)
    list.append(item)

# converting list to array
arr = np.array(list)

print(arr)

arr = np.expand_dims(arr, axis=0)  # or axis=1
plt.imshow(arr, cmap='Greys')
plt.show()
plt.savefig("residue"+ str(p) + ".png")

# x_data = (range(0, p))
# plt.scatter(x_data, list, c='r', label='data')
# # plt.plot(list)
# plt.show()
