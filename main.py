from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)
html_bytes = page.read()

html_object = html_bytes.decode("utf-8")
title_index = html_object.find('title') + len("<title>")

print(html_object)
print(title_index)
