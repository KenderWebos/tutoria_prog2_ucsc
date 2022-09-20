# https://www.beecrowd.com.br/judge/es/problems/view/1091

def main():
    while True:
        k = int(input())
        if k == 0:
            break
        n, m = map(int, input().split())
        for i in range(k):
            x, y = map(int, input().split())
            if x == n or y == m:
                print("divisa")
            elif x > n and y > m:
                print("NE")
            elif x < n and y > m:
                print("NO")
            elif x < n and y < m:
                print("SO")
            elif x > n and y < m:
                print("SE")
    input()

if __name__ == '__main__':
        main()
