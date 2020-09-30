#include <bits/stdc++.h>
using namespace std;
int pnd(long f1, long f2)
{
    int z1 = 1, z2 = 1;
    if (f1 == f2)
        return 0;
    else
    {
        for (int s = 2; s < f1; s++)
        {
            if (f1 % s == 0)
            {
                z1 = 0;
                break;
            }
        }
        for (int s = 2; s < f2; s++)
        {
            if (f2 % s == 0)
            {
                z2 = 0;
                break;
            }
        }
        if ((z1 == 1) && (z2 == 1))
            return 1;
        else
            return 0;
    }
}
int main()
{
    long t, n, k = 0, c[4000];
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        long x = 2, y = n - 2;
        int u = 0;
        while (y >= n / 2)
        {
            int l1 = 0, l2 = 0, q1, q2;
            for (int j = 2; j < x; j++)
            {
                if (x % j == 0)
                {
                    q1 = x / j;
                    if (q1 == 1)
                        break;

                    else
                        l1 = pnd(j, q1);
                }
                if (l1 == 1)
                    break;
            }
            for (int j = 2; j < y; j++)
            {
                if (y % j == 0)
                {
                    q2 = y / j;
                    if (q2 == 1)
                        break;
                    else
                        l2 = pnd(j, q2);
                }
                if (l2 == 1)
                    break;
            }
            if ((l1 == 1) && (l2 == 1))
            {
                c[k++] = 1;
                u = 1;
                break;
            }
            else
                x++;
            y--;
        }
        if (u == 0)
            c[k++] = 0;
    }
    for (int r = 0; r < k; r++)
    {
        if (c[r] == 1)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
