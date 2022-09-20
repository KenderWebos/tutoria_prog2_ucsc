# https://www.beecrowd.com.br/judge/es/problems/view/2060

def main():
    n = int(input())
    a = input().split()
    b = [0, 0, 0, 0]
    for i in range(n):
        if int(a[i]) % 2 == 0:
            b[0] += 1
        if int(a[i]) % 3 == 0:
            b[1] += 1
        if int(a[i]) % 4 == 0:
            b[2] += 1
        if int(a[i]) % 5 == 0:
            b[3] += 1
    print("{} Multiplo(s) de 2".format(b[0]))
    print("{} Multiplo(s) de 3".format(b[1]))
    print("{} Multiplo(s) de 4".format(b[2]))
    print("{} Multiplo(s) de 5".format(b[3]))

    input()

if __name__ == '__main__':
        main()    