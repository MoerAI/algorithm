#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    vector<pair<int, string>> v;
    v.push_back(pair<int, string>(90, "김철수"));
    v.push_back(pair<int, string>(93, "이철민"));
    v.push_back(pair<int, string>(97, "한용훈"));
    v.push_back(pair<int, string>(87, "나한빈"));
    v.push_back(pair<int, string>(92, "이상현"));

    sort(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++)
    {
        cout << v[i].second << ' ';
    }
    return 0;
}
