#include <bits/stdc++.h>
using namespace std;
int prime(int x, int &h)
{
    int flag = 1, d[400], f = 1;
    for (int i = 2; i < x; i++)
    {
        if (x % i == 0)
        {
            flag = 0;
            return 0;
        }
    }
    if (flag == 1)
    {
        d[h++] = x;
        int temp = x;
        for (int i = 0; i < h; i++)
        {
            if (temp == d[i])
            {
                f = 0;
                return 0;
                break;
            }
        }
    }
    if (f == 1)
        return 1;
}
int main()
{
    int t, n, a[400], b[400], c[400], k = 0, h, s;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int m = 0, r = 0;
        cin >> n;
        int x = 2, y = n - 2, v = 0;
        while (y >= n / 2)
        {
            int u = 1;
            for (int j = 2; j <= x; j++)
            {
                if (x % j == 0)
                {
                    x = x / j;
                    a[m++] = j;
                }
            }
            for (int j = 2; j <= y; j++)
            {
                if (y % j == 0)
                {
                    y = y / j;
                    b[r++] = j;
                }
            }
            h = 0;
            for (int j = 0; j < m; j++)
            {
                int l = prime(a[j], h);
                if (l == 0)
                {
                    u = 0;
                    break;
                }
            }
            if (u == 0)
            {
                x++;
                y--;
                continue;
            }
            s = 0;
            for (int j = 0; j < r; j++)
            {
                int g = prime(b[j], s);
                if (g == 0)
                {
                    u == 0;
                    break;
                }
            }
            x++;
            y--;
            if (h == 1 || s == 1)
            {
                v = 0;
            }
            else if (u == 1)
            {
                c[k++] = 1;
                v = 1;
                break;
            }
        }
        if (v == 0)
            c[k++] = 0;
    }
    for (int i = 0; i < k; i++)
    {
        if (c[k] == 0)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
}
