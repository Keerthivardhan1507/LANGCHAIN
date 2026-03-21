import requests

#Wrather Tool

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return response.text
#Calculator Tool

def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Error in Calculation"