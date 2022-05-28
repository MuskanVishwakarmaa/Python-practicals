#Q7. Print the Sum of Key Value Pairs in a Given Dictionary
D = {2: 8, 5: 20, 3: 15}
res_sumList = []
for key in D:
  res_sumList.append(key + D[key])
print("Sum of Key-value pairs is =",list(res_sumList))