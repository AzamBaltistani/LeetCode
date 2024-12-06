#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int height_size = height.size();
        int left = 0, right = height_size - 1, max_water = 0;

        for (int i = 0; i < height_size; i++)
        {
            max_water = max(max_water, (min(height[left], height[right]) * (height_size - 1 - i)));

            if (height[left] <= height[right])
                ++left;
            else
                --right;
        }

        return max_water;
    }
};

int main()
{
    Solution sol;

    vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7, 3};

    cout << height.size() << endl;
    cout << sol.maxArea(height);
}