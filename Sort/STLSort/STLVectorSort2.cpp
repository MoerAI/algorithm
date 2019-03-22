#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<string, pair<int, int>> a, pair<string, pair<int,int>> b)
{
    if(a.second.first == b.second.first)
    {
        return a.second.second > b.second.second;
    }
    else
    {
        return a.second.first > b.second.first;
    }
}

int main(void)
{
    vector<pair<string, pair<int, int>>> v;
    v.push_back(pair<string, pair<int, int>>("han", make_pair(90, 19961231)));
    v.push_back(pair<string, pair<int, int>>("cheer", make_pair(90, 19921207)));
    v.push_back(pair<string, pair<int, int>>("yeon", make_pair(95, 19930203)));
    v.push_back(pair<string, pair<int, int>>("up", make_pair(88, 19900302)));
    v.push_back(pair<string, pair<int, int>>("ji", make_pair(97, 19940630)));

    //compare가 없으면 이름순으로 정렬됨
    sort(v.begin(), v.end(), compare);
    for(int i = 0; i < v.size(); i++)
    {
        cout << v[i].first << ' ';
    }
    return 0;
}
