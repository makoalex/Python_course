from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class = "special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special mako_forever">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
"""initialising beautiful soup and parsing html"""
data = BeautifulSoup(html, "html.parser")
elem = data.select(".special")[0]  # we get the first elem of the list instance of an element class
elem1 = elem.get_text() # this syntax helps us get the text only from the first object.
print(elem1)
"""to simply we can also do this:"""
for el in data.select(".special"):
    print(el.get_text())
"""we can also use .NAME which is a not a method, and refers to the name of the tag"""
"""for every tag that has the class special in it """
for i in data.select(".special"):
    print(i.name)
    """we can laos use .ATTRS and this is a dictionary containing key value pairs for the elem inside the class"""
    print(i.attrs)
    """ some can be a list as elements can have more than one class"""
