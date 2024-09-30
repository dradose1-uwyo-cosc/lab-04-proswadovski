items = ["eggs","milk","honey","cereal","pop"]
prices =  [3,4,5,2,6]

for i in range(len(items)):
    print(f"I bought {items[i]} for ${prices[i]}")

total = 0
for t in prices:
    total = total + t
print(f"I spent ${total} at Walmart")
for t in 
leastindex = prices.index(min(prices))
print(f"The cheapest item was ${prices[leastindex]}")