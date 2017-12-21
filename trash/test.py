,'


threshold = 0.55
dictLab = []
classRes = []
classNum = 0
for header in tableHeader:
    if dictLab:
        res = []
        for tempDict in dictLab:
            #计算距离放入res
        if max(res) > threshold:
            pos = res.index(max(res))
            tempDict = dictLab[pos]
            for key in set(header):
                if type(key) != type('a') and np.isnan(key):
                    continue
                else:
                    value = tempDict.get(key, -1)
                    tempDict[key] = value + 1
            dictLab[pos] = tempDict
            classRes.append(pos)
        else:
            tempDict = dict()
            for key in header:
                tempDict.setdefault(key, 0)
            dictLab.append(tempDict)
            classRes.append(classNum)
            classNum += 1
    else:
        tempDict = dict()
        for key in header:
            tempDict.setdefault(key,0)
        dictLab.append(tempDict)
        classRes.append(classNum)
        classNum += 1
        
        