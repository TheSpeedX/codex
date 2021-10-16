
#include <iostream>

using namespace std;

 int LCM(int n1, int n2) {
		int lcm = 0;
		for (int i = 1; i < n2; i++) {
			lcm = (n1 > i) ? n1 : i;
			 for (lcm = (n1 > i) ? n1 : i; lcm <= (n1*n2); lcm++)
			 {
				 if(lcm % n1 == 0 && lcm % i == 0)
				 {
				   n1 = lcm;
		           break;
			 }
				 lcm += 1;
		       }
		}  
	   return lcm;
	 }
	 
int main()
{
    int res=LCM(20,100);
    cout<<res;
//output will be 1163962800
    return 0;
}
