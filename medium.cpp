#include<bits/stdc++.h>
using namespace std;
int main()
{
  long t,a[100000],m=0,l=0,b[100000];
  char s1[100000],s2[100000];
  cin>>t;
  for(int i=0;i<t;i++)
  {
    cin>>s1>>s2;
    int k=0;
    int c=0;
    int flag1=0,flag2=0;
    int min_ans=INT_MAX;
    for(int j=0;s1[j]!='\0';j++)
    {
      for(int g=j;s1[g]!='\0';g++)
      {
      if(s1[j]==s2[k])
       { if(k==strlen(s2)-1){flag2=1;break;}
        if(k==0){flag1=1;k++;}
        else k++;

       }
      else if(flag1==1)c++;
      else continue;

      }
      if(c<min_ans){min_ans=c;}


}
if(flag2==1){a[m++]=1;b[l++]=min_ans;}
else a[m++]=0;


  }
  int w=0;
  for(int i=0;i<m;i++)
  {
    if(a[i]==1)cout<<"YES"<<" "<<b[w++]<<endl;
    else cout<<"NO"<<endl;
  }
  return 0;
}
