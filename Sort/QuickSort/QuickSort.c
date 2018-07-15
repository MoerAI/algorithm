#include<stdio.h>

int num = 10;
int array[10] = {10,9,8,3,1,5,4,2,6,7};
void quickSort(int *array, int start, int end);
int main(void){
    quickSort(array,0,num-1);
    for(int i=0; i<num; i++){
        printf("%d ",array[i]);
    }
    return 0;
}
void quickSort(int *array, int start, int end){
    if(start>=end){
        return;
    }
    int key = start;
    int i = start+1;
    int j = end;
    int temp;

    while(i<=j){
        while(array[i]<=array[key]){
            i++;
        }
        while(array[j]>=array[key]&&j>start){
            j--;
        }
        if(i>j){
            temp = array[j];
            array[j] = array[key];
            array[key] = temp;
        }else{
            temp = array[j];
            array[j] = array[i];
            array[i] = temp;
        }
    }
    quickSort(array, start, j-1);
    quickSort(array, j+1, end);
}
