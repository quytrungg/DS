#include <iostream>
using namespace std;

int coinFlip(int n, int H, int T)
{
    if (H < 0 || T < 0)
        return 0;
    if (n == 0)
        return 1;
    return coinFlip(n - 1, H - 1, T) + coinFlip(n - 1, H, T - 1);
};

int main()
{
    cout << coinFlip(3, 2, 1);
    return 0;
}
