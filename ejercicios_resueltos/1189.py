# https://www.beecrowd.com.br/judge/es/problems/view/1189

def main():
    a = []
    for i in range(12):
        a.append([])
        for j in range(12):
            a[i].append(float(input()))
    op = input()
    s = 0
    c = 0
    for i in range(12):
        for j in range(12):
            if i < j:
                s += a[i][j]
                c += 1
    if op == 'S':
        print("{:.1f}".format(s))
    else:
        print("{:.1f}".format(s / c))

if __name__ == '__main__':
        main()        