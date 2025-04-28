class HTMLnode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    # tag - string representing html tag name
    # value - string representing the value inside of html tag
    # children - list of HTMLnode objects representing children inside this node
    # props - dict of key value pairs representing attributes of html tags 

    self.tag = tag
    self.value = value 
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()

  def props_to_html(self):
    attributes = ""

    for key,value in self.props.items():
      attributes = attributes + f" {key}={value}"

    return attributes
  
  def __repr__(self):
    return f"""HTMLnode: 
    tag: {self.tag}
    value: {self.value}
    children: {self.value}
    props: {self.props}"""
