a = list(range(3, 18, 2))
b = list(range(2, 17, 2))

for odd in a:
    for even in b:
        print(f"{odd} ===> {even}")
    print("============")
