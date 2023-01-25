
def gapAlgo(list1, list2, n, m):
  gap = (n + m) // 2

  while gap > 0:
    a = 0
    b = a + gap

    while b < n + m:
      if a < n:
        a_list = list1
      else:
        a_list = list2
      
      if b < n:
        b_list = list1
      else:
        b_list = list2

      if a_list == list1 and b_list == list1:
        if list1[a] > list2[b]:
          list1[a], list2[b] = list2[b], list1[a]
      elif a_list == list1 and b_list == list2:
        temp = b % n

        if list1[a] > list2[temp]:
          list1[a], list2[temp] = list2[temp], list1[a]
      else:
        temp1 = a % n
        temp2 = b % n

        if list1[temp1] > list2[temp2]:
          list1[temp1], list2[temp2] = list2[temp2], list1[temp1]

        
      a += 1
      b += 1

    gap //= 2
#wrong
