# main.py
nums=[2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, 2, 4, 1, 3, 2, 5, ]
def partition(nums):
  equal=[]
  lesser=[]
  greater=[]
  if len(nums)>1: 
    pivot=nums[0]
    for i in range(len(nums)):
      if pivot > nums[i]:
        lesser.append(nums[i])
      elif pivot == nums[i]:
        equal.append(nums[i])
      elif pivot < nums[i]:
        greater.append(nums[i])
  else:
    print("TOO SHORT of a list")
  return equal,lesser,greater
  
def quickSort(nums):
  if len(nums)<=1:
    return nums
  equal,lesser,greater=partition(nums)
  e=quickSort(lesser)
  d=quickSort(greater)
  tada=[]
  tada.extend(e)
  tada.extend(equal)
  tada.extend(d)
  return tada
print(quickSort(nums))


#n * log(n)
