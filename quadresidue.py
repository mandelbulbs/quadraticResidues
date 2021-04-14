p = int(input("enter a prime number: "))
a = int(input("enter another number smaller than p: "))

def quadres(prime, num):
    result = pow(num, int((prime-1)/2), prime)
    if result == p-1:
        print("-1")
    if result == 1:
        print("1")
    if result == 0:
        return 0

print(quadres(p, a))
