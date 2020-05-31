import requests
from bs4 import BeautifulSoup

def readCSV(filename):
    with open(filename) as file:
        links = [line.replace('\n', '') for line in file]
        return links

def writeCSV(prices):
    with open("out.txt", "w+") as file:
        for line in prices:
            file.write(line[0] + ", " + line[1] + '\n')
    pass

def scrape(link):
    rawHtml = requests.get(link).content
    soup = BeautifulSoup(rawHtml, 'html.parser')
    spans = soup.find_all('span', {'class': 'price'})
    return list(spans[0])[0]
    pass

def findPrices(links):
    return [[scrape(link), link] for link in links]

def main():
    filename = input("Name of csv of websites: ")
    links = readCSV(filename)
    prices = findPrices(links)
    writeCSV(prices)
    pass

if __name__ == "__main__":
    main()