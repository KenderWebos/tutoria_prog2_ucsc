#include <iostream>
using namespace std;
#define MAX 100

int main(int argc, char const *argv[])
{
    //IDE (borrar en caso de no ser necesario)
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif

    int k, array[MAX];
    cin>>k; //Lectura de la cantidad de números a ingresar
    for (int i = 0; i < k; i++){
        cin>>array[i]; //Números ingresados
    }
    
    while (k!=0)
    {
        for (int a = 0; a < k; a++){
            for (int b = a+1; b < k; b++){
                for (int c = b+1; c < k; c++){
                    for (int d = c+1; d < k; d++){
                        for (int e = d+1; e < k; e++){
                            for (int f = e+1; f < k; f++){
                                cout<<array[a]<<' '<<array[b]<<' '<<array[c]<<' '<<array[d]<<' '<<array[e]<<' '<<array[f]<<endl; //Ordenamiento ascendente de todas las combinaciones posibles de los números ingresados
                            }
                        }
                    }
                }
            }
        }
        
        cin>>k; //Nueva lectura de cantidad de números dentro del ciclo
        for (int i = 0; i < k; i++){
            cin>>array[i]; //Nuevo ingreso de números dentro del ciclo
        }
        if(k!=0){ //Condicional para evitar error de formato (línea vacía extra al final) en el juez virtual.
            cout<<"\n";
        }
    }
    
    return 0;
}
