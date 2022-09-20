# https://www.beecrowd.com.br/judge/es/problems/view/1240

def main():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        if len(a) < len(b):
            print("nao encaixa")
        else:
            if a[-len(b):] == b:
                print("encaixa")
            else:
                print("nao encaixa")

    input()

if __name__ == '__main__':
        main()    