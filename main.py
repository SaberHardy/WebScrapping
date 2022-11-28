from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html_page = page.read().decode("utf-8")

print(html_page)

strings = ['Name: ', 'Hometown: ', 'Favorite animal: ', 'Favorite Color: ']

for string in strings:
    string_start_idx = html_page.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html_page[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html_page[text_start_idx: text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print('clean text: ', clean_text)
