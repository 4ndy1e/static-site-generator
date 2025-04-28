from textnode import TextNode, TextType
from htmlnode import HTMLnode

def main():
  testNode = TextNode("This is some anchor text", "link", "https://www.boot.dev")
  print(testNode)

  props = { 
    "href": "https://www.google.com",
    "target": "_blank",
  }

  testHTMLnode = HTMLnode("p", "Hello World", props=props)
  print(testHTMLnode)
  print(testHTMLnode.props_to_html())
  
main()