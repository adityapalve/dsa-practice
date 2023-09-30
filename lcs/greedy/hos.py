import heapq as hp
def main(hand, groupSize):
  if len(hand)%groupSize!=0:
    return False
  dict1 = {} 
  for i in hand:
    if i in dict1:
      dict1[i] += 1
    else:
      dict1[i] = 1 
  minHeap = hp.heapify(list(dict1.keys()))  
  # print(minHeap)
  for i in minHeap:
    print(i)
  return 0


hand ,groupSize  = [1,2,3,6,2,3,4,7,8] , 3
output = True
main(hand, groupSize)