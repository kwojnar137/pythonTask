import sys

'''
#1
Load .txt file and process data line by line

#2
Spliting line by '/' separator and make list with int type line parts
Before changing type check data format of inputs for zero-padding or empty spaces

#3
Function makeDate receive previously validated inputs list and sort them before non repetition permutation
First fited to earliest permutation option is returned and printed in year-month-day format


'''




def checkMonthEnd(year, month, day):
    '''
    month set is generated by  
    '''
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        monthSet= {'1' : 31, '2' : 29, '3' : 31, '4' : 30, '5' : 31, '6' : 30 , '7' : 31 , '8' : 31, '9' : 30, '10' : 31, '11' : 30, '12' : 31}
    elif year % 4 != 0 or year % 100 == 0:
        monthSet= {'1' : 31, '2' : 28, '3' : 31, '4' : 30, '5' : 31, '6' : 30 , '7' : 31 , '8' : 31, '9' : 30, '10' : 31, '11' : 30, '12' : 31}

    if day > monthSet[str(month)]:
        return True
    else: 
        return False
    


def isValid(year, month, day):
    yearValid = False
    MonthValid = False
    DayValid = False
    
    if year >= 0 and year <= 999:
        yearValid = True
    elif year >= 2000 and year <= 2999:
        yearValid = True
    else:
        yearValid = False
        
    if month >= 1 and month <= 12:
        MonthValid = True
    else:
        MonthValid = False
        
    if day >= 1 and day <= 31:
        DayValid = True
    else:
        DayValid = False
            
    if yearValid and MonthValid and DayValid:
        if checkMonthEnd(year, month, day):
            return False
        
    if yearValid and MonthValid and DayValid:
        return True
    else: 
        return False

def makeDate(partsList):
    partsList.sort()
    
    year, month, day =  partsList[0], partsList[1], partsList[2]
    if isValid(year, month, day):
        date = [year, month, day]
        return date
    
    year, month, day =  partsList[0], partsList[2], partsList[1]
    if isValid(year, month, day):
        date = [year, month, day]
        return date
    
    year, month, day =  partsList[1], partsList[0], partsList[2]
    if isValid(year, month, day):
        date = [year, month, day]
        return date
    
    year, month, day =  partsList[1], partsList[2], partsList[0]
    if isValid(year, month, day):
        date = [year, month, day]
        return date
    
    year, month, day =  partsList[2], partsList[0], partsList[1]
    if isValid(year, month, day):
        date = [year, month, day]
        return date
    
    year, month, day =  partsList[2], partsList[1], partsList[0]
    if isValid(year, month, day):
        date = [year, month, day]
        return date
    
    return 'is Illegal'


def outputForm(date):
    if type(date) != type('is illegal'): #typo protected
        if date[0] < 1000:
            date[0] += 2000
            output = str(date[0]) + '-' + str(date[1]) + '-' + str(date[2])
            return output
        elif date[0] > 1000:
            output = str(date[0]) + '-' + str(date[1]) + '-' + str(date[2])
            return output
    else:
        return 'is illegal'


def splitLine(line):
    lineParts = line.split(sep='/')
    
    for index, part in enumerate(lineParts):
        if part == '':
            return 'is illegal'
        elif (part == '00' or part == '000'):
            lineParts[index] = '2000'
        elif (int(part) >= 32 and int(part) <= 99):
            add = int(part)
            lineParts[index] = int('20' + str(add))
             
    lineParts = list(map(int, lineParts))
    return lineParts

f = open('./' +  sys.argv[1], 'r')

date = ''
for line in f:
    partsList = splitLine(line)
    if partsList != 'is illegal':
        date = makeDate(partsList)
        dateOut = outputForm(date)
    else:
        dateOut = 'is illegal' 
    print(dateOut)

f.close()