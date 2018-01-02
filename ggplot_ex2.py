import csv

import ggplot
import pandas
import requests
from ggplot import aes, geom_bar

def plot1(data):
    xvar = data['teamID' == 'SFN']
    yvar = data['teamID' == 'LAN']
    gg = ggplot(data, aes(xvar,yvar))+ geom_bar()
    return gg

if __name__ == '__main__':
    data = pandas.read_csv('hr_by_team.csv')
    print data
    print plot1(data)