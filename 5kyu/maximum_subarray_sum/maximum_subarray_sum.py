def max_sequence(arr):
    max_sum = []
    count = count1 = 0
    p = p1 = p2 = 0
    k = k1 = k2 = int(len(arr))
    if arr == []:
         return 0
    while count < int(len(arr)):   
        max_sum.append(sum(arr[i] for i in range(p, k)))
        max_sum.append(sum(arr[i] for i in range(p1, k1)))
        max_sum.append(sum(arr[i] for i in range(p1, k)))
        k2 = k
        p2 = p1
        count1 = 0
        while count1 < len(range(p1,k)):
                if k != int(len(arr)) and p1 != 0:
                        max_sum.append(sum(arr[i] for i in range(p1, k2)))
                        max_sum.append(sum(arr[i] for i in range(p2, k)))
                        k2 -= 1
                        p2 += 1
                count1 += 1
        k -= 1
        p1 += 1
        count += 1
    
    return max(max_sum)
