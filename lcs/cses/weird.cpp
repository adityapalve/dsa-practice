#include <iostream>
#include <unordered_map>
using namespace std;
/*
int findMissingNumber(int n, int arr[]){
  unordered_map<int, bool> num_map;

  for(int i=1; i<=n;i++){
    num_map[i] = true;
  }

  for(int i=0; i<n-1; i++){
    num_map[arr[i]] = false;
  }

  for(auto &pair : num_map){
    if(pair.second){
      return pair.first;
    }
  }

  return -1;
}
*/

int foo(int n, int arr[]){
  
}

int main(){
  int n;
  cin>> n ;

  int arr[n-1];
  
  for(int i=0; i<n-1; i++){
    cin >> arr[i];
  }

  int missing_number = findMissingNumber(n, arr);
  cout << "missing number:"<< missing_number << endl;

  return 0;
}
