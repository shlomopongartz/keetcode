using namespace std;

#include <iostream> 
#include <vector> 

class Solution {
public:
	void dutch_flags(vector<int>& nums, long &i,long &j, long &k) {
		i = 0;
		j = 0;
		k = nums.size() - 1;

		while (j <= k) {
			if (nums[j] < 0) {
				//swap A[i] and A[j]
				long tmp = nums[i];
				nums[i] = nums[j];
				nums[j] = tmp;
				++i;
				++j;
			} else if (nums[j] > 0) {
				// swap A[j] and A[k]
				long tmp = nums[k];
				nums[k] = nums[j];
				nums[j] = tmp;
				--k;
			} else {
				++j;
			}
		}
		return;
	}
	vector<vector<int>> threeSum(vector<int>& nums) {
		vector<vector<int>> out;
		long i, j, k;

		dutch_flags(nums, i, j, k);

		long negNum = i;
		long zerosNum = j - i;
		long posNum = nums.size() - j;

		std::sort(nums);

		cout << "negNum " << negNum << " zerosNum " << zerosNum << " posNum " << posNum << std::endl;

		for (auto i = nums.begin(); i != nums.end(); ++i) {
			cout << *i << " ";
		}
		cout << std::endl;
		out.push_back(nums);
		return out;
	}
};

int main(void)
{
	vector<int> nums = {1, 0, -1};
	vector<vector<int>> res;
	Solution s;

	res = s.threeSum(nums);
	cout << '[';
	for (int i = 0; i < res.size(); ++i) {
		cout << '[' << res[i][0] << "," << res[i][1] << "," << res[i][2] << "],";
	}
	cout << "]\n";

	return 0;
}
