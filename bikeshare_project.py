import time
import pandas as pd
import numpy as np

city_main = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'satueday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

def get_filters():
    """
    first i assigned the city, month and day as global names in order to handle the gender and dob types that is
    not inculded in all the csv sheets """

    global city, month, day
    print('Hello! it seems that you want to explore some US bikeshare data!')

    #city inputs that allows the user to check the data based on his needs lower is assigned to avoid upper and lower cases issues
    city = input('Which city would you like to discover, Washington, new york city, or chicago?\n>>').lower()
    while city not in city_main:
        print('oops we only have info about washington, new york city, and chicago\n>>')
        city = input('Which city would you like to discover, Washington, new york city, or chicago?\n>>').lower()
    #month inputs that allows the user to check the data based on a specific period lower is assigned to avoid upper and lower cases issues
    month = input("Which month would you like to know about, we have the first half from january until june? type all for the whole period\n>>").lower()
    while month not in months:
        print("we are sorry but the available data are from january until June.\n>>")
        month = input("Which month would you like to know about, we have the first half from january until june? type all for the whole period\n>>").lower()


    #month inputs that allows the user to check the data based on a specific week day, also the whole week, lower is assigned to avoid upper and lower cases issues
    day = input("Which day would you like to know about?, (all, monday, tuesday, ETC)\n>>").lower()
    while day not in days:
        print("just make sure that you either type a day from saturday till friday, or all for all days\n>>")
        day = input("Which day would you like to know about?, (all, monday, tuesday, ETC)\n>>").lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """ here we are loading the data from the provided csv files that include all the data that a user might need to know about"""
    """ the last part about this function i used what was included in the project section for project problem 3 and solution 3, i tried to solve the problem and this code is way better and taught me this way """
    # to allow pandas to read the available csvs
    df = pd.read_csv(city_main[city])

    # to convert the columns to dates to extract the exact month and day based on previously specified inputs
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # to extract month and day of week from Start Time to show the statistics needed
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")

    # to filter the choices either by a month or id a user want to know about the whole period
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()
    print('the most common month for the selected period is: {} Note: 1 for january, 2 for february, ETC:\n>>'.format(common_month))

    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.strftime("%A")
    common_day = df['weekday'].mode()
    print('the most common weekday for the selected period: {}\n>>'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()
    print('cyclists used to start at: {}\n>>'.format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start= df['Start Station'].mode()
    print('cyclists love to start at: {}\n>'.format(commonly_start))

    # TO DO: display most commonly used end station
    commonly_end = df['End Station'].mode()
    print('cyclist usually end at: {}\n>>>'.format(commonly_end))

    # TO DO: display most frequent combination of start station and end station trip
    two_combination = (df['Start Station'] + df['End Station']).mode()
    print('cyclists most common route is: {}\n>>>'.format(two_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time for the selcted period: {}\n>>>'.format(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('the average travel time for the selcted period: {}\n>>>'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the count of each user type is: {}\n>>>'.format(user_types))

    if city != "washington":
    # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('the count of each gender for bikeshare users is: {}\n>>>'.format(gender_count))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()
        print('the oldest cyclists date of birth is: {}\n>>>'.format(earliest))
        print('Most youngest cyclists date of birth is: {}\n>>>'.format(most_recent))
        print('Most common cyclists date of birth for is: {}\n>>>'.format(most_common))
    else:
        print("washington doesn't have suffecient info about genders and date of birth")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    while True:
        display = input('would you like to display random samples and quick statistics\n>>').lower()
        if display == "yes":
            print('the first few rows of the data: {}\n>>>'.format(df.head()))

            print('the last few rows of the data: {}\n>>>'.format(df.tail()))

            print('overall quick stats: {}\n>>>'.format(df.describe()))
        else:
            print('No raw data required')
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
