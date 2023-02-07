impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut x = 0;
        for i in operations.iter()
        {
            if i.chars().nth(0).unwrap() == '-' || i.chars().nth(i.len() - 1).unwrap() == '-'
            {
                x = x - 1;
            }
            else
            {
                x = x + 1;
            }
        }
        x
    }
}