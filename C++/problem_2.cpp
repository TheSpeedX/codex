#include <iostream>

using namespace std;

int main(){
    int limit = 4000000;
    int a = 1, b = 1, sum = 0,temp;
    while (b < limit){
        if (b % 2 == 0){
            sum = sum + b;
        }
        temp = a + b;
        a = b;
        b = temp;
    }
    cout << sum;
    return 0;
}