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
    <li class="special mako-forever">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
parse = BeautifulSoup(html, "html.parser")
"""in order to select an elem of we can do the following:"""
data = parse.body.contents[1]  # that selects the entire body then add [1] to get the 1st elem
"""in order to select the contents of the body we jjust add the .CONTENTS  at the end"""
print(data)
"""we need to pay attention to the new line when printing a certain element - see file text"""
"""to get the inner text in the above example, we call .CONTENTS again, and that will give is the inner portion"""
data1 = parse.body.contents[1].contents
print(data1)
""" we can descend into the hierachy and navigate through the elements, from DIV  to OL, by calling NEXT_SIBLING
as they have the same level on the hierarchy, not embedded into one another"""
new_data = parse.body.contents[1].next_sibling.next_sibling  # called it twice because there was a new line
print(new_data)
""" we can select an element and find its parent as well and then keep moving up as shown next:"""
data2 = parse.select(".special")[0].parent.parent.parent
print(data2)
print('separator')
"""parse.find(class_ = "special).parent"""
"""next line is about using the search tags"""
finding = parse.find(id="first").find_next_sibling()
print(finding)
print('2nd separator')
"""next line is about finding the previous sibling"""
"""we will start by selecting <div data-example="yes">bye</div> from the code and then navigate up"""
finding_previous = parse.select("[data-example]")[1].find_previous_sibling().find_previous_sibling()
print(finding_previous)
print('3rd separator')
"""another thing we can do is that we can search by giving a string as an argument"""
"""<li class="special mako-forever">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li> like in this example:"""
finding_next = parse.find(class_="mako-forever").find_next_sibling(class_="special")
print(finding_next)
find_next = parse.select(".mako-forever")[0].find_next_sibling()  # or using the CSS selectors
print(find_next)
print('another separator')
"""this methods will actually search based of what you're looking for """
"""this will find the parent of the H3 element which is <div>"""
finding_parent = parse.find("h3").find_parent()
print(finding_parent)
print('last separator')
finding_parent_with_string = parse.find("p").find_parent("body")
print(finding_parent_with_string)
