List_A = ['Ginger', 'Willow', 'Scout', 'Roscoe', 'Bear', 'Kobe', 'Baxter', 'Zara',
          'Fiona', 'Milo', 'Oakley', 'Dakota', 'Prince', 'Bruno', 'Panda', 'Dexter',
          'Ziggy', 'Roscoe', 'Lucy', 'Boomer', 'Fiona', 'Ella', 'Emma', 'Oakley']

Dict_A = {}

for name in List_A:
    if name not in Dict_A.keys():
        Dict_A[name] = 1
    else:
        count = Dict_A[name]
        count += 1
        Dict_A[name] = count

print(Dict_A)
