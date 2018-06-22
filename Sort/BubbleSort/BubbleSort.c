#include<stdio.h>

int main(void){
    int temp,i,j,index;
    int array[10]={10,1,9,8,5,2,3,7,6,4};
    int arraySize = sizeof(array)/sizeof(int);
    printf("Bubble Sort \n");
    for(i=0;i<arraySize;i++){
        for(j=0;j<arraySize-i-1;j++){
            if(array[j]>array[j+1]){
                temp=array[j];
                array[j]=array[j+1];
                array[j+1]=temp;
            }
        }
    }
    for(i=0;i<arraySize;i++){
        printf("%d ", array[i]);
    }
    return 0;
}
