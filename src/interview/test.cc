#include <iostream>

using namespace std;

int sumDigit(int n)
{
    int sum = 0;
    while (n >= 10)
    {
        int r = n % 10;
        sum += r;
        n /= 10;
    }
    return sum + n;
}

int findBiggest(int *arr, int n)
{
    int max = 0;
    for (int i = 0; i < n; i++)
    {
        max = arr[i] > max ? arr[i] : max;
    }
    return max;
}

// [1,2,3,4,5,6,7,8,9,10,11,12]
// [1,2,3,4,5,6,7,8,9,1,2,3]
// s trung so

// 3

// [1,2,3]
// 3

int lotteryCoupons(int n)
{
    int *temp = new int[n];
    for (int i = 0; i < n; i++)
    {
        temp[i] = sumDigit(i + 1);
    }
    int max = findBiggest(temp, n);
    int *count = new int[max];
    for (int i = 0; i < max; i++)
    {
        count[i] = 0;
    }
    for (int i = 0; i < n; i++)
    {
        count[temp[i] - 1]++;
    }
    int maxOccur = findBiggest(count, max);
    int result = 0;
    cout << maxOccur << "\n";
    for (int i = 0; i < max; i++)
    {
        cout << count[i] << "\n";
        if (count[i] == maxOccur)
        {
            result++;
        }
    }
    return result;
}

int main()
{
    // lotteryCoupons(12);
    cout << lotteryCoupons(3);
    return 0;
}