import sys
import requests
import mysql.connector
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="buscalibre"
)

mycursor = mydb.cursor()
num = 1
URL = sys.argv[1]


while(True):
	pageNum = "?page=" + str(num)
	num += 1
	page = requests.get(URL+pageNum)
	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find_all("div", class_="producto")
	if results == []:
		break
	for libro in results:
		titulo = libro.find("div", class_="nombre")
		precio = libro.find("h3", class_="precio-ahora")
		precio = precio.text.replace("$", "")
		precio = precio.replace(".", "")
		precio = precio.strip()
		autor = libro.find("div", class_="autor")

		sql = "INSERT INTO libro (titulo, autor, precio) VALUES (%s, %s, %s)"
		val = (titulo.text, autor.text, precio)
		mycursor.execute(sql, val)

		mydb.commit()

		print(mycursor.rowcount, "record inserted.")

		print(titulo.text, "-", precio, "-", autor.text)
