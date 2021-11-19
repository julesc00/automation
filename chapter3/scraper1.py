
import requests
from bs4 import BeautifulSoup


URL = "http://www.columbia.edu/~fdc/sample.html"

res = requests.get(URL)
page = BeautifulSoup(res.text, "html.parser")
link_section = page.find("h3", attrs={"id": "chars"})
section = []

for element in link_section.next_elements:
    if element.name == "h3":
        break
    section.append(element.string or "")

result = "".join(section)
print(result)
