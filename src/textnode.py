from enum import Enum

class TextType(Enum):
  NORMAL_TEXT = "normal"
  BOLD_TEXT = "bold"
  ITALIC_TEXT = "italic"
  CODE_TEXT = "code"
  LINK = "link"
  IMAGE = "image"

class TextNode(): 
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  # checks whether this node and another node is equal or not 
  def __eq__(self, other):
    if not isinstance(other, TextNode):
      return False
    
    return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    
  # returns a string representation of node
  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"