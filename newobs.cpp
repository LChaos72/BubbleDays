#include<bits/stdc++.h>
using namespace std;
int main()
{
 long t;
 string s;
 cin>>t;

 for(int i=0;i<t;i++)
 {
  long a[26]={0};
  string b;
  cin>>s;
   for(int j=0;s[j]!='\0';j++)
   {
     int num=int(s[j])-65;
     a[num]++;

   }

  int flag=0,l=0;
   for(int j=0;j<26;j++)
   {
     if(a[j]==1){flag=1; b[l++]=char(j+65);}

   }

   if (flag==0){cout<<-1<<endl;continue;}
   else
   {
long pos[l];
   for(int j=0;j<l;j++)
   {
     pos[j]=s.find(b[j]);
   }

   cout<<*min_element(pos,pos+l)<<endl;
 }
 }
 return 0;
}
