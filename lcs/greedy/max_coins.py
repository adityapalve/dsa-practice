def maxCoins(piles):

  piles.sort()
  coins = 0

  for i in range(len(piles)+1):
    if i % 3 == 0 and i!= 0:
      
      coins += piles[i-2]
    
    print(coins)

  return coins

piles = [2,4,1,2,7,8]
output = 9
print(maxCoins(piles))