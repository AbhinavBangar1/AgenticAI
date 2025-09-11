This repository contains 2 folder with following python scripts

1.Level 1 contains `llm_call.py` and `pdf_reader.py` .  
2.Level 2 conatins `weather_mcp.py` and `client_agent.py` .  
  
It also contains requirements for running the scripts  


## Script Description 

1.`llm_call.py` : A Streamlit chatbot which uses Google's llm model **GEMINI** .  
2.`pdf_reader.py` : Upload a PDF and extract its text .  
3.`weather_mcp.py` : Creates a mcp server using fastmcp library and provides the realtime weather of a city using OpenWeather's API .  
4.`client_agent.py` : mcp client to access the mcp server  

## Setup Instructions

1.Clone the repository
```bash
 git clone https://github.com/AbhinavBangar1/AgenticAI
```

2.Create a Virtual Environment 
```bash
python -m venv my_env
my_env\Scripts\activate 
```

3.Install Dependencies
```bash
pip install -r requirements.txt
```

4.Add environment variables  
create a file named .env in the root folder , in the folder add :  
GEMINI_API_KEY=your_gemini_api_key_here  
OpenWeather_API_key=your_openweather_api_key_here  


## Running the Scripts

1.llm_call.py
Run the Streamlit app to chat with google gemini using api:
```bash
streamlit run Level1/llm_call.py
```

2.pdf_reader.py
Run the Streamlit app to upload any PDF file and extract its text content:
```bash
streamlit run Level1/pdf_reader.py
```

3.weather_mcp.py
Start the MCP server 
```bash
fastmcp dev Level2/weather_mcp.py
```
4.client_agent.py
Run the MCP client to query weather from the server:
```bash
python Level2/client_agent.py
```


## Sample input outputs

1.Chatbot

**Input:**
```bash
tell me a interesting fact
```

**Output**
```bash
AI's response  

Here's one:
**Hummingbirds are the only bird species that can truly fly backward.** Their unique wing structure allows them to rotate their wings almost 180 degrees, giving them incredible agility, including hovering and even flying upside down for short bursts!'
```

2.PDF reader 

**Input:**
```bash
.\Level1\example_PDFs\data.pdf
```

**Output**
```bash
Text Extracted from PDF file

Example of Data Table 1 sample blue LED value green LED value red LED value clear water 97 19 79 blue water 73 11 13 green water 35 15 14 tea water 33 13 70     Example of Data Table 2 sample blue % transmitted green % transmitted red % transmitted clear water 97/97 = 100% 19/19 = 100% 79/79 = 100% blue water 73/97 = 75% 11/19 = 58% 13/79 = 17% green water 35/97 = 36% 15/19 = 79% 14/79 = 18% tea water 33/97 = 34% 13/19 = 68% 70/79 = 91%   Example of Measuring Ocean Color Graph 1 
   
Example of Data Table 3 sample blue LED value green LED value red LED value + 1 tsp milk 13 14 12 +1tsp milk + blue 10 9 6 +1tsp milk +green 9 13 7 +1tsp milk + tea 7 9 9     Example of Data Table 4 Water sample blue % transmitted green % transmitted red % transmitted + 1 tsp milk 13/13 = 100% 14/14 = 100% 12/12 = 100% +1tsp milk + blue 10/13 = 77% 9/14 = 64% 6/12 = 50% +1tsp milk +green 9/13 = 69% 13/14 = 93% 7/12 = 58% +1tsp milk + tea 7/13 = 54% 9/14 = 69% 9/12 = 75%   Example of Measuring Ocean Color Graph 2 '
```


3. MCP Server and Client

**Input:**
```bash
Enter the City: London
```

**Output**
```bash
According to Weather API , its Clouds , 15.46 degree celsius in London
```
