#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int a, int b)
{
    //오름차순 내림차순을 변경 할 수 있다.
    return a > b;
}

int main(void)
{
    int a[10] = {9, 3, 5, 4, 1, 10, 8, 6, 7, 2};
    sort(a, a + 10, compare);
    for(int i = 0; i < 10; i++)
    {
        cout << a[i] << ' ';
    }
}
