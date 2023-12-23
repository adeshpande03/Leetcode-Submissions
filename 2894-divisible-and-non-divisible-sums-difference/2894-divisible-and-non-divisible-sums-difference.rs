impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        let mut d = 0;
        for i in 1..n+1{
            if (i % m == 0){
                d -= i;
            }
            else{d += i;}
        }
        d
    }
}