from src.weather_report import WeatherReport
from src.weather_service import WeatherService
from src.location_service import LocationService


def print_weather_data_to_console(data, zipcode):
    city = data[0]
    state = data[1]
    min_temperature = data[2]
    max_temperature = data[3]
    condition = data[4]
    print("{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}".format(
        city, state, zipcode, min_temperature, max_temperature, condition).expandtabs(10))


def main():
    weather_report = WeatherReport()
    location_service = LocationService()
    weather_service = WeatherService()
    weather_report.set_location_service(location_service)
    weather_report.set_weather_service(weather_service)
    with open('zipcode_list.txt', 'r') as file:
        zipcode_list = file.read().splitlines()
        zipcode_dictionary = weather_report.get_all_data(zipcode_list)
        print("Weather data:")
        print("City\tState\tZipcode\tMin\tMax\tCondition".expandtabs(10))
        for zipcode in zipcode_list:
            print_weather_data_to_console(zipcode_dictionary[zipcode], zipcode)
        print("\nHottest city:")
        zipcode = weather_report.get_hottest_city(zipcode_list)
        city, state = zipcode_dictionary[zipcode][0], zipcode_dictionary[zipcode][1]
        print("{:s}\t{:s}\t{:s}".format(city, state, zipcode).expandtabs(10))
        print("\nColdest city:")
        zipcode = weather_report.get_coldest_city(zipcode_list)
        city, state = zipcode_dictionary[zipcode][0], zipcode_dictionary[zipcode][1]
        print("{:s}\t{:s}\t{:s}".format(city, state, zipcode).expandtabs(10))


if __name__ == '__main__':
    main()
