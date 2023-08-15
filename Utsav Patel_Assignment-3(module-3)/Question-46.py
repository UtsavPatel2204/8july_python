a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
combine={}
val=0
for d in a:
    if d['item'] not in combine:
        combine[d['item']] = d['amount']
    else:
        combine[d['item']] += d['amount'] 
print(combine) 