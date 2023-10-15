class Solution {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        int middle = nums.length / 2;
        while (start <= end){
            middle = start + (end - start) / 2;
            if (nums[middle] == target) {
                return middle;
            }
            else if (nums[middle] > target) {
                end = middle - 1;
            }
            else start = middle + 1;
        }
        return start;
    }
}
