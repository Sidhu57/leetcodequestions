a = input("Enter letters: ")

c = {
    'Q': 1,
    'W': 2,
    'E': 30,
    'R': 500,
    'T': 1000
}

b = 0

for i in a:
    b += c[i]

print(b)
