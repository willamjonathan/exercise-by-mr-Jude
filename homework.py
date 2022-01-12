import csv
import pandas as pd
import matplotlib.pyplot as plt
import random as rand

df=pd.read_csv('activity.csv')
print(df.info())

def numbnans(df):
    return df.isnull().sum()

print('number of nans:')
print(numbnans(df))

def newdataset():
    new_dataset =df.copy()
    new_dataset.fillna(rand.randint(0,100), inplace=True)
    return new_dataset

print('\n new_dataset \n')
new_dataset=newdataset()
# df.dropna(inplace=True)

def steps(df):
    steps_per_day = df.groupby('date').sum()['steps']
    return steps_per_day.to_frame()

print('steps_per_day')
print(steps(df))

def histogram_of_total_steps_per_day(df):
    steps_per_day = steps(df)
    plt.hist(steps_per_day)
    plt.xlabel('Total Steps')
    plt.ylabel('Days')
    plt.title('Histogram of Total Steps Per Day')
    plt.show()

histogram_of_total_steps_per_day(df)

def get_mean_of_steps_per_day(df):
    mean_per_day=df.groupby('date').mean()['steps']
    return mean_per_day.to_frame().dropna()

print('MEAN')
print(get_mean_of_steps_per_day(df))
def get_median_of_total_steps_per_day(df):
    mean_per_day=df.groupby('date').median()['steps']
    return mean_per_day.to_frame().dropna()

print('MEDIAN')
print(get_median_of_total_steps_per_day(df))

#time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all days (y-axis)
def plot_mean_of_total_steps_per_day():
    plt.plot(get_mean_of_steps_per_day(df), 'r')
    plt.xlabel('5-minute Interval')
    plt.ylabel('Mean Steps Per Day')
    plt.title('Mean of Total Steps Per Day')
    plt.show()

plot_mean_of_total_steps_per_day()

print('DAY THAT HAS MOST STEPS:')
def get_date_that_have_max_steps_per_5_minute_interval():
    steps_per_day = steps(df)
    return steps_per_day.idxmax()

print(get_date_that_have_max_steps_per_5_minute_interval())

histogram_of_total_steps_per_day(new_dataset)
print('MEAN OF NEW DATASET')
print(get_mean_of_steps_per_day(new_dataset))
print('MEDIAN OF NEW DATASET')
print(get_median_of_total_steps_per_day(new_dataset))

#classify dates to weekend or weekdays
df['WEEKDAY'] = pd.to_datetime(df['date']).dt.dayofweek
weekdays=[]
weekends=[]
weekdays_average_steps=[]
weekends_average_steps=[]

for i in range(len(df)):
    if df['WEEKDAY'][i]<5:
        weekdays.append(df['date'][i])
        weekdays_average_steps.append(df['steps'][i])
    else:
        weekends.append(df['date'][i])
        weekends_average_steps.append(df['steps'][i])


#plotting the average steps per day for weekdays and weekends
plt.figure(figsize=(20,5), dpi=100)
plt.plot(weekdays, weekdays_average_steps, 'ro')
plt.plot(weekends, weekends_average_steps, 'bo')
plt.xlabel('Date')
plt.ylabel('Average Steps Per Day')
plt.title('Average Steps Per Day for Weekdays and Weekends')
plt.show()
