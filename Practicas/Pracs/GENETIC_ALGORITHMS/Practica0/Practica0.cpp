#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <ctime>
using namespace std;

void quickSort(int arr[], int izq, int der){
	
	int pivote = arr[(izq+der)/2];
	int aux, i = izq, j = der;
	
	while(i<=j){
		while(arr[i]<pivote) i++;
		while(arr[j]>pivote) j--;
		aux = arr[i];
		arr[i] = arr[j];
		arr[j] = aux;
		i++;
		j--;
	}
	
	if(izq<j)
		quickSort(arr, izq, j);
		if(i<der)
            quickSort(arr, i, der);	 	 
		
}

void Bin(int num){
	int * bin;
	bin = (int *)malloc(sizeof(int)*10);
	int j;
		
	for(int i=10;i>=0;i--){
           bin[i] = (j%2);
           j = j/2;
        }
	
	for(int i=0;i<10;i++)
		cout<<bin[i]<<" ";			 		  
	
}

int main(){
	
	int num, i = 0, j;
	int * arr;
	
	cout<<"\tOrdenamiento de Poblaciones de Acuerdo a su Informacion\n"<<endl;
	cout<<"Por favor ingresa el tamaño de la poblacion de datos a evaluar"<<endl;
	cin>>num;
	
	arr = (int *)malloc(sizeof(int)*num);
	
	srand(time(0));
	for(i=0;i<num;i++){	
		arr[i] = rand();
		cout<<arr[i]<<endl;
	}
	
	cout<<"A continuacion se ordenaran los datos de forma ascendente\n"<<endl;
	quickSort(arr, 0, num-1);
	
	for(i=0;i<num;i++){
		cout<<i<<arr[i]<<endl;
		Bin(arr[i]);
	}
}
