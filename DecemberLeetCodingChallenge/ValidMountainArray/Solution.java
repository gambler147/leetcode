class Solution {
    public boolean validMountainArray(int[] arr) {
        // two pointers, go through from each end of arr
        // and if both ends increase to same position, then 
        // it is a mountain array
        int n = arr.length;
        
        int i=0;
        while (i+1<n && arr[i+1] > arr[i]) {
            i++;
        }
        
        int j=n-1;
        while (j-1 >=0 && arr[j-1] > arr[j]) {
            j--;
        }
        
        return (i > 0 && j < n-1 && j==i);
    }
}