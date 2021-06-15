import requests
import difflib
import csv

userCity = input("Enter a city to see the weather for it: ").lower()

with open ('gb.csv', newline='') as csvfile:
    locations = csv.reader(csvfile, delimiter=',')
    mostAccuracteScore = 0
    mostLikelyCity = ""
    for row in locations:
        seq = difflib.SequenceMatcher(None,userCity,str(row).lower())
        d = seq.ratio()*100
        if d > mostAccuracteScore:
            mostAccuracteScore = d
            mostLikelyCity = str(row).lower()

print(f"Guess you meant {mostLikelyCity}?")

response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=853e425fd00c436c8c493818211306&q={mostLikelyCity}&aqi=no")
response = response.json()
#print(response)

print("in " + str(response['location']['name']) + " it is " + str(response['current']['temp_c']) + " ºC")