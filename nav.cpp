#include <bits/stdc++.h>
using namespace std;
void funcC(long long x, long long &a[100000], long long n)
{
    long r = 0;
    long temp = a[0];
    int m = 0;
    for (int i = 0;; i++)
    {
        a[r] = a[r + 1];
        r++;
        if (r == n - 1)
        {
            a[n - 1] = temp;
            temp = a[0];
            r = 0;
            m++;
        }
        if (m == x)
            break;
    }
}
void funcA(long long x, long long &a[100000], long long n)
{

    long r = n - 1;
    long temp = a[n - 1];
    int m = 0;
    for (int i = 0;; i++)
    {
        a[r] = a[r - 1];
        r--;
        if (r == 0)
        {
            a[0] = temp;
            temp = a[n - 1];
            r = n - 1;
            m++;
        }
        if (m == x)
            break;
    }
}
long long funcR(long long x, long long &a[100000], long long n)
{
    long r = 0;
    for (int i = 0; i < x; i++)
    {
        r++;
        if (r == n - 1)
            r = 0;
    }
    return a[r];
}

int main()
{
    long long int n, q, a[100000], r, b[100000], x;
    char ch;
    cin >> n >> q;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    long k = 0;
    for (int i = 0; i < q; i++)
    {
        cin >> ch >> x;
        if (ch == 'C')
            funcC(x, a, n);
        else if (ch == 'A')
            funcA(x, a, n);
        else
            b[k++] = funcR(x, a, n);
    }
    for (int i = 0; i < k; i++)
    {
        cout << b[i] << endl;
    }
}
