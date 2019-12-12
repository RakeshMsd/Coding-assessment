def returnSum(myDictionary): 
      
    sum = 0
    for i in myDictionary: 
        sum = sum + myDictionary[i] 
    return sum
dict = {'akash': 985, 'suriya':963, 'abi':826} 
print("Sum :", returnSum(dict)) 