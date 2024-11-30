#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(int x)
{
    string str = to_string(x);
    int str_size = str.length();

    for (int i = 0; i < str_size / 2; i++)
    {
        if (str[i] != str[str_size - 1 - i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int num;
    cin >> num;
    cout << isPalindrome(num);

    return 0;
}