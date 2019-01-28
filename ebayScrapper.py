import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def getData(url):
    r = requests.get(url)
    return r.text


def beautifyAndPresent(html):
    soup = BeautifulSoup(html, 'html.parser')
    i=0
    teste=""
    while 1:
        teste=soup.find(id="srp-river-results-listing"+str(i+1))
        if str(teste) == "None":
            break
        href=teste.find("a",{"class": "s-item__link"})
        print("##########################################################################")
        print("# Link: "+href["href"])
        print("# Title: "+teste.find("h3",{"class": "s-item__title"}).text)
        print("# State: "+teste.find("span",{"class": "SECONDARY_INFO"}).text)
        try:
            print("# Price: "+teste.find("span",{"class": "ITALIC"}).text)
        except AttributeError:
            print("# Price: unknown")
        print("# Shipping cost: "+teste.find("span",{"class": "s-item__shipping s-item__logisticsCost"}).text)
        print("# "+teste.find("span",{"class": "s-item__location s-item__itemLocation"}).text)
        print("##########################################################################")
        i=i+1
    print("Done! hope you find what tou looking for")
def main():
    try:
        numberPages = int(input('Enter number of pages (minimun and default is 1) : '))
    except ValueError:
        numberPages = 1
    if numberPages<=0:
        numberPages=1
    user_input = str(input("Enter what to search: "))
    if user_input=="":
        print("cannot be empty")
        return
    input_list = user_input.split(' ')
    print("Prices option:")
    print("0-none")
    print("1- Exact value")
    print("2- max price")
    print("3- min price")
    print("4- between to prices")
    try:
        priceopt = int(input('Enter number (0 by default): '))
    except ValueError:
        priceopt = 0
    if priceopt == 0:
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + input_list[0]
        for x in range(1, len(input_list)):
            url = url+"+"+input_list[x]

        url=url+"&_sacat=0&LH_TitleDesc=0&_pgn="
        print("Starting.....")
        for x in range(0, numberPages):
            link = url +str(x+1)
            html = getData(link)
            beautifyAndPresent(html)
    elif priceopt == 1:
        try:
            priceExact=float(input('Enter exact price: '))
        except ValueError:
            print("Something went wrong with price input")
            return
        if priceExact <=0:
            print("Price minor or equal to zero")
            return

        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + input_list[0]
        for x in range(1, len(input_list)):
            url = url+"+"+input_list[x]

        url=url+"&_sacat=0&rt=nc&_udlo="+str(priceExact)+"&_udhi="+str(priceExact)+"&_pgn="
        print("Starting.....")
        for x in range(0, numberPages):
            link = url +str(x+1)
            html = getData(link)
            beautifyAndPresent(html)
    elif priceopt == 2:     
        try:
            priceHigh=float(input('Enter high price: '))
        except ValueError:
            print("Something went wrong with price input")
            return
        if priceHigh <=0:
            print("Price is minor or equal to zero")
            return
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + input_list[0]
        for x in range(1, len(input_list)):
            url = url+"+"+input_list[x]

        url=url+"&_sacat=0&rt=nc&_udhi="+str(priceHigh)+"&_pgn="
        print("Starting.....")
        for x in range(0, numberPages):
            link = url +str(x+1)
            html = getData(link)
            beautifyAndPresent(html)
    elif priceopt == 3:
        try:
            priceLow=float(input('Enter low price: '))
        except ValueError:
            print("Something went wrong with price input")
            return
        if priceLow <=0:
            print("Price minor or equal to zero")
            return
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + input_list[0]
        for x in range(1, len(input_list)):
            url = url+"+"+input_list[x]

        url=url+"&_sacat=0&_udlo="+str(priceLow)+"&rt=nc&_pgn="
        print("Starting.....")
        for x in range(0, numberPages):
            link = url +str(x+1)
            html = getData(link)
            beautifyAndPresent(html)
    elif priceopt == 4:
        try:
            priceHigh=float(input('Enter max price: '))
            priceLow=float(input('Enter low price: '))
        except ValueError:
            print("Something went wrong with price input")
            return
        
        if priceHigh <= 0 or priceLow <= 0:
            print("Price cannot be minor or equal to zero")
            return
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + input_list[0]
        for x in range(1, len(input_list)):
            url = url+"+"+input_list[x]

        url=url+"&_sacat=0&_udhi="+str(priceHigh)+"&rt=nc&_udlo="+str(priceLow)+"&_pgn="
        print("Starting.....")
        for x in range(0, numberPages):
            link = url +str(x+1)
            html = getData(link)
            beautifyAndPresent(html)
    else:
        print("Insert a valid number!")
        return

if __name__ == "__main__":
    main()