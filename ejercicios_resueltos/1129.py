# https://www.beecrowd.com.br/judge/es/problems/view/1129

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            r = input().split()
            for j in range(5):
                if r[j] == 'N':
                    print(j+1)
                    break
    input()

if __name__ == '__main__':
        main()    