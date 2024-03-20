from bs4 import BeautifulSoup
import requests
import csv
import sys

def scrap(n):
    id = str(n)
    url = "https://nethnews.lk/article/" + id
    print(url)

    # get html content from the url
    try:
        r = requests.get(url)
        data = r.text
    except requests.RequestException as e:
        print("An error occurred while fetching the webpage:", e)
        return

    # parse with BS
    soup = BeautifulSoup(data, "lxml")

    # get title
    h1s = soup.find_all('h1')
    if len(h1s) < 1:
        print("Title not found for ID:", id)
        return None

    title = h1s[0].get_text()
    print("Title:", title)

    # get date and time
    date = soup.find_all("time", {"class": "entry-date"})
    if len(date) < 1:
        print("An error occurred! Date not found.")
        return None
    date = date[0].get_text()
    print("Date:", date)
    return title, date

# Define CSV filename
csv_filename = "scraped_data.txt"

# scrap news items by id (from 111200 to 111300)
start_id = 111200
end_id = 111300

# Open CSV file for writing
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Title', 'Date'])

    for n in range(start_id, end_id + 1):
        result = scrap(n)
        if result is None:
            continue
        csv_writer.writerow(result)
        print("\n===============================\n\n")

print("Data saved to", csv_filename)
