from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

"""first we have to initialize beautiful soup by writing the following and parse the HTML """
soup_dejour = BeautifulSoup(html, "html.parser")
# print(soup_dejour)
# print(type(soup_dejour))
# """ we can nw use methods from within"""
# print(soup_dejour.body)
# print(soup_dejour.body.div)  # this will only orint the first DIV , if we the other we have to use the find all
d = soup_dejour.find_all('li')
print(d)
"""we can print based of id when we have a tag with id"""
c = soup_dejour.find(id='first')
c1= soup_dejour.select("#first")
print(c1[0])

""" we can print based of a class as well only we have to use the underscore after class so as not to be confused
with a Python class."""
b = soup_dejour.find_all(class_='special')
b1 = soup_dejour.select(".special")
print(b1[0])
"""we can also select based of attributes, and then we type ATTRS and colon and write the data as a dictionary 
in the exact way we find it in the HTML code as in the example bellow"""
a = soup_dejour.find(attrs={'data-example': 'yes'})
a1= soup_dejour.select("[data-example]")
print(a1)
print(a)
