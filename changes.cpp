#include <bits/stdc++.h>
using namespace std;
int main()
{
    long t, n, a, b, d[200000], e, f, g[200000], h = 0, k;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n >> b >> a;
        for (long j = 0; j < n; j++)
        {
            cin >> d[j];
        }
        e = b;
        f = a;
        for (k = 0; k < n; k++)
        {
            if (d[k] == 0)
            {
                if (f - 1 >= 0)
                    f = f - 1;
                else if (e - 1 >= 0)
                    e = e - 1;
                else
                    break;
            }
            else
            {
                if ((e - 1 >= 0) && (f != a))
                {
                    e = e - 1;
                    f = f + 1;
                }
                else if (f - 1 >= 0)
                    f = f - 1;
                else
                    break;
            }
        }
        g[h++] = k;
    }
    for (int i = 0; i < h; i++)
    {
        cout << g[i] << endl;
    }
}
