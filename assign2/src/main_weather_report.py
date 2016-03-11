from weather_report import WeatherReport
from weather_service import WeatherService
from location_service import LocationService
import sys


def print_weather_data_to_console(zipcode, location_data, weather_data):
    city, state = location_data
    min_temperature, max_temperature, condition = weather_data

    print(("{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}"
        .format(city, state, zipcode, min_temperature, max_temperature, condition)
        .expandtabs(10)))


def main():
    weather_report = WeatherReport()

    weather_report.set_location_service( LocationService() )
    weather_report.set_weather_service( WeatherService() )

    with open(sys.path[0] + '/zipcode_list.txt', 'r') as file:
        zipcode_list = file.read().splitlines()

    location_dictionary = weather_report.get_cities_and_state(zipcode_list)
    weather_dictionary = weather_report.get_weather_data(zipcode_list)

    print("Weather data:")
    print("City\tState\tZipcode\tMin\tMax\tCondition".expandtabs(10))

    for zipcode in zipcode_list:
        print_weather_data_to_console(
            zipcode,
            location_dictionary[zipcode],
            weather_dictionary[zipcode])

    print("\nHottest city:")
    zipcode = weather_report.get_hottest_zipcode(weather_dictionary)
    city, state = location_dictionary[zipcode]
    print("{:s}\t{:s}\t{:s}".format(city, state, zipcode).expandtabs(10))

    print("\nColdest city:")
    zipcode = weather_report.get_coldest_zipcode(weather_dictionary)
    city, state = location_dictionary[zipcode]
    print("{:s}\t{:s}\t{:s}".format(city, state, zipcode).expandtabs(10))


if __name__ == '__main__':
    main()
