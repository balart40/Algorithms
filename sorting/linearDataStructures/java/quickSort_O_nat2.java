// package created by the IDE Eclipse, rename or create the same name
// ADA =  Analysis and Design of Algorithms class
package ADA_pkg;

public class QuickSort {

	public static int Partition(int[] array, int left, int right)
	{
		int x = array[right];
		int i = left -1;
		// the pseudo code in the book show from j to r-1, in a for that is
		// j<right again
		// need to be carefull about the bounds being inclusive or not
		// as well as the language program regarding arrays if its
		//1--N or 0-N-1 fashion
		for(int j=left;j<right;j++)
		{
			if(array[j]<=x)
			{
				i++;
				Utils.swap(array, i, j);
			}
		}
		Utils.swap(array, i+1, right);
		return i+1;
	}
	
	// From introduction to algorithms MIT press Page 171
	// left = p
	// right = r
	// pivot = q
	// Assuming an array A[left...........right]
	public static void QuickSort(int[] array, int left, int right)
	{
		if (left<right)
		{	
			int pivot = Partition(array, left, right);
			// Here we divide de array to sort to
			// A[left......pivot-1]
			QuickSort(array, left, pivot-1);
			// and A[pivot+1......r]
			QuickSort(array,pivot+1,right);
		}
	}
	
	public static void main(String[] args) 
	{
		int[] arrayForQuickSort = {1,2,5,26,7,14,3,7,12};
		System.out.println("Original array");
		Utils.printArray(arrayForQuickSort);
		// provide initial right to be the last one of the elements
		// Subtracting  1 since the array is from 0 to n-1 not 1 to n in java
		int initialRight = arrayForQuickSort.length-1;
		int initialLeft = 0;
		QuickSort(arrayForQuickSort,initialLeft,initialRight);
		System.out.println("Array after QuickSort");
		Utils.printArray(arrayForQuickSort);
	}
}
