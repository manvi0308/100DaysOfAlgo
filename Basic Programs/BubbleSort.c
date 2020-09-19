#include<stdio.h>
#include<conio.h>

# Function describing bubble sort
void bubbleSort(int arr[], int n)
{
	int i, j;
	for(i=0; i<n-1; i++)
	{
		for(j=0; j<n-i-1; j++)
		{
			if(arr[j] > arr[j+1])
			{
				swap(&arr[j], &arr[j+1]);
			}
		}
	}
}

# swap function used to swap two variables
void swap(int *xp, int *yp)
{
	int temp;
	temp = *xp;
	*xp = *yp;
	*yp = temp;
}

# A utility function to print an array
void printArray(int arr[], int size)
{
	int i;
	for(i=0; i<size; i++)
	{
		printf("%d\t", arr[i]);
	}
}

# Driver code
void main()
{
	int arr[] = {11, 6, 0, 1, 67};
	int size = sizeof(arr)/sizeof(arr[0]);
	bubbleSort(arr, size);
	printArray(arr, size);
}
