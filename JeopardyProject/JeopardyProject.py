import requests
from bs4 import BeautifulSoup

game_id = 7792  # Replace with the desired game ID
url = f"http://www.j-archive.com/showgame.php?game_id={game_id}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

clues = soup.find_all("td", class_="clue")

print(soup.prettify())

for clue in clues:
    # Extract the question and answer
    question = clue.find("td", class_="clue_text").text
    answer = clue.find("em", class_="correct_response").text
    question_value = clue.find("td", class_="clue_value").text

    # Print the question and answer
    print("Question Value:", question_value)
    print("Question:", question)
    print("Answer:", answer)
    print()
import requests
from bs4 import BeautifulSoup

game_id = 7792  # Replace with the desired game ID
url = f"http://www.j-archive.com/showgame.php?game_id={game_id}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

clues = soup.find_all("td", class_="clue")

print(soup.prettify())

for clue in clues:
    # Extract the question and answer
    question = clue.find("td", class_="clue_text").text
    answer = clue.find("em", class_="correct_response").text
    question_value = clue.find("td", class_="clue_value").text

    # Print the question and answer
    print("Question Value:", question_value)
    print("Question:", question)
    print("Answer:", answer)
    print()
