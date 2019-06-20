#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

class Solution
{
private:
    unordered_map<int, vector<string>> record;

public:
    vector<string> recursion(int n)
    {
        vector<string> result;
        if (n == 1)
            result.push_back("()");
        else if (record.find(n) == record.end()) {
            vector<string> subResult = recursion(n - 1);
            for (int i = 0; i < subResult.size; i++)
            {
                result.push_back("()" + subResult.at(i));
                result.push_back("(" + subResult.at(i) + ")");
            }
            record.insert({{n, result}});
        }
        else
        {
            result = record.find(n)->second;
        } 
        return result;
    }

    vector<string> generateParenthesis(int n) {
        return recursion(n);
    }
};

int main(int argc, char const *argv[])
{
    Solution *s = new Solution();
    for (int i = 1; i < 10; i++)
    {
        vector<string> result = s->generateParenthesis(i);
        for (int j = 0; j < result.size; j++)
        {
            cout << result.at(j) << endl;
        }
        cout << endl;
    }
    return 0;
}
