from src.api.weather_api import get_weather

api_key = "b88b7e287ecb2ec96beb7e53ca0fc46b"
cities = ["Kyiv", "Odesa", "Lviv", "Dnipro"]

def main():

    print("Select a city:")
    for index, city in enumerate(cities, start=1):
        print(f"{index}. {city}")

    choice = int(input("Enter your choice (1-3): "))

    if 1 <= choice <= len(cities):
        city_name = cities[choice - 1]
        get_weather(city_name, api_key)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
