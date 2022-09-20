# https://www.beecrowd.com.br/judge/es/problems/view/1043

# Lea 3 números del tipo punto flotante (A, B y C) y verifique si es posible realizar un triángulo con ellos. Si esto es posible, calcular el perímetro del triángulo y mostrar el siguiente mensaje:
# Perimetro = XX.X
# Si esto no es posible, calcular el área de un trapecio, cuyas bases son A, B y su altura es C, y mostrar el siguiente mensaje:
# Area = XX.X

def main():
    a, b, c = map(float, input().split())
    if a + b > c and a + c > b and b + c > a:
        print("Perimetro = {:.1f}".format(a + b + c))
    else:
        print("Area = {:.1f}".format(((a + b) * c) / 2))

    input()

if __name__ == '__main__':
        main()    
