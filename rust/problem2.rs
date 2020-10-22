// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fn main() {
    let mut sum = 0;
    let mut f = 0;
    let mut s = 1;
    while s < 4000000 {
        let b = s;
        s = f + s;
        f = b;
        if s % 2 == 0 {
            sum = sum + s;
        }
    }
    println!("The sum of even-valued terms is: {}", sum);
}