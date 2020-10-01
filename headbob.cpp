#include<bits/stdc++.h>
using namespace std;
int main()
{
  long t,n,b[10000];
  char a[10000];
  cin>>t;
  int k=0;
  for(int i=0;i<t;i++)
  {
    cin>>n;
    gets(a);
    int flag=1;
    for(int j=0;j<n;j++)
    {
      if(a[j]=='I') {flag=0;b[k++]=1;break;}
      else if(a[j]=='Y'){flag=0;b[k++]=0;break;}
      else continue;
    }
    if(flag==1)b[k++]=-1;
  }
  for(int i=0;i<k;i++)
  {
    if(b[i]==1)cout<<"INDIAN"<<endl;
    else if(b[i]==0)cout<<"NOT INDIAN"<<endl;
    else cout<<"NOT SURE"<<endl;
  }
  return 0;
}
