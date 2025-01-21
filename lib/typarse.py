#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv

def parse(ville):
    url = 'http://www.tyzicos.com/ville-concerts/'+ville

    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all concert entries
    concerts = []
    concert_rows = soup.find_all("div", class_="row concert-ctn")

    for row in concert_rows:
        # Extract details for each concert
        date_section = row.find_previous("div", class_="date")  # Look for the associated date
        day_name = date_section.find("span", class_="day-name").text.strip() if date_section else ""
        day_num = date_section.find("span", class_="day-num").text.strip() if date_section else ""
        month = date_section.find("span", class_="month").text.strip() if date_section else ""
        year = date_section.find("span", class_="year").text.strip() if date_section else ""
        date = f"{day_name} {day_num} {month} {year}"

        concert_name = row.find("span", class_="titre").text.strip() if row.find("span", class_="titre") else ""

        lieu = row.find("div", class_="lieu")
        lieu_name = lieu.find("a").text.strip() if lieu and lieu.find("a") else ""

        ville = row.find("div", class_="ville")
        ville_name = ville.find("a").text.strip() if ville and ville.find("a") else ""

        heure = row.find("div", class_="heure").text.strip() if row.find("div", class_="heure") else ""

        prix = row.find("div", class_="prix").text.strip() if row.find("div", class_="prix") else ""

        # Append extracted data to the list
        concerts.append({
            "Date": date,
            "Concert": concert_name,
            "Lieu": lieu_name,
            "Ville": ville_name,
            "Heure": heure,
            "Prix": prix
        })

    return concerts