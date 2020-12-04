import java.util.*;

class Solution {
  public int calculate(String s) {
    Stack<String> stk = new Stack<>();

    StringBuilder curr = new StringBuilder();

    for (char c : s.toCharArray()) {
      if (c == ' ') {
        continue;
      }

      if (c >= '0' && c <= '9') {
        curr.append(c);
        continue;
      }

      // if string builder is not empy, we append the number to the stack
      if (curr.length() > 0) {
        int num = Integer.parseInt(curr.toString());
        curr.setLength(0);
        // check if previous operator is '*' or '/', if so, we calculate
        String op = "";
        if (stk.size() > 0) op = stk.peek();
        stk.push(Integer.toString(num));
        if (op.equals("*") || op.equals("/")) {
          singleOperation(stk);
        }
      }

      // if we encounter a "(" or + or - or / or /, we simply push it to the stack
      // else if we encounter a ")", we calculate the result within the parenthesis
      if (c == ')') {
        while (true) {
          String snum = stk.pop();
          if (stk.peek().equals("(")) {
            stk.pop();
            stk.push(snum);
            break;
          } else {
            stk.push(snum);
            singleOperation(stk);
          }
        }

        // after performing the operation, we need to check whether previous operator is * or /
        String snum = stk.pop();
        String op = "";
        if (stk.size() > 0) op = stk.peek();
        if (op.equals("*") || op.equals("/")) {
          stk.push(snum);
          singleOperation(stk);
        } else {
          stk.push(snum);
        }

        
      } else { // c is +, -, /, * or (
        stk.push(Character.toString(c));
      }

    }

    if (curr.length() > 0) {
      stk.push(curr.toString());
    }
    // at the end, we calculate the result for the stack
    while (stk.size() >= 3) {
      singleOperation(stk);
    }

    return Integer.parseInt(stk.pop());
  }


  private void singleOperation(Stack<String> stk) {
    if (stk.size() >= 3) {
      int num = Integer.parseInt(stk.pop());
      String op = stk.pop();
      int other = Integer.parseInt(stk.pop());
      if (op.equals("*")) {
        stk.push(Integer.toString(num * other));
      } else if (op.equals("/")) {
        stk.push(Integer.toString(other / num));
      } else if (op.equals("+")) {
        stk.push(Integer.toString(num + other));
      } else if (op.equals("-")) {
        stk.push(Integer.toString(other - num));
      }
    }
  }
}