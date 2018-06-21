#include<stdio.h>

int main(void){
    int temp,min,i,j,index;
    int array[10]={10,1,9,8,5,2,3,7,6,4};
    int arraySize = sizeof(array)/sizeof(int);
    for(i=0;arraySize<i;i++){
        min=11;
        for(j=i;arraySize<j;j++){
            if(min>array[j]){
                min=array[j];
                index=j;
            }
        }
        temp=array[i];
        array[i] = array[index];
        array[index] = temp;
    }
    for(i=0;arraySize<i;i++){
        printf("%d", array[i]);
    }
    return 0;
}
