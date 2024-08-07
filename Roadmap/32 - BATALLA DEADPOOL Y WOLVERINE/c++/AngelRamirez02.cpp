//Angel Ramirez Castro
#include <iostream>
#include <stdlib.h>
#include <thread>  
#include <chrono>  

using namespace std;

//clase para personajes
class personaje{
	public:
		int vida; //valor de vida
		int ataque, prob_evadir; //valor de ataque y prob de evadir el siguiente ataque
};

int main(){
	//creacion de personajes
	personaje DeadPool, Wolwerine;
	cout<<"\tSimulador de batalla\n\n";
	//Ingreso de la vida de los usuarios
	cout<<"Ingrese la vida de Deadpool: ";
	cin>>DeadPool.vida;
	cout<<"Ingrese la vida de Wolwerine: ";
	cin>>Wolwerine.vida;
	//Inicio de turnos, true para deadpol, false para wolwerine
	bool DeadPoolTurno=true;
	int turno=1;

	while( Wolwerine.vida>0 && DeadPool.vida>0){
		system("cls");
		cout<<"\n\tSimulador de batalla\n";
		if(DeadPoolTurno){
			//Genera el valor del ataque de deadpool y la prob de evadir de wolwerine
			DeadPool.ataque=rand()%91+10;
			Wolwerine.prob_evadir=rand()%101;
			
			if(Wolwerine.prob_evadir<20){ //si la probabilidad es 20%
				cout<<"Wolwerine logra evadir el ataque!\n";
			}
			else if(DeadPool.ataque==110){//ssuper ataque
				cout<<"Deadpool conecta un super ataque de "<<DeadPool.ataque<<endl;
				cout<<"Wolwerine no puede atacar en el siguiente turno\n";
				Wolwerine.vida-=DeadPool.ataque;//wolwerine pierde vida
				DeadPoolTurno=true;
			}
			else{ //ataque normal
				cout<<"Deadpool logra un ataque de "<<DeadPool.ataque<<endl;
				Wolwerine.vida-=DeadPool.ataque;//wolwerine pierde vida
				DeadPoolTurno=false;
			}
			//Imprime resultados
			cout<<"\n\t\tTurno: "<<turno<<endl;
			cout<<"\t\tD   VS   W\n";
			cout<<"\t       "<<DeadPool.vida<<"       "<<Wolwerine.vida<<endl;
			this_thread::sleep_for(chrono::seconds(1));
		}
		else{
			//Genera el valor del ataque de wolwerine y la prob de evadir de deadpool
			Wolwerine.ataque=rand()%111+10;
			DeadPool.prob_evadir=rand()%101;
			
			if(DeadPool.prob_evadir<25){//probabilidad de 25%
				cout<<"Deadpool logra evadir el ataque!\n";	
			}
			else if(Wolwerine.ataque==120){//super ataque
				cout<<"Wolwerine conecta un super ataque de "<<Wolwerine.ataque<<endl;
				cout<<"Deadpool no puede atacar en el siguiente turno\n";
				DeadPool.vida-=Wolwerine.ataque;//Deadpool pierde vida
				DeadPoolTurno=false;	
			}
			else{//ataque normal
				cout<<"Wolwerine logra un ataque de "<<Wolwerine.ataque<<endl;
				DeadPool.vida-=Wolwerine.ataque;//Deadpool pierde vida
				DeadPoolTurno=true;	
			}
			//Imprime resultados
			cout<<"\n\t\tTurno: "<<turno<<endl;
			cout<<"\t\tD   VS   W\n";
			cout<<"\t       "<<DeadPool.vida<<"       "<<Wolwerine.vida<<endl;
			this_thread::sleep_for(chrono::seconds(1));
		}
		turno++;//aumenta el numero de turno	
	}
	//muestra ganador
	if(DeadPool.vida>Wolwerine.vida){
		cout<<"\n\tDeadpool es el ganador!\n";
	}else{
		cout<<"\n\tWolwerine es el ganador!\n";	
	}
		
	return 0;
}
