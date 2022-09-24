#include <iostream>

bool func(int *arr, int n)
{
    int max = arr[0];
    for (int i = 1; i < n; i++)
    {
        max = arr[i] > max ? arr[i] : max;
    }
    bool *check = new bool[max * max + 1];
    for (int i = 0; i < max * max + 1; i++)
    {
        check[i] = false;
    }
    for (int i = 0; i < n; i++)
    {
        check[arr[i] * arr[i]] = true;
    }
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (check[arr[i] * arr[i] + arr[j] * arr[j]])
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int a[4] = {3, 12, 5, 13};
    std::cout << func(a, 4);
    return 0;
}