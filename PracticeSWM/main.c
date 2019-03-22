#include <stdio.h>

int number, data[1000000];

void quickSort(int* data, int start, int end)
{
    if(start >= end)//원소가 1개인 경우 그대로 두기
    {
        return;
    }

    int key = start;//키는 첫 번째 원소
    int i = start + 1, j = end, temp;

    while(i <= j)
    {
        while(data[i] <= data[key])//키보다 큰 값을 만날 때까지
        {
            i++;
        }
        while(data[j] >= data[key] && j > start)
        {
            j--;
        }
        if(i > j)
        {
            temp = data[j];
            data[j] = data[key];
            data[key] = temp;
        }
        else
        {
            temp = data[i];
            data[i] = data[j];
            data[j] = temp;
        }
    }

    quickSort(data, start, j - 1);
    quickSort(data, j + 1, end);
}

int main()
{
    scanf("%d", &number);
    for(int i = 0; i < number; i++)
    {
        scanf("%d",&data[i]);
    }
    quickSort(data, 0, number - 1);
    for(int i = 0; i < number; i++)
    {
        printf("%d\n", data[i]);
    }
    return 0;
}
