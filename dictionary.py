
import urllib.request as web
import matplotlib.pyplot as pyplot


def plotQuakes():
    """
    Plot the locations of all the earthquakes in the past month. 
    
    Parameters: None.
    
    Return Value: None.
    """
    
    url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
    quakeFile = web.urlopen(url)
    header = quakeFile.readline()
    
    longitudes = []
    latitudes = []
    depths = []
    for line in quakeFile:
        line = line.decode('utf-8')
        row = line.split(',')
        latitudes.append(float(row[1]))
        longitudes.append(float(row[2]))
        depths.append(float(row[3]))
    quakeFile.close()
    
    colors = []
    
    for depth in depths:
        if depth < 10:
            colors.append('yellow')
        elif depth < 50:
            colors.append('red')
        else:
            colors.append('blue')
    
    pyplot.scatter(longitudes, latitudes, 10, color = colors)
    pyplot.show()
