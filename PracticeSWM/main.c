#include <stdio.h>
#include <stdlib.h>

int main()
{
    int index, mini, temp;
    int array[10] = {3, 5, 6, 7, 8, 2, 10, 1, 4, 9};

    for(int i = 0; i < 10; i++)
    {
        mini = 99999;

        for(int j = i; j < 10; j++)
        {
            if(mini>array[j])
            {
                mini = array[j];
                index = j;
            }
        }
        temp = array[i];
        array[i] = array[index];
        array[index] = temp;
    }

    for(int i = 0; i < 10; i++)
    {
        printf("%d ",array[i]);
    }

    return 0;
}
