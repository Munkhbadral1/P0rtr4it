#include<fstream>
#include<iostream>
using namespace std;

int main(){
    fstream myFile;
    int counter1=0;
    myFile.open("2022.11.30-4.txt", ios::out);
    if(myFile.is_open()){
        for(int a=0; a<10; a++){
            for(int b=0; b<10; b++){
                for(int c=0; c<10; c++){
                    for(int d=0; d<10; d++){
                        myFile<<"<img width=\"60px\" src=\"https://eyesh.eec.mn/uploads/pupils/22300"<<a<<b<<c<<d<<".jpg\">"<<"\n";
                    }
                }
            }
        }
        myFile.close();
    }
    system("pause");
}