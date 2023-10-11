import requests
from bs4 import BeautifulSoup
import csv

csv_file = open("shoes.csv", 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Sub-Title', 'Price'])

source = requests.get('https://www.nike.com/in/w/mens-jordan-37eefznik1').text
section = BeautifulSoup(source, 'lxml')

for soup in section.find_all('div', class_='product-card__body'):
    title = soup.find('div', class_='product-card__title').text
    print(title)
    subtitle = soup.find('div', class_='product-card__subtitle').text
    print(subtitle)
    price = soup.find('div', class_='product-card__price').text
    price=price.split(' ')
    print(price[-1])
    csv_writer.writerow([title, subtitle, price[-1]])

