import json
import csv
import codecs
import re

def generateNewCsv():
    jsonData = codecs.open('info.json', 'r', 'utf-8')
    csvfile = open('info.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter=',')
    keys = ['region', 'unit_price', 'total_price']
    writer.writerow(keys)
    for line in jsonData:
        dic = json.loads(line)
        region = dic['region'][0]
        unit_price = str(int(re.findall(r"\d+", dic['unit_price'][0])[0]))
        if dic['total_price'] == []:
            total_price = ''
        else:
            total_price = 0
            ls = re.findall(r"\d+", dic['total_price'][0])
            for num in ls:
                total_price += int(num)
            total_price /= len(ls)
            total_price = str(int(total_price))
        writer.writerow([region, unit_price, total_price])
    jsonData.close()
    csvfile.close()

if __name__ == '__main__':
    generateNewCsv()