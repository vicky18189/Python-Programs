import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefing-room/statements-releases/")

# print(result.status_code)
# print(result.headers)


src = result.content
soup = BeautifulSoup(src, "html.parser")

urls = []
for h2 in soup.find_all("h2"):
    a = h2.find('a')
    urls.append(a['href'])

    print(urls)



# links = soup.find_all("a")
# print(links)
# print("\n")

# for link in links:
#     if "About" in link.text:
#         print(link)
#         print(link.attrs["href"])