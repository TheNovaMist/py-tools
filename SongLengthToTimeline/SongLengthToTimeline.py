import re
from datetime import datetime, timedelta


def addTimeStamp(timePoint, duration):
    # begin of time stamp str 
    # duration time str

    # convert to datetime object
    dt = datetime.strptime(timePoint, "%M:%S")

    # get minute and second
    temp = datetime.strptime(duration, "%M:%S")
    m = temp.minute
    s = temp.second
    res = (dt + timedelta(minutes = m, seconds = s)).strftime("%M:%S")

    # new timePoint
    return res


if __name__ == '__main__':

    rawText = ""

    # 1. read raw txt file
    with open("./Disc.txt", 'r', encoding='utf-8') as f:
        # print(f.read())
        rawText = f.read()
    
    # print(rawText)

    # 2. split Disc 1 and Disc 2
    lines = rawText.split('Disc 2')
    # print(lines[0])
    # print(lines[1])
    

    # 3. use re to filter list
    rawLines = list(filter(lambda x: re.match('\d{2}\s.*', x) != None, lines[1].split('\n')))
    # print(rawLines)

    # 4. filter timestamp for each line
    durationList = []
    for line in rawLines:
        # list to string
        durationList.append(''.join(re.findall(r'\d:\d\d', line)))
    # print(durationList)

    # 5. get timePoint list
    timePointList = ['00:00']
    timePoint = '00:00'
    for duration in durationList:
        timePoint = addTimeStamp(timePoint, duration)
        timePointList.append(timePoint)

    # print(timePointList)
    # print(rawLines)

    # 6. replace duration to timePoint
    result = []
    for i in range(len(rawLines)):
        line = rawLines[i]
        parts = line.rsplit(' ', 1) # split from right two parts
        line = parts[0] + ' ' + timePointList[i]
        result.append(line)
    # print(result)


    # 7. write to txt file
    with open('./timeline.txt', 'a', encoding='utf-8') as out:
        for r in result:
            out.write("%s\n" % r)
