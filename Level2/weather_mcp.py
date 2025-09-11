import requests
import os 
from dotenv import load_dotenv
from fastmcp import FastMCP #using fastmcp library to create a MCP server

load_dotenv()
api_key = os.getenv("OpenWeather_API_key")
#print(api_key)

mcp = FastMCP("Get Weather")        # creating a MCP server

@mcp.tool(name = "Get Weather" , description = "Give weather of the given city")
def getWeather(city : str) -> str:
    # city = input("Enter the city : ")
    api_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(api_URL)
    # print("Statut code : ",response.status_code)
    if response.status_code != 200:
        return f"Couldn't fetch weather for {city}. Please check the city name."
    data=response.json()
    Weather = data["weather"][0]["main"].capitalize()
    Temp = data["main"]["temp"]
    # print("Weather Description : ",response.text)
    # print("*" * 60)
    # print("\n")
    # print("Weather : " , Weather)
    # print("Temperature : ", Temp)
    # return f"Temperature of {city} is {round((Temp - 273.15),2)} degree celsius and weather being {Weather}"
    return f"According to Weather API , its {Weather} , {round((Temp - 273.15),2)} degree celsius in {city}"

if __name__ == "__main__":
    mcp.run()




