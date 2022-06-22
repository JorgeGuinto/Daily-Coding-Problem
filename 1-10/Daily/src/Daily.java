import java.util.*;

public class Daily {
    public static void main(String[] args) {
        /*Problem 01
        int [] x = {-2,3,4,5,9};
        System.out.println(containsPairWithSum(x,8));*/
        /*Problem 02 */
        int [] x = {1, 2, 3, 4, 5};
        printArray(productArray(x));


    }

    /*Problem 01
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
    */
    public static boolean googleAddition (int [] array, int k){
        for (int i = 0; i <= array.length; i++){
            for (int j = i+1; j < array.length; j++){
                System.out.println(array[i] + " + " + array[j] + " = " + (array[i] + array[j]));
                if(array[i] + array[j] == k){
                    return true;
                } else{
                    continue;
                }
            }
        }
        return false;
    }

    //Solution found on Internet.
    public static boolean containsPairWithSum(int[] a, int x) {
        Arrays.sort(a);
        for (int i = 0, j = a.length - 1; i < j;) {
            int sum = a[i] + a[j];
            if (sum < x)
                i++;
            else if (sum > x)
                j--;
            else
                return true;
        }
        return false;
    }

    //Problem 02
    public static int[] arrayProduct (int [] a){
        int[] b = new int[a.length];
        for (int i = 0; i <= a.length-1; i++){
            int local = 1;
            for (int j = 0; j <= a.length-1; j++){
                if(i == j){
                    continue;
                }
                local *= a[j];
            }
            b[i] = local;
        }
        return b;
    }

    public static int[] productArray(int arr[]){
        int n= arr.length;
        if (n == 1) {
            System.out.print(0);
            return arr;
        }

        int left[] = new int[n];
        int right[] = new int[n];
        int prod[] = new int[n];
        left[0] = 1;
        right[n - 1] = 1;

        for (int i = 1; i < n; i++){
            left[i] = arr[i - 1] * left[i - 1];
        }
        for (int j = n - 2; j >= 0; j--){
            right[j] = arr[j + 1] * right[j + 1];
        }
        for (int i = 0; i < n; i++){
            prod[i] = left[i] * right[i];
        }
        return prod;
    }

    public static void printArray (int [] a){
        System.out.print("{");
        for (int i = 0; i <= a.length-1; i++){
            System.out.print(a[i] + ", ");
        }
        System.out.print("}");
    }


}