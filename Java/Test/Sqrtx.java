class Solution {
    public int mySqrt(int x) {
        int result = 1;
        while (result * result <= x) {
            result++;
        }
        if (result - 1 > 46339) {
            return 46340;
        }
        return result - 1;
    }
}

public class Sqrtx {
    public static void main(String[] args) {
        Solution s = new Solution();
        for (int i = 2147395580; i < 2147395610; i++) {
            System.out.println(i + " " + s.mySqrt(i));
        }
    }
}