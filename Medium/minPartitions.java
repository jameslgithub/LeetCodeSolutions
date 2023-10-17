class Solution {
    public int minPartitions(String n) {
        char [] temp = n.toCharArray();
        int count = 0;
        for (int i = 0; i < n.length(); i++){
            if (temp[i] - '0' > count) {
                count = temp[i] - '0';
            }
        }
        return count;
    }
}
