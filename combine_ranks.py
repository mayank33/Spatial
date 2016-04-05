result_malls = "open_spaces_commercial_sorted"
newm = 0
for i in layers:
    if i.name() == result_malls:
        newm = i
        break

fins = []
newm_features = newm.getFeatures()        
for i in newm_features:
    fins.append([i['RANK']+i['RANK_2'],i.id()])
fins.sort()
num = 1
for i in fins:
    newm.changeAttributeValue(i[1], 88, num)
    num += 1
