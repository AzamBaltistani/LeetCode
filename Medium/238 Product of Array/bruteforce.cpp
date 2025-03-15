#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        vector<int> ans = {};

        for (int i = 0; i < nums.size(); i++)
        {
            int product = 1;
            for (int j = 0; j < nums.size(); j++)
            {
                if (i == j)
                    continue;

                product *= nums[j];
            }

            ans.push_back(product);
        }

        return ans;
    }
};

int main()
{

    Solution sol;
    vector<int> nums = {};

    for (int i = 0; i < 1000000; i++)
    {
        nums.push_back(3);
    }

    sol.productExceptSelf(nums);
}