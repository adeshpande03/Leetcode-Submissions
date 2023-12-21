impl Solution {
    pub fn buy_choco(mut prices: Vec<i32>, money: i32) -> i32 {
        prices.sort();
        let c = money - prices[0] - prices[1];
        if (c >= 0)
        {
            return c;
        }
        else{
        return money;}
    }
}