import csv
from collections import Counter

#----------------------------------------------------------------------------
#|Defining the mean function                                                |   
#----------------------------------------------------------------------------

def mean():
    with open("Height-Weight.csv", newline = "") as f:
        reader = csv.reader(f)
        file_data = list(reader)

    file_data.pop(0)
    newData = []

    for i in range(len(file_data)):
        n_num = file_data[i][0]
        newData.append(float(n_num))

    n = len(newData)
    total = 0

    for x in newData:
        total += x

    mean = total / n

    print("Mean(Average) is -> " + str(mean))



#----------------------------------------------------------------------------
#|Defining the median function                                              |   
#----------------------------------------------------------------------------

def median():
    with open("Height-Weight.csv", newline = "") as f:
        reader = csv.reader(f)
        file_data = list(reader)

    file_data.pop(0)
    newData = []

    for i in range(len(file_data)):
        n_num = file_data[i][0]
        newData.append(float(n_num))

    n = len(newData)
    newData.sort()

    if n%2 == 0:
        median1 = float(newData[n//2])
        median2 = float(newData[n//2-1])
        median = (median1 + median2)/2
    else:
        median = newData[n//2]
    
    print("Median is -> " + str(median))



#----------------------------------------------------------------------------
#|Defining the mode function                                                |   
#----------------------------------------------------------------------------

def mode():

    with open("Height-Weight.csv", newline = "") as f:
        reader = csv.reader(f)
        fileData = list(reader)

    fileData.pop(0)

    newData = []

    for i in range(len(fileData)):
        n_num = fileData[i][1]
        newData.append(n_num)

    data = Counter(newData)

    modeDataForRange = {"50-60":0, "60-70":0, "70-80":0}

    for height, occurence in data.items():
        if 50<float(height)<60:
            modeDataForRange["50-60"] += occurence
        elif 60<float(height)<70:
            modeDataForRange["60-70"] += occurence
        elif 70<float(height)<80:
            modeDataForRange["70-80"] += occurence

    modeRange, modeOccurence = 0, 0

    for Range, occurence in modeDataForRange.items():
        if occurence>modeOccurence:
            modeRange, modeOccurence = [int(Range.split("-")[0]), int(Range.split("-")[1])], occurence

    mode = float((modeRange[0] + modeRange[1])/2)

    print("Mode is -> " + str(mode))



#----------------------------------------------------------------------------
#|Executing the functions                                                   |   
#----------------------------------------------------------------------------

mean()
median()
mode()