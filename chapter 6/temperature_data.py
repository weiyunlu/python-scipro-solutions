"""
Exercise 6.14: Compare average temperatures in cities
Author: Weiyun Lu
"""

from datetime import datetime
from numpy import asarray
import matplotlib.pyplot as plt

def make_citydict(filename):
    citydict = {}
    with open(filename, 'r') as infile:
        for line in infile:
            if line.find(".5in'><b>") != -1: #if found, we've got a city
                city = (line.split(".5in'><b>")[1]).split('( </b>')[0].strip()
            elif line.find('.txt">') != -1: #if found, we look for the filename
                txtfile = (line.split('.txt">')[1]).split('</a>')[0].strip()
                citydict[city] = txtfile
            else:
                continue
    return citydict
    
def citydata(cityname, citydict):
    filename = 'city_temp/' + citydict[cityname]
    citydata = {'name': cityname, 'temperatures': []}
    with open(filename, 'r') as infile:
        for line in infile:
            temp = float(line.split()[3].strip())
            if temp == -99:
                continue
            else:
                month = int(line.split()[0].strip())
                day = int(line.split()[1].strip())
                year = int(line.split()[2].strip())
                date = datetime(year,month,day)
                citydata['temperatures'].append((date, temp))
    return citydata

mycitydict = make_citydict('city_temp/citylistWorld.htm')

def plot_temps(*cities):
    citylist = []
    for city in cities:
        name = city['name']
        citylist.append(name)
        x = asarray([value[0] for value in citydata(name, mycitydict)['temperatures']])
        y = asarray([value[1] for value in citydata(name, mycitydict)['temperatures']])
        plt.plot_date(x, y , '-')
    plt.title('Temperatures over time')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.legend(citylist)
    plt.show()
    
#test run
Warsawdata = citydata('Warsaw', mycitydict)
Abidjandata = citydata('Abidjan', mycitydict)
Guangzhoudata = citydata('Guangzhou', mycitydict)
plot_temps(Warsawdata, Guangzhoudata, Abidjandata)