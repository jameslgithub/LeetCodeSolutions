class Solution {
    public int mostWordsFound(String[] sentences) {
        int temp = 0;
        for (int i = 0; i < sentences.length; i++) {
            System.out.println(sentences[i]);
            String [] words = sentences[i].split("\\s+");
            if (words.length > temp) {
                temp = words.length;
            }
        }
        return temp;
        
    }
}
