import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities  = ['chicago', 'new york city', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you want to explore in three cities: chicago, new york city or washington?\n Your answer: ")
        city = city.lower()
        if city in cities:
            break
        else:
            print("ERROR: This city is not existed in our explore list! Please choose another!\n")
    # get user input for month (all, january, february, ... , june)
    while True:    
        month = input("Which month would you want to specific explore in first six month?\nNote: If want to explore all six month, please type 'all'\n Your answer: ")
        month = month.lower()
        if month in months:
            break
        else:
            print("ERROR: This month is not existed in our explore list! Please choose another!\n")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of week would you want to specific explore?\nNote: If want to explore all week, please type 'all'\n Your answer: ")
        day = day.lower()
        if day in days:
            break
        else:
            print("ERROR: This month is not existed in our explore list! Please choose another!\n")
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
    #load data into frame
    df = pd.read_csv(CITY_DATA[city])
    
    #convert Start Time to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #create new column: moth
    df['month'] = df['Start Time'].dt.month
    
    #create new column: day of week
    df['day of week'] = df['Start Time'].dt.weekday_name
    
    #create new column: start hour
    df['start hour'] = df['Start Time'].dt.hour
    
    #filter months
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    #filter day of week
    if day != 'all':
        df = df[df['day of week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day of week'].mode()[0]
    print('Most common day of week: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['start hour'].mode()[0]
    print('Most common start hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_used_start_station = df['Start Station'].mode()[0]
    print('Most common used start station: ', most_common_used_start_station)

    # TO DO: display most commonly used end station
    most_common_used_end_station = df['End Station'].mode()[0]
    print('Most common used end station: ', most_common_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_start_and_end_station'] = df['Start Station'] + ", " + df['End Station']
    print('Most frequent combination of start station and end station trip: ', df['combination_start_and_end_station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('Number of User Types:\n', counts_of_user_types)

    # TO DO: Display counts of gender
    try:
        counts_of_gender =  df['Gender'].value_counts()
        print('Number of Gender: \n', counts_of_gender)
    except KeyError:
        print("ERROR: This city does not have Gender data so can not find counts of gender!\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    #earliest_year_of_birth
    try:
        earliest_year_of_birth =  df['Birth Year'].min()
        print('Earliest year of birth: ', earliest_year_of_birth)
    except KeyError:
        print("ERROR: This city does not have birth year data so can not find the earliest year of birth!\n")
    #most_recent_year_of_birth
    try:
        most_recent_year_of_birth = df['Birth Year'].max()
        print('Most recent year of birth: ', most_recent_year_of_birth)
    except KeyError:
        print("ERROR: This city does not have birth year data so can not find the most recent year of birth!\n")
    #most_common_year_of_birth
    try:
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth: ', most_common_year_of_birth)
    except KeyError:
        print("ERROR: This city does not have birth year data so can not find the most common year of birth!\n")

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
