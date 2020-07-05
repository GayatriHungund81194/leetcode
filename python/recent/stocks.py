def get_max_profit(stock_prices):
    profit = 0
    least_cost = stock_prices[0]
    for i in range(1,len(stock_prices)):
        if stock_prices[i] < least_cost:
            least_cost = stock_prices[i]
        prof = stock_prices[i] - least_cost
        if (prof>profit):
            profit = prof
    return profit
p = get_max_profit([1, 5, 3, 2])
print(p)