/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let bestBuy = prices[0];
    let maxprofit = 0;
    for(let i=0; i<prices.length; i++){
        if(prices[i] > bestBuy){
            maxprofit = Math.max(maxprofit, prices[i] - bestBuy)
        }
        bestBuy = Math.min(bestBuy, prices[i]);
    }
    return maxprofit;
};