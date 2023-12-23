impl Solution {
    pub fn sum_of_multiples(n: i32) -> i32 {
        let mut c = 0;
        for x in 1..n + 1
        {
            if x%3==0||x%5==0||x%7==0{
                c += x;
            }
        }
        c
    }
}