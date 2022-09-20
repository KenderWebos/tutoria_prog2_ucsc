#https://www.beecrowd.com.br/judge/es/problems/view/1179

def main():
    par = []
    impar = []
    for i in range(15):
        n = int(input())
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
        if len(par) == 5:
            for j in range(5):
                print("par[{}] = {}".format(j, par[j]))
            par = []
        if len(impar) == 5:
            for j in range(5):
                print("impar[{}] = {}".format(j, impar[j]))
            impar = []
    for i in range(len(impar)):
        print("impar[{}] = {}".format(i, impar[i]))
    for i in range(len(par)):
        print("par[{}] = {}".format(i, par[i]))

    input()    

if __name__ == '__main__':
        main()        