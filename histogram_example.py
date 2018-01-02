import pandas
import matplotlib.pyplot as plt

subway_data = pandas.read_csv('turnstile_data_master_with_weather.csv')
plt.figure()
subway_data = subway_data[subway_data['rain']==0].hist()
subway_data = subway_data[subway_data['rain']==1].hist()

subway_data.plot()
plt.show()