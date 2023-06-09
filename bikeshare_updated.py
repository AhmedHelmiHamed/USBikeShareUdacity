import time
import pandas as pd
import numpy as np
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
    print('Please enter the required city (chicago, new york city, washington).')
    city=input()
    city=city.lower()
    while city!='chicago' and city!= 'new york city' and city !='washington':
     
        print('You entered a wrong value, try again')
        city=input()
        city=city.lower()
    

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Please enter the required month (january, february,..., june or all).')
    month = input()
    month = month.lower()
    while month !='all' and month !='january' and month !='february' and month !='march' and month !='april' and month !='may' and month !='june':
        print('You entered a wrong value, try again')
        month = input()
        month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Please enter the required weekday (sunday, monday,..., saturday or all).')
    day = input()
    day = day.lower()
    while day !='all' and day !='sunday' and day !='monday' and day !='tuesday' and day !='wednesday' and day !='thursday' and day !='friday' and day !='saturday':
        print('You entered a wrong value, try again')
        day = input()
        day = day.lower()

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
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
        # TO DO: display the most common month
    print('The most common month is ')
    print(df['month'].mode())
    
    
        # TO DO: display the most common day of week
    print('The most common day is ' )
    print(df['day_of_week'].mode())


    # TO DO: display the most common start hour
    print('The most common hour is ' )
    print(df['hour'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is ' )
    print(df['Start Station'].mode())

    # TO DO: display most commonly used end station
    print('The most commonly used end station is ' )
    print(df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip
    print("The most commonly used route is")
    print((df['Start Station']+"-->"+df['End Station']).mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total trips travel time in seconds is ' + str(df['Trip Duration'].sum())+' seconds')

    # TO DO: display mean travel time
    print('The trip duration in seconds is ' + str(df['Trip Duration'].mean())+' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The count of types of users is as follows')
    print(df['User Type'].value_counts())
    if 'Gender' in df:
        # TO DO: Display counts of gender
        print('The count of types of users is as follows')
        print(df['Gender'].value_counts())
    
    if 'Birth Year' in df:
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is ' + str(df['Birth Year'].dropna(axis=0) .min()))
        print('The most recent year of birth is ' + str(df['Birth Year'] .dropna(axis=0).max()))
        print('The most common year of birth is ' + str(df['Birth Year'] .dropna(axis=0).mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """ Asks the user if he/she wants to display the raw data for 5 users, after displaying them, the function asks the user if he/she needs the data of the next five users till the user input any other thing than yes"""
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes to proceed or any other input to stop \n").lower()
    start_loc = 0
    while (view_data=='yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: Enter yes to proceed or any other input to stop \n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
