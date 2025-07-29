import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/marcusgoede/api/great-circle-mapper'

mcp = FastMCP('great-circle-mapper')

@mcp.tool()
def aircraft_type_read(icao_iata: Annotated[str, Field(description='ICAO 3 letter or IATA 2 letter code')]) -> dict: 
    '''get aircraft type data by IATA or ICAO code'''
    url = 'https://greatcirclemapper.p.rapidapi.com/aircraft/read/A388'
    headers = {'x-rapidapi-host': 'greatcirclemapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'icao_iata': icao_iata,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def air_route_calculation(route: Annotated[str, Field(description='ICAO airport cides, separated by hyphens')],
                          speed: Annotated[str, Field(description='Speed in kts')]) -> dict: 
    '''calculate distance and flight time for any airports and any speed'''
    url = 'https://greatcirclemapper.p.rapidapi.com/airports/route/EGLL-KJFK/510'
    headers = {'content-type': 'text/html;charset=UTF-8', 'vary': 'Accept-Encoding', 'x-rapidapi-host': 'greatcirclemapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'route': route,
        'speed': speed,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def airport_search(query: Annotated[str, Field(description='ICAO code, IATA code, town, airport name')]) -> dict: 
    '''get a list of airport records'''
    url = 'https://greatcirclemapper.p.rapidapi.com/airports/search/Cologne'
    headers = {'x-rapidapi-host': 'greatcirclemapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def airport_read(icao_iata: Annotated[str, Field(description='ICAO code or IATA code')]) -> dict: 
    '''get airport by IATA code or ICAO code'''
    url = 'https://greatcirclemapper.p.rapidapi.com/airports/read/KSFO'
    headers = {'x-rapidapi-host': 'greatcirclemapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'icao_iata': icao_iata,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
