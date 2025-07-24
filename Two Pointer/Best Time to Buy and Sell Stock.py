cur = prices[0]

profit = 0

for i in range(1, len(prices)):
    if prices[i] - cur > profit:
        profit = prices[i] - cur
    
    if cur > prices[i]:
        cur = prices[i]

print(profit) 