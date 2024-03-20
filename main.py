from bs4 import BeautifulSoup
import requests
import sys


def scrap(n):
    id = str(n)
    url = "https://nethnews.lk/article/" + id
    print(url)

    # get html content from the url
    r = requests.get(url)
    data = r.text


    # parse with BS
    soup = BeautifulSoup(data, "lxml")

    # get title
    h1s = soup.find_all('h1')
    #print(h1s)

    # if title not found, stop the execution
    if len(h1s) < 1:
        print("An error occurred!")
        return

    title = h1s[0].get_text()
    print(title)
    #print(title.encode('utf8'))

    # get date and time
    date = soup.find_all("time", {"class": "entry-date"})
    if len(date) < 1:
        print("An error occurred!")
        return
    date = date[0].get_text()
    print(date)
    #print(date.encode('utf8'))

    # get article content
    contents = soup.find_all("div", {"class": "td-post-content"})
    contents = contents[0].get_text()
    print(contents)

    # Open file in write mode
    with open("doc/neth_" + id + ".txt", "w", encoding="utf-8") as file:
        file.write("<title>" + title + "</title>\n")
        file.write("<time>" + date + "</time>\n")
        file.write("<author></author>\n")
        file.write("<body>" + contents + "</body>")


# scrap news items by id (from 510500 to 512500)
for n in range(111200, 111282):
    scrap(n)
    print("\n===============================\n\n")
