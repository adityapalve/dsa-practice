#include <iostream>

using namespace std;

void pointers(){
 int a = 10;
 int *p = &a;
 cout<< a << endl;
 cout<< *p << endl;
 cout<< &p << endl;
}

int main(){
  pointers();
  return 0;
}