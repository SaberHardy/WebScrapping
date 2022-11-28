from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)
html_bytes = page.read()

html_page = html_bytes.decode("utf-8")
start_title_index = html_page.find('title') + len("<title>")

end_title_index = html_page.find("</title>")

print(html_page)

print("The Title starting from: ", start_title_index)
print("The Title end in: ", end_title_index)

print(f"Page Title is: {html_page[start_title_index: end_title_index]}")
