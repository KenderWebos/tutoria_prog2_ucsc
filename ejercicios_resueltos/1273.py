# https://www.beecrowd.com.br/judge/es/problems/view/1273

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        a = []
        for i in range(n):
            a.append(input())
        m = 0
        for i in range(n):
            if len(a[i]) > m:
                m = len(a[i])
        for i in range(n):
            print(a[i].rjust(m))
        print()

if __name__ == '__main__':
        main()        

        