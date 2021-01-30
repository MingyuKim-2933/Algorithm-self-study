# arr = [5, 3, 7, 9, 2, 5, 2, 6]
# arrMin = float('inf')  # 'inf' = 최댓값
# for i in range(len(arr)):
#     if arr[i] < arrMin:
#         arrMin = arr[i]
# print(arrMin)

# another solution
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')  # 'inf' = 최댓값
for x in arr:
    if x < arrMin:
        arrMin = x
print(arrMin)
