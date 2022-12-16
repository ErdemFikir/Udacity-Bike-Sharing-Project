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
    while True:
         try:
             # with a try-except mechanism, user input problems are being eleminated
             city = (input("Please type the city name (like; all,chicago, new york city, washington) : ")).lower()
             break
         except ValueError:
             #if a value Error happens, code goes to begining and get the user inputs again
             print("You didn't enter valid data, please try again")   

    
       
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
             try:
                 month = (input("Please type the month name (like; all, january, february, ... , june) : ")).lower()
                 break
             except ValueError:
                 print("You didn't enter valid data, please try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = (input("Please type the city day name (like; all, monday, tuesday, ... sunday) : ")).lower()
            break
        except (KeyError,ValueError):
            # If user doesn't enter correct values,
            print("You didn't enter valid data, please try again")

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
    
    while True:
        
        try: 
            # Data frame is being created
            if ( city.lower() != 'all'):
                # If we have 
                df = pd.DataFrame(pd.read_csv(CITY_DATA[city]))
            else:
                df = pd.concat(map(pd.read_csv, [CITY_DATA['chicago'], CITY_DATA['new york city'],CITY_DATA['washington']]), ignore_index=True)
            
            # Converting Start Time to date time
            df['Start Time'] = pd.to_datetime(df['Start Time']) 
            
            # Adding new columns like months and day_of_week which extracted from Start Time
            df['month'] = df['Start Time'].dt.month
            
            # Adding new columns like months and day_of_week which extracted from Start Time
            df['day_of_week'] = df['Start Time'].dt.day_name()
            
            # Adding new columns like months and day_of_week which extracted from Start Time
            df['start_hour'] = df['Start Time'].dt.hour
            
            
            # Filtering data frame according to user inputs
            months = ['january','february','march','april','may','june','july','august','semptember','october','november','december']
            
            # Filtering months by converting months(text) to numbers
            if (month.lower() != 'all'):
                df = df[df['month'] == months.index(month)+1]
            
            
            
            # Filtering days by starting capital letter
            if (day.lower() != 'all'):
                df = df[df['day_of_week'] == day.title()]  
            break
            
            
            
        except (KeyError,ValueError):
            # if there is a Key Error or Value Error by user, code bracnhes to get the user input again
            print("You have entered wrong city,month or day, please enter again !!!")
            city,month,day = get_filters()
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    popular_month =int(df['month'].mode())
    print("Most Common Month: " + str(popular_month))
    
    # TO DO: display the most common day of week
    popular_day_of_week = (df['day_of_week'].mode()).to_string(index=False, name=False, dtype=False)
    print("Most Common Day: " + popular_day_of_week)
    
    # TO DO: display the most common start hour
    popular_start_hour =int(df['start_hour'].mode())
    print("Most Common Start Hour: " + str(popular_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station =(df['Start Station'].mode()).to_string(index=False, name=False, dtype=False)
    print("Most Common Start Station: " + popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station =(df['End Station'].mode()).to_string(index=False, name=False, dtype=False)
    print("Most Common End Station: " + (popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    #if start or end station has more oocurance it only print the more occured one
    
    if ( df['Start Station'].value_counts()[0] > df['End Station'].value_counts()[0]):
        print("Most Common Start & End Station: " + (popular_start_station))
    
    elif ( df['Start Station'].value_counts()[0] < df['End Station'].value_counts()[0]):
        print("Most Common Start & End Station: " + (popular_end_station))
        
    #if they are equal both of them are printed, if it is the same station, print only one name
    else:
        print_variable = "Most Start & End Station: " + popular_start_station
        if(popular_start_station != popular_end_station):
            print_variable += ("and " + popular_end_station)
        print(print_variable)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =int(df['Trip Duration'].sum())
    print("Most Common Total Travel Time: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time =int(df['Trip Duration'].mean())
    print("Most Common Mean Travel Time: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    try:
        # TO DO: Display counts of user types
        print("User Type Counts: " + (df['User Type'].value_counts()).to_string(index=True, name=False, dtype=False))
        # TO DO: Display counts of gender
        print("Gender Counts: " + str(df['Gender'].value_counts()))
        
    except KeyError:
        # if there is a Key Error or Value Error by user, code bracnhes to get the user input again
        print("User Type or Gender can not be founded in this filter!!!")
        
    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = 5000.0
        for i in df['Birth Year']:
            if i < earliest_year:
                earliest_year = i
        most_recent_year =0.0        
        for i in df['Birth Year']:
            if i > most_recent_year:
                most_recent_year = i
                
        most_common = df['Birth Year'].mode()
        
        print("The Most Erliest Birth Year: " + str(earliest_year))
        print("The Most Recent Birth Year: " + str(most_recent_year))
        print("The Most Common Birth Year: " + (most_common).to_string(index=False, name=False, dtype=False))
        
    except KeyError:
        # if there is a Key Error or Value Error by user, code bracnhes to get the user input again
        print("Birth Year can not be founded in this filter!!!")
        
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
