import random
import string
alpha = list(string.ascii_letters)
print(alpha)
#alpha=[ 'A','B','C', 'D', 'E','F','G','H', I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y,z]
number=['1','2','3','4','5','6','7','8','9','0'] #number = list(range(10))
symbols=['!','@','#','%','^','&','*',]
print("Welcome to PyPassword Generator!")
no_letters=int(input("How many letters would you like in your password: "))
no_symbols=int(input("How many symbols do you want: "))
no_numbers=int(input("How many numbers doyou want: "))
password_list=[]
for char in range(1,no_letters+1):
    password_list.append(random.choice(alpha))
for char in range(1,no_symbols+1):
    password_list.append(random.choice(number))
for char in range(1,no_numbers +1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)


password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
                     
