#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>

using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        tmp = new int [nums.size()];
        sort(nums.begin(), nums.end()); 
        permuteUnique(nums, 0, res);
        delete [] tmp;
        return res;
    }
private:
	void permuteUnique(vector<int>& nums, int from, vector<vector<int>> &res) {
		if (from == nums.size()) {
			vector<int> t(tmp, tmp + from + 1);
			res.push_back(t);
			return;
		}
		for (int i = from; i < nums.size(); ++i) {
			tmp[i] = nums[i];
			vector<int> newnums(nums.begin(), nums.begin() + from);
			newnums
			permuteUnique(newnums, int from + 1, res)
		}
	}
	static int *tmp;
};

int *Solution::tmp = nullptr;

void compare(vector<vector<int>> &res, vector<vector<int>> &exp)
{
	if (res.size() != exp.size()) {
		cout << "different size" << endl;
	}
}

int main()
{
	Solution s;
	{
		vector<int> nums{1,1,2};
		vector<vector<int>> res = s.permuteUnique(nums);
		vector<vector<int>> exp{{1,1,2},{1,2,1},{2,1,1}};
		compare(res, exp);
	}
	{
		vector<int> nums{1,2,3};
		vector<vector<int>> res = s.permuteUnique(nums);
		vector<vector<int>> exp{{1,2,3},{1,3,2},{2,1,3},{2,3,1},{3,1,2},{3,2,1}};
		compare(res, exp);
	}
}
