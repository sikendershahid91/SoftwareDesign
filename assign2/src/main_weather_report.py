from weather_report import WeatherReport
from weather_service import WeatherService
from location_service import LocationService
import sys


def print_zipcode_and_city_state(zipcode, location_data, end = '\n'):
    city, state = location_data
    print("{:<20}{:<10}{:<10}".format(city, state, zipcode), end = end)


def print_weather_data(weather_data):
    min_temperature, max_temperature, condition = weather_data
    print(("{:<10}{:<10}{:s}"
        .format(min_temperature, max_temperature, condition)))


def print_zipcode_data_to_console(zipcode, location_data, weather_data):
    print_zipcode_and_city_state(zipcode, location_data, end = '')
    print_weather_data(weather_data)


def sorted_zipcode_by_city(zipcode_list, location_dictionary):
    zipcode_list.sort(key = lambda zipcode: location_dictionary[zipcode][0])
    return zipcode_list


def main():
    weather_report = WeatherReport()

    weather_report.set_location_service( LocationService() )
    weather_report.set_weather_service( WeatherService() )

    with open(sys.path[0] + '/zipcode_list.txt', 'r') as file:
        zipcode_list = file.read().splitlines()

    location_dictionary = weather_report.get_cities_and_state(zipcode_list)
    weather_dictionary = weather_report.get_weather_data(zipcode_list)

    print("Weather data:")
    print("City\t\tState\tZipcode\tMin\tMax\tCondition".expandtabs(10))

    zipcode_list = sorted_zipcode_by_city(zipcode_list, location_dictionary)

    for zipcode in zipcode_list:
        print_zipcode_data_to_console(
            zipcode,
            location_dictionary[zipcode],
            weather_dictionary[zipcode])

    print("\nHottest city:")
    zipcode = weather_report.get_hottest_zipcode(weather_dictionary)
    print_zipcode_and_city_state(zipcode, location_dictionary[zipcode])

    print("\nColdest city:")
    zipcode = weather_report.get_coldest_zipcode(weather_dictionary)
    print_zipcode_and_city_state(zipcode, location_dictionary[zipcode])


if __name__ == '__main__':
    main()
