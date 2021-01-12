import datetime
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", 
          "Aug", "Sept", "Oct", "Nov", "Dec"]

def grab_data():
    city = []
    longitude = []
    latitude = []
    month = []
    monthnum = []
    sunshine = []

    with open('sunshine.csv', 'r', buffering = 1) as f:
        for line in f:
            line = line.split(',')
            city.append(str(line[0]))
            longitude.append(float(line[1]))
            latitude.append(float(line[2]))
            month.append(str(line[3]))
            monthnum.append(int(line[4]))
            sunshine.append(int(line[5]))

        uniq_cities = set(city)
        uniq_long = set(longitude)
        uniq_lat = set(latitude)

        # Define plot space
        fig, ax = plt.subplots(figsize=(16, 9))
        plt.xticks(np.arange(12),months)

        start = 0
        end = 12
        count = 12


        for city_idx,city_name in zip(range(len(uniq_cities)),uniq_cities):
            plt.plot(np.arange(12),sunshine[start:end],label=city_name)
            start += count
            end += count
        
        plt.legend(title='Cities', bbox_to_anchor=(1, .6), loc='upper left')
        #plt.legend('Chicago','Houston', 'Miami', 'New York', 'San Francisco', 'Seattle'))
        ax.set_title('Sunshine Hours Per Month by City from 1981-2010')
        plt.xlabel('Month')
        plt.ylabel('Sunshine (in hours)')
        fig.tight_layout(rect=[0,0,.87,1])
        plt.savefig("myousefa_a1.png")

grab_data()