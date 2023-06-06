#import requests/beautifulSoup library
import requests
from bs4 import BeautifulSoup

#Create url for the episode desired to pull
game_id = 7792  # Replace with the desired game ID
url = f"http://www.j-archive.com/showgame.php?game_id={game_id}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

clues = soup.find_all("td", class_="clue")
final = soup.find("table" , class_= "final_round")
print("\n\n\n")
print( len( clues ) )
print("\n\n\n")

#
#print(soup.prettify())


"""for clue in clues:
    # Extract the question and answer
    question = clue.find("td", class_="clue_text").text
    answer = clue.find("em", class_="correct_response").text
    question_value = clue.find("td", class_="clue_value").text

    # Print the question and answer
    print("Question Value:", question_value)
    print("Question:", question)
    print("Answer:", answer)
    print()
"""
iterationNumber = 0
for clue in clues:
  if( iterationNumber == 60) :
    break

  # Extract the question and answer
  
  question = clue.find("td", class_="clue_text")

  if ( question == None ) :
    question = None
    answer = None
    question_value = None
  else :
    question = clue.find("td", class_="clue_text").text
    answer = clue.find("em", class_="correct_response").text
    if ( None != clue.find("td", class_="clue_value_daily_double") ):
      question_value = "Daily Double"
    elif ( None != clue.find("td", id_="clue_FJ")): 
      question_value = "Final Jeopardy"
    else:
      question_value = clue.find("td", class_="clue_value").text
    
  # Print the question and answer
  print("Question Value:", question_value)
  print("Question:", question)
  print("Answer:", answer)
  print()
  iterationNumber += 1

question = final.find("td", class_="clue_text").text
answer = final.find("em", class_="correct_response").text

print("Final Jeopardy")
print("Question:", question)
print("Answer:", answer)
print()