import time
import pandas as pd
import numpy as np
import calendar 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose a city from Chicago, New York or Washington:').lower()
        if city not in CITY_DATA:
            print('Please choose a correct city name')
            
        else:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
      month = input('Please Choose a month from January to June "or" All to display all the months:').lower()
      months = ['january', 'february', 'march', 'april', 'may','june']
      if month != 'all' and month not in months:
        print('Please choose a correct month name')
        
      else: 
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose a day of week from Sunday, Monday, ..., Saturday "or" all to display all the days of the week:').lower()
        days = ['sunday', 'monday','tuesday', 'wednesday', 'thursday', 'friday','saturday']
        if day != 'all' and day not in days:
            print('Please choose a correct week day name')
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df

def display_raw_data(df):
    
    i = 0
    Answer = input('Do you want to see 5 lines of raw data? yes/no: ').lower()
    pd.set_option('display.max_columns', None)
    while True:
        if Answer == 'no':
            break
        print(df[i:i+5])
        Answer = input('Do you want to see 5 lines of raw data? yes/no: ').lower()
        i += i+5
        


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month is:', calendar.month_name[common_month])
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week is:',common_day )
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour is:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    Common_start_station = df['Start Station'].mode()[0]
    print('Most common start station is:', Common_start_station )


    # TO DO: display most commonly used end station
    
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station is:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    
    Common_start_end_station = (df['Start Station'].mode()[0] + '-' + df['End Station'].mode()[0])
    print('Most frequent combination of start station and end station trip is:',Common_start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time is:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('Total number of users types:', user_types)

    # TO DO: Display counts of gender
    
    if 'Gender' in df:
        Gender = df['Gender'].value_counts()
        print('Counts of gender:', Gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df:
        Earliest_birth_year = int(df['Birth Year'].min())
        print('The earliest birth year:\n ', Earliest_birth_year )
        most_recent_birth_year = int(df['Birth Year'].max())
        print('The most recent birth year:\n ', most_recent_birth_year)
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('The most common birth year:\n ',most_common_birth_year )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
