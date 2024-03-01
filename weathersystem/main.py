from WeatherAppFunctions import collect_weather_data, \
    calculate_average, find_highest, find_lowest, present_results

from plot_data import plot_temperatures_freq, plot_temperatures_bar_chart


def main():
    temperatures = collect_weather_data()
    average = calculate_average(temperatures)
    highest = find_highest(temperatures)
    lowest = find_lowest(temperatures)
    present_results(average, highest, lowest)



if __name__ == "__main__":
    main()
