# https://www.beecrowd.com.br/judge/es/problems/view/1087

def main():
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        if x1 == x2 and y1 == y2:
            print(0)
        elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2): # abs() devuelve el valor absoluto
            print(1)
        else:
            print(2)
    input()

if __name__ == '__main__':
        main()    