#Function
import datetime
from Speak import Say
from Listen import Listen
from bs4 import BeautifulSoup
import requests
import pywhatkit
import webbrowser as web
import webbrowser
from pywikihow import search_wikihow
#2 Types

#1 - Non Input
#eg: Time , Date , Speedtest

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Say("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Say("This May Also Help You Sir .")

def SolarBodies(body):

    url_2 = f"https://api.le-systeme-solaire.net/rest/bodies/{body}" 

    rrr = requests.get(url_2)

    Data_2 = rrr.json()

    mass = Data_2['mass'] ['massValue']

    volume = Data_2['vol'] ['volValue']

    density = Data_2['density']

    gravity = Data_2['gravity']

    escape = Data_2['escape']

    Say(f"mass of {body} is {mass}kilogram.")
    Say(f"gravity of {body} is {gravity}meter per second square.")
    Say(f"volume of {body} is {volume}cubic meter.")
    Say(f"density of {body} is {density}kilogram per cubic meter.")
    Say(f"speed of {body} is {escape}meter per second .")    

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

#2 - Input
#eg - google search , wikipedia

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        import pywhatkit
        pywhatkit.search(query)

    elif 'Flipkart' in tag:
        webbrowser.open("https://www.flipkart.com/")

    elif 'Amazon' in tag:
        webbrowser.open("https://www.amazon.in/?ie=UTF8&ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_CjwKCAjwos-HBhB3EiwAe4xM906wUSE4-7dXCE24o0a8-IbAVv7_PQAg0FzkH9Rsiy2xAX17b_a-XRoChXgQAvD_BwE_k_&ext_vrnc=hi&gclid=CjwKCAjwos-HBhB3EiwAe4xM906wUSE4-7dXCE24o0a8-IbAVv7_PQAg0FzkH9Rsiy2xAX17b_a-XRoChXgQAvD_BwE")    
        
    elif 'how to' in tag:

        max_result = 1

        how_to_func = search_wikihow(query=tag,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Say(how_to_func[0].summary) 

    elif 'temperature' in tag:
        search = "temperature in Baramati"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Say(f"{temperature} ")
        Say("Do I Have To Tell You Another Place Temperature ?")
        next = Listen()

        if 'yes' in next:
            Say("Tell Me The Name Of tHE Place ")
            name = Listen()
            search = f"{name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Say(f"{name} is {temperature} ")

        else:
            Say("no problem sir")

    elif "YouTube search" in tag:
        Query = query.replace("jarvis","")
        query = Query.replace("YouTube search","")
        YouTubeSearch(query)       
        
    elif "solar system" in tag:
        Say('Tell me the name of planet')
        bod = Listen()
        planet=bod.replace(" ","")
        body=planet.replace(" ","") 
        Body= str(body)
        SolarBodies(body=Body)        
