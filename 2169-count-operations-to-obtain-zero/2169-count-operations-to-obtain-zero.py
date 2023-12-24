impl Solution {
    pub fn count_operations(mut num1: i32, mut num2: i32) -> i32 {
        let mut d = 0;
        while num1 != 0 && num2 != 0
        {
            if num1 < num2 
            {
                let c = num2;
                num2 = num1;
                num1 = c;
            }
            num1 -= num2;
            d += 1;
        }
        d
    }
}