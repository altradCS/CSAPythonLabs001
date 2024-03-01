
def collect_weather_data():
    temperatures = []  # List to store the temperatures
    print("Enter daily temperatures (type 'done' to finish):")
    while True:
        temp = input("> ")
        if temp.lower() == 'done':
            break
        try:
            temperatures.append(float(temp))
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")
    return temperatures


def calculate_average(temperatures):
    if temperatures:
        return sum(temperatures) / len(temperatures)
    else:
        return 0

def find_highest(temperatures):
    return max(temperatures) if temperatures else None

def find_lowest(temperatures):
    return min(temperatures) if temperatures else None


def present_results(average, highest, lowest):
    print("\nWeather Analysis Results:")
    print(f"Average Temperature: {average:.2f}")
    print(f"Highest Temperature: {highest}")
    print(f"Lowest Temperature: {lowest}")

