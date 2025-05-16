import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] input = scanner.nextLine().split(" ");
        int[] nums = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            nums[i] = Integer.parseInt(input[i]);
        }


        Arrays.sort(nums);

        int n = nums.length;


        long product1 = (long) nums[n - 1] * nums[n - 2] * nums[n - 3];


        long product2 = (long) nums[0] * nums[1] * nums[n - 1];


        if (product1 > product2) {
            System.out.println(nums[n - 3] + " " + nums[n - 2] + " " + nums[n - 1]);
        } else {
            System.out.println(nums[0] + " " + nums[1] + " " + nums[n - 1]);
        }
    }
}
