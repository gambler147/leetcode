class Solution {
    public String decodeAtIndex(String S, int K) {
        // use a stack to store batches of characters or numbers
        // record current length of decoded strings, when reaching K,
        // revert to last batch string to find whether the string contains
        // Kth character, if not, pop it and module by last number. Repeat until
        // finding the character
        Stack<String> stack = new Stack<>();
    
        StringBuilder sb = new StringBuilder();
        long mul = 1;
        long cur = 0;
        for (char c : S.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                if (mul > 1) {
                    stack.push(String.valueOf(mul));
                    cur *= mul;
                    mul = 1;
                }
                sb.append(c);
            }
            
            if (c >= '2' && c <= '9') {
                if (sb.length() > 0) {
                    String x = sb.toString();
                    stack.push(x);
                    cur += x.length();
                    sb.setLength(0);
                }
                mul *= c - '0';
            }
            
            // stop when cur >= K
            if (cur >= K) {
                break;
            }
        }
        // if sb is not empty, add it to stack, this is the case when we reach the end of S
        if (sb.length() > 0) {
            String x = sb.toString();
            stack.push(x);
            sb.setLength(0);
            cur += x.length();
        }
        // if mul is not 1, multiply cur by mul
        if (mul > 1) {
            stack.push(String.valueOf(mul));
            cur *= mul;
        }
        // then we repeat by checking the end of stack
        while (true) {
            String x = stack.pop();
            // check if x is digits or letters
            char lead = x.charAt(0);
            if (lead >= '0' && lead <= '9') {
                int n = Integer.parseInt(x);
                int n0 = (int) (cur / (long) n); // length of previous decoded string
                // K -> K % prev
                K %= n0;
                if (K == 0) K = n0;
                cur = n0;
            } else {
                // x is letters, we check if x contains Kth character
                int len = x.length();
                long n0 = cur - len;
                if (K > n0) {
                    return Character.toString(x.charAt(K-(int) n0-1));
                }
                // otherwise, cur -> cur - len
                cur -= len;
            }

        }
        
    }
}

