impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut v = Vec::new();
        for i in accounts.iter()
        {
            v.push(i.iter().sum());
        }
        return *v.iter().max().unwrap();
    }
}