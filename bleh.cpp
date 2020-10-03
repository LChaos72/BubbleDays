#include<bits/stdc++.h>
using namespace std;
int main()
{
  long n,q,a[100000],b[100000];

  cin>>n>>q;
  for(int i=0;i<n;i++)
  {
    cin>>a[i];
  }
  for(int i=0;i<q;i++)
  {
    cin>>b[0];
    if(b[0]==1)
    {
      cin>>b[1];
      int pos=b[1]-1;
      if(a[pos]==0)a[pos]=1;
      else a[pos]=0;
    }
    else
    {
      cin>>b[1]>>b[2];
      int pos=b[2]-1;
      if(a[pos]==1)cout<<"ODD"<<endl:
      else cout<<"EVEN"<<endl;
  }
  return 0;
}
