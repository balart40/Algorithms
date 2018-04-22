// package created by the IDE Eclipse, rename or create the same name
// ADA =  Analysis and Design of Algorithms class
package ADA_pkg;


public class mergeSort {
	// pivot = q
	// right  = r
	// left = p
	// to maintain consistency with the pseudo code of the algorithm depicted
	// in Introduction to algorithms MIT press page 31
	public static void merge(int[] array, int left, int pivot, int right)
	{
		int n1 = pivot-left+1;
		int n2 = right - pivot;
		if((n1<=0) || (n2<=0))
		{
			return;
		}
		int i;
		int j;
		int[] L = new int[n1];
		int[] R = new int[n2];
		for(i = 0;i<n1;i++)
		{
			L[i] = array[left+i];
		}
		for(j = 0;j<n2;j++)
		{
			R[j] = array[pivot+j+1];
		}
		i = 0;
		j = 0;
		for(int k=left;k<=right;k++)
		{
			if(i<L.length && j<R.length)
			{
				if (L[i]<=R[j])
				{
					array[k] = L[i];
					i++;
				}
				else
				{
					array[k] = R[j];
					j++;
				}
			}
			else
			{
				if(i == L.length && j < R.length)
				{
					array[k] = R[j];
					j++;
				}
				if(j == R.length && i < L.length)
				{
					array[k] = L[i];
					i++;
				}
			}
		}
	}
	
	public static void mergeSort(int[] array, int left, int right)
	{
		if(left<right)
		{
			int pivot  = Math.floorDiv(left+right, 2);
			mergeSort(array,left,pivot);
			mergeSort(array,pivot+1,right);
			Utils.printArray(array);
			merge(array,left,pivot,right);
		}
	}
	
	public static void main(String[] args) 
	{
		int[] arrayForMergeSort = {1,2,5,26,7,14,3,7,12};
		System.out.println("Original array");
		Utils.printArray(arrayForMergeSort);
		// provide initial right to be the last one of the elements
		// Subtracting  1 since the array is from 0 to n-1 not 1 to n in java
		int initialRight = arrayForMergeSort.length-1;
		int initialLeft = 0;
		mergeSort(arrayForMergeSort, initialLeft, initialRight);
		System.out.println("Array after MergeSort");
		Utils.printArray(arrayForMergeSort);
	}
}
