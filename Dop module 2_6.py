def find_unigue_pairs(target):
    password = ''

    for a in range (1, target // 2 + 1):
        for b in range  (a + 1, target + 1 - a):
            if target % (a + b) ==0:
                password += str (a) + str(b)
    return password

for target in range (3,21):
    pairs = find_unigue_pairs(target)
    print(f" {target}: {pairs}")


