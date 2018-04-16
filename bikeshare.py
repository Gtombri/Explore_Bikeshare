#### Udacity Project: Explore US Bikeshare Data
#### Author: Gerrit Tombrink
#### Python Version 3.6

# Import packages
import pandas as pd
import sys
import time

# Import files of the different cities and replace strings with Pandas
try:
    df_chicago = pd.read_csv('chicago.csv')
    df_chicago.columns = df_chicago.columns.str.replace('\s+', '_')

    df_new_york_city = pd.read_csv('new_york_city.csv')
    df_new_york_city.columns = df_new_york_city.columns.str.replace('\s+', '_')

    df_washington = pd.read_csv('washington.csv')
    df_washington.columns = df_washington.columns.str.replace('\s+', '_')
except Exception:
    sys.exit("Please, insert the city-files into the directory of this file.")

# Insert variables for classification
month_val = -1
day_val = -1


# All functions for the calculation; they use the package Pandas

def get_city():
    '''This function asks the user for a city and returns the city for that city's bike share data.
    Args: none
    Returns: the name of the "city" as a str
    '''
    while True:
        try:
            city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                        'Would you like to see data for Chicago, New York, or Washington?\n').lower()
            if city == "chicago":
                print("You have chosen the city 'Chicago' and the filename 'chicago.csv'.")
                return(city)
            elif city == "new york":
                print("You have chosen the city 'New York' and the filename 'new_york_city.csv.'")
                return(city)
            elif city == "washington":
                print("You have chosen the city 'Washington' and the filename 'washington.csv.'")
                return(city)
            else:
                print("Please choose between Chicago, New York or Washington.")
        except KeyboardInterrupt:
            print("No input taken.")


def get_time_period():
    '''This function asks the user for a time period and returns the specified filter.
    Args: none
    Returns: the filter "time_period" as a str
    '''
    while True:
        try:
            time_period = input('\nWould you like to filter the data by month, day, or not at'
                                ' all? Type "none" for no time filter.\n').lower()
            if time_period == "month" or time_period == "day" or time_period == "none":
                print("You have chosen: {}".format(time_period))
                return time_period
            else:
                print("Please choose between month, day or none.")
        except KeyboardInterrupt:
            print("No input taken.")


def get_month():
    '''This function asks the user for a month and returns the specified month.
    Args: none
    Returns: the filter "month" as an int
    '''
    global month_val
    while True:
        try:
            month_val = int(input('\nWhich month? January, February, March, April, May, or June? Please type your response as an integer (1-6).\n'))
            if month_val <= 6 and month_val >= 1:
                print("You have chosen {}. month.".format(month_val))
                return month_val
            else:
                print("Please choose between January, February, March, April, May, or June.")
        except ValueError:
            print("That is not a valid number.")
        except KeyboardInterrupt:
            print("No input taken.")


def get_day():
    '''This function asks the user for a day and returns the specified day.
    Args: none
    Returns: the filter "day" as an int
    '''
    global day_val
    while True:
        try:
            day_val = int(input('\nWhich day? Please type your response as an integer (0-6).\n'))
            if day_val <=6 and day_val >= 0:
                print("You have chosen the day: {}.".format(day_val))
                return day_val
            else:
                print("That is a wrong week-number.")
        except ValueError:
            print("That is not a valid number.")
        except KeyboardInterrupt:
            print("No input taken.")


def popular_month(city, day_val):
    '''This function calculates the most popular month for start time.
    Args: city; choosed by the user input
    Returns: the most popular month as an int; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if day_val >= 0:
            day_in = city[city.Start_Time.dt.dayofweek == day_val]
            popular_month_result = day_in["Start_Time"].groupby(day_in.Start_Time.dt.month).count().idxmax()
            print("What is the most popular month for start time?")
            return ("It is: {}\n".format(popular_month_result))
        else:
            popular_month_result = city["Start_Time"].groupby(city.Start_Time.dt.month).count().idxmax()
            print("What is the most popular month for start time?")
            return("It is: {}\n".format(popular_month_result))
    except:
        print("Missing columns in table.\n")


def popular_day(city, month_val):
    '''This function calculates the most popular day of week for start time.
    Args: city, mont_val; choosed by the user input
    Returns: the most popular day of week as an int; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if month_val > 0:
            month_in = city[city.Start_Time.dt.month == month_val]
            popular_weekday = month_in["Start_Time"].groupby(month_in.Start_Time.dt.weekday_name).count().idxmax()
            print("What is the most popular day of week (Monday, Tuesday, etc.) for start time?")
            return ("It is: {}\n".format(popular_weekday))
        else:
            popular_weekday = city["Start_Time"].groupby(city.Start_Time.dt.weekday_name).count().idxmax()
            print("What is the most popular day of week (Monday, Tuesday, etc.) for start time?")
            return("It is: {}\n".format(popular_weekday))
    except:
        print("Missing columns in table.\n")


def popular_hour(city, day_val):
    '''This function calculates the most popular hour of day for start time.
    Args: city, mont_val; choosed by the user input
    Returns: the most popular hour of day as an int; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if day_val >= 0:
            day_in = city[city.Start_Time.dt.dayofweek == day_val]
            popular_hour = day_in["Start_Time"].groupby(day_in.Start_Time.dt.hour).count().idxmax()
            print("What is the most popular hour of day for start time?")
            return("It is: {}\n".format(popular_hour))
        else:
            popular_hour = city["Start_Time"].groupby(city.Start_Time.dt.hour).count().idxmax()
            print("What is the most popular hour of day for start time?")
            return("It is: {}\n".format(popular_hour))
    except:
        print("Missing columns in table.\n")


def trip_duration(city, month_val, day_val):
    '''This function calculates the total trip duration and average trip duration.
    Args: city, mont_val, day_val; choosed by the user input
    Returns: total and average trip duration in sec as a float; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if month_val > 0:
            month_in = city[city.Start_Time.dt.month == month_val]
            total_trip = month_in["Trip_Duration"].sum()
            aver_trip = month_in["Trip_Duration"].mean()
            print("What is the total trip duration and average trip duration?")
            return("The total trip duration of your chosen city is: {} seconds and the average trip duration of this city is: {} seconds.\n".format(total_trip, aver_trip))
        elif day_val >= 0:
            day_in = city[city.Start_Time.dt.dayofweek == day_val]
            total_trip = day_in["Trip_Duration"].sum()
            aver_trip = day_in["Trip_Duration"].mean()
            print("What is the total trip duration and average trip duration?")
            return("The total trip duration of your chosen city is: {} seconds and the average trip duration of this city is: {} seconds.\n".format(total_trip, aver_trip))
        else:
            total_trip = city["Trip_Duration"].sum()
            aver_trip = city["Trip_Duration"].mean()
            print("What is the total trip duration and average trip duration?")
            return("The total trip duration of your chosen city is: {} seconds and the average trip duration of this city is: {} seconds.\n".format(total_trip, aver_trip))
    except:
        print("Missing columns in table.\n")


def popular_stations(city, month_val, day_val):
    '''This function calculates the most popular start and end station.
    Args: city, mont_val, day_val; choosed by the user input
    Returns: most popular start and end station as a str; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if month_val > 0:
            month_in = city[city.Start_Time.dt.month == month_val]
            popular_start_station = month_in["Start_Station"].groupby(month_in.Start_Station).count().idxmax()
            popular_end_station = month_in["End_Station"].groupby(month_in.End_Station).count().idxmax()
            print("What is the most popular start station and most popular end station?")
            return ("The most popular start station of your chosen city is: {} and the most popular end station of this city is: {}.\n".format(popular_start_station, popular_end_station))
        elif day_val >= 0:
            day_in = city[city.Start_Time.dt.dayofweek == day_val]
            popular_start_station = day_in["Start_Station"].groupby(day_in.Start_Station).count().idxmax()
            popular_end_station = day_in["End_Station"].groupby(day_in.End_Station).count().idxmax()
            print("What is the most popular start station and most popular end station?")
            return ("The most popular start station of your chosen city is: {} and the most popular end station of this city is: {}.\n".format(popular_start_station, popular_end_station))
        else:
            popular_start_station = city["Start_Station"].groupby(city.Start_Station).count().idxmax()
            popular_end_station = city["End_Station"].groupby(city.End_Station).count().idxmax()
            print("What is the most popular start station and most popular end station?")
            return("The most popular start station of your chosen city is: {} and the most popular end station of this city is: {}.\n".format(popular_start_station, popular_end_station))
    except:
        print("Missing columns in table.\n")


def popular_trip(city, month_val, day_val):
    '''This function calculates the most popular trip.
    Args: city, mont_val, day_val; choosed by the user input
    Returns: most popular trip as a str; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if month_val > 0:
            city['COUNTER'] = 1
            month_in = city[city.Start_Time.dt.month == month_val]
            popular_trip = month_in.groupby(['Start_Station', 'End_Station'])['COUNTER'].sum().idxmax()
            print("What is the most popular trip?")
            return ("The most popular trip of your chosen city is: {}\n".format(popular_trip))
        elif day_val >= 0:
            city['COUNTER'] = 1
            day_in = city[city.Start_Time.dt.dayofweek == day_val]
            popular_trip = day_in.groupby(['Start_Station', 'End_Station'])['COUNTER'].sum().idxmax()
            print("What is the most popular trip?")
            return ("The most popular trip of your chosen city is: {}\n".format(popular_trip))
        else:
            city['COUNTER'] = 1
            popular_trip = city.groupby(['Start_Station', 'End_Station'])['COUNTER'].sum().idxmax()
            print("What is the most popular trip?")
            return ("The most popular trip of your chosen city is: {}\n".format(popular_trip))
    except:
        print("Missing columns in table.\n")


def users(city, month_val, day_val):
    '''This function calculates the counts of each user type.
    Args: city, mont_val, day_val; choosed by the user input
    Returns: counts of each user type as an int; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if month_val > 0:
            month_in = city[city.Start_Time.dt.month == month_val]
            count_user_type = month_in["User_Type"].groupby(month_in.User_Type).agg({"count"})
            print("What are the counts of each user type?")
            return ("The counts are:\n {}\n".format(count_user_type))
        elif day_val >= 0:
            day_in = city[city.Start_Time.dt.dayofweek == day_val]
            count_user_type = day_in["User_Type"].groupby(day_in.User_Type).agg({"count"})
            print("What are the counts of each user type?")
            return ("The counts are:\n {}\n".format(count_user_type))
        else:
            count_user_type = city["User_Type"].groupby(city.User_Type).agg({"count"})
            print("What are the counts of each user type?")
            return ("The counts are:\n {}\n".format(count_user_type))
    except:
        print("Missing columns in table.\n")


def gender(city, month_val, day_val):
    '''This function calculates the counts of gender.
    Args: city, mont_val, day_val; choosed by the user input
    Returns: counts of gender as an int; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if month_val > 0:
            month_in = city[city.Start_Time.dt.month == month_val]
            count_gender = month_in["Gender"].groupby(month_in.Gender).agg({"count"})
            print("What are the counts of gender?")
            return ("The counts are: {}\n".format(count_gender))
        elif day_val >= 0:
            day_in = city[city.Start_Time.dt.dayofweek == day_val]
            count_gender = day_in["Gender"].groupby(day_in.Gender).agg({"count"})
            print("What are the counts of gender?")
            return ("The counts are: {}\n".format(count_gender))
        else:
            count_gender = city["Gender"].groupby(city.Gender).agg({"count"})
            print("What are the counts of gender?")
            return ("The counts are: {}\n".format(count_gender))
    except:
        print("Missing columns in table.\n")


def birth_years(city, month_val, day_val):
    '''This function calculates the earliest, most recent and most popular birth years.
    Args: city, mont_val, day_val; choosed by the user input
    Returns: earliest, most recent and most popular birth years as an int; calculated with pandas
    '''
    try:
        city['Start_Time'] = pd.to_datetime(city['Start_Time'])
        if month_val > 0:
            month_in = city[city.Start_Time.dt.month == month_val]
            min_birth = month_in["Birth_Year"].groupby(month_in.Birth_Year).min().idxmin()
            max_birth = month_in["Birth_Year"].groupby(month_in.Birth_Year).max().idxmax()
            popular_birth = month_in["Birth_Year"].groupby(month_in.Birth_Year).count().idxmax()
            print("What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and most popular birth years?")
            return("The earliest birth year is {}, the most recent birth year is {} and the most popular birth year is {}.\n".format(min_birth, max_birth, popular_birth))
        elif day_val >= 0:
            day_in = city[city.Start_Time.dt.dayofweek == day_val]
            min_birth = day_in["Birth_Year"].groupby(day_in.Birth_Year).min().idxmin()
            max_birth = day_in["Birth_Year"].groupby(day_in.Birth_Year).max().idxmax()
            popular_birth = day_in["Birth_Year"].groupby(day_in.Birth_Year).count().idxmax()
            print("What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and most popular birth years?")
            return("The earliest birth year is {}, the most recent birth year is {} and the most popular birth year is {}.\n".format(min_birth, max_birth, popular_birth))
        else:
            min_birth = city["Birth_Year"].groupby(city.Birth_Year).min().idxmin()
            max_birth = city["Birth_Year"].groupby(city.Birth_Year).max().idxmax()
            popular_birth = city["Birth_Year"].groupby(city.Birth_Year).count().idxmax()
            print("What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and most popular birth years?")
            return("The earliest birth year is {}, the most recent birth year is {} and the most popular birth year is {}.\n".format(min_birth, max_birth, popular_birth))
    except:
        print("Missing columns in table.\n")


def display_data(city):
    '''This function displays five or more lines of data if the user specifies that they would like to.
    Args: city
    Returns: five or more lines of data as different types; calculated with pandas
    '''
    while True:
        try:
            display = input('\nWould you like to view individual trip data?'
                            ' Type \'yes\' or \'no\'.\n').lower()
            if display == "yes":
                lines = 5
                print(city.head(lines))
                while True:
                    display_2 = input('\nWould you like to see five more lines?'
                                      ' Type \'yes\' or \'no\'.\n').lower()
                    if display_2 == "yes":
                        lines += 5
                        print(city.head(lines))
                    elif display_2 == "no":
                        break
                    else:
                        print("Please choose between yes or no.\n")
                break
            elif display == "no":
                break
            else:
                print("Please choose between yes or no.\n")
        except KeyboardInterrupt:
            print("\nNo input taken.\n")


def statistics():
    '''This function opens the different functions and their calculation and prints out descriptive statistics specified by the user via raw input.
    Args: none
    Returns: none
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    if city == "chicago":
        city = df_chicago
    elif city == "new york":
        city = df_new_york_city
    elif city == "washington":
        city = df_washington

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    global month_val
    global day_val

    if time_period == "month":
        month_val = get_month()
    elif time_period == "day":
        day_val = get_day()

    # Start:
    # Print the results of each function and the time of calculation
    #

    print('\nCalculating the first statistic...\n')

    # Question: What is the most popular month for start time?
    if time_period == 'none' or time_period == 'day':
        start_time = time.time()
        print(popular_month(city, day_val))

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...\n")

    # Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        print(popular_day(city, month_val))

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...\n")

    start_time = time.time()

    # Question: What is the most popular hour of day for start time?
    print(popular_hour(city, day_val))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...\n")
    start_time = time.time()

    # Question: What is the total trip duration and average trip duration?
    print(trip_duration(city, month_val, day_val))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...\n")
    start_time = time.time()

    # Question: What is the most popular start station and most popular end station?
    print(popular_stations(city, month_val, day_val))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...\n")
    start_time = time.time()

    # Question: What is the most popular trip?
    print(popular_trip(city, month_val, day_val))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...\n")
    start_time = time.time()

    # Question: What are the counts of each user type?
    print(users(city, month_val, day_val))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...\n")
    start_time = time.time()

    # Question: What are the counts of gender?
    print(gender(city, month_val, day_val))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...\n")
    start_time = time.time()

    # Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    print(birth_years(city, month_val, day_val))

    print("That took %s seconds." % (time.time() - start_time))

    # End:
    # Print the results of each function and the time of calculation
    #

    # Open the the function display_data
    display_data(city)

    # Asks the user for restart
    while True:
        try:
            restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
            if restart == 'yes':
                statistics()
            elif restart == 'no':
                print("Goodbye!")
                break
            else:
                print("Please choose between yes or no.")
                continue
            break
        except:
            print("\nNo input taken.\n")

if __name__ == "__main__":
    statistics()