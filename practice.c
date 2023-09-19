#include <stdio.h>
#include <stdlib.h>
void l_search(int arr[], int n, int x)
{
    int flag = 0;
    int i;
    for (i = 0; i < n; i++)
    {
        if (arr[i] == x)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 1)
    {
        printf("Element found at %d index", i);
    }
    else
    {
        printf("Element not found!!");
    }
}
int main()
{
    int n, x;
    printf("Enter size of array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the array elements: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("Enter the element you to search: ");
    scanf("%d", &x);
    l_search(arr, n, x);
    return 0;
}