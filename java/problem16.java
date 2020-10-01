
public class problem16{
public static void main(String[] args) {

    ArrayList<Integer> n = myPow(2, 100);

    int result = 0;
    for (Integer i : n) {
        result += i;
    }

    System.out.println(result);
}

public static ArrayList<Integer> myPow(int n, int p) {
    ArrayList<Integer> nl = new ArrayList<Integer>();
    for (char c : Integer.toString(n).toCharArray()) {
        nl.add(c - 48);
    }

    for (int i = 1; i < p; i++) {
        nl = mySum(nl, nl);
    }

    return nl;
}

public static ArrayList<Integer> mySum(ArrayList<Integer> n1, ArrayList<Integer> n2) {
    ArrayList<Integer> result = new ArrayList<Integer>();

    int carry = 0;

    int max = Math.max(n1.size(), n2.size());
    if (n1.size() != max)
        n1 = normalizeList(n1, max);
    if (n2.size() != max)
        n2 = normalizeList(n2, max);

    for (int i = max - 1; i >= 0; i--) {
        int n = n1.get(i) + n2.get(i) + carry;
        carry = 0;
        if (n > 9) {
            String s = Integer.toString(n);
            carry = s.charAt(0) - 48;
            result.add(0, s.charAt(s.length() - 1) - 48);
        } else
            result.add(0, n);
    }

    if (carry != 0)
        result.add(0, carry);

    return result;
}

public static ArrayList<Integer> normalizeList(ArrayList<Integer> l, int max) {
    int newSize = max - l.size();
    for (int i = 0; i < newSize; i++) {
        l.add(0, 0);
    }
    return l;
}
}