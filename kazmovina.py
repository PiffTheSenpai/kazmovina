import requests 
import time
from bs4 import BeautifulSoup


def pure_hate():

  url = "https://www.csfd.cz/film/1286545-onemanshow-the-movie/prehled/"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

  response = requests.get(url, headers=headers)
  #print(response.status_code)

  if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the elements that contain the information you want
    title_element = soup.find("div", class_="film-header-name")
    rating_element = soup.find("div", class_="film-rating-average")
    rating_person_element = soup.find("span", class_="counter")

    # Extract the text from the elements
    title = title_element.text.strip() if title_element else "Title not found"
    rating = rating_element.text.strip() if rating_element else "Rating not found"
    rating_person_element = rating_person_element.text.strip()[1:-1] if rating_person_element else "Rating person not found"

    # Print the extracted information
    print(title, "je stále mrdka a má:", rating, " na ČSFD od", rating_person_element, "lidi." )
    
  else:
    print("Rip dude, response code je:", response.status_code)


if __name__ == "__main__":
  while True:
    pure_hate()
    time.sleep(30)