import requests
from bs4 import BeautifulSoup

# Sending the GET request
url = requests.get("https://www.scrapethissite.com/pages/simple/")
if url == '400':
    print("Request send failed!")

# Making the soup for scrappe
soup = BeautifulSoup(url.text, "html.parser")
page_title = soup.find("h1")
print("Main page title: ", page_title.find(string=True).strip())

countries = []
# Using find with the CSS class to find the respective info about the country
country_names = soup.find_all("h3", class_="country-name")
country_capital = soup.find_all("span", class_="country-capital")
country_population = soup.find_all("span", class_="country-population")

# Since the result from the search above returns a list we use 'i' to get from that list
i = 0

# Basic for to iterate on all the countries/titles on page
for country_name in country_names:
    """
    Here we have a appending with the following information, {str(country_name.text).strip() which is the country name and the dict key, {"Capital": str(country_capital[i].text).strip(), "Population": str(country_population[i].text).strip()}}) which now we use 'i' to get from list like mentioned above and create a dictionary to use as the country info, i use strip because sometimes i get undesired spaces
    """
    countries.append({str(country_name.text).strip(): {"Capital": str(country_capital[i].text).strip(), "Population": str(country_population[i].text).strip()}})
    i += 1

for country in countries:
    for key, val in country.items():
        print(key, val)