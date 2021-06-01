#include <bits/stdc++.h>
using namespace std;

int main(){
	int n,i,j;
	cin>>n;

	for(int i=n;i>0;i--){
		for(int j=1;j<=i;j++){
			cout<<j<<" ";
		}
		for(int j=0;j<2*(n-i)-1;j++){
			cout<<"*";
			cout<<" ";
		}
		cout<<endl;
	}

	return 0;
}
