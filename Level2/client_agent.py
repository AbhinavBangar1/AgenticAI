from fastmcp import Client
import asyncio


async def client_agent():
    async with Client("weather_mcp.py") as client :
        city = input("Enter the City : ")
        weather = await client.call_tool("Get Weather",{"city" : city})
        print(f"{weather.content[0].text}")

if __name__ == "__main__":
    asyncio.run(client_agent())