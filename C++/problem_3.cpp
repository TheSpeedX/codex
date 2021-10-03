#include <iostream>

using namespace std;

int main(){
    int bigNum = 600851475143;
    int factor = 2, lastFactor = 1;
    while(bigNum>1){
        if(bigNum%factor==0){
            lastFactor = factor;
            bigNum = bigNum / factor;
            while (bigNum % factor==0)
                bigNum = bigNum / factor;
        }
        factor = factor + 1;
    }
    cout << lastFactor;
    return 0;
}