import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("Hi, my name is Andy", TextType.BOLD_TEXT)
    node2 = TextNode("Hi, my name is Andy", TextType.BOLD_TEXT)

    self.assertEqual(node, node2)

  def test_not_eq(self):
    node = TextNode("Hi, my name is Andy", TextType.BOLD_TEXT)
    node2 = TextNode("Hi my name is Andy", TextType.ITALIC_TEXT)

    self.assertNotEqual(node, node2)

  def test_text(self):
    node = TextNode("Hello World", TextType.BOLD_TEXT)
    node2 = TextNode("World Hello", TextType.BOLD_TEXT)
    node3 = TextNode("Hello World", TextType.BOLD_TEXT)

    self.assertEqual(node, node3)
    self.assertNotEqual(node, node2)

  def test_text_type(self):
    node = TextNode("Hello World", TextType.ITALIC_TEXT)
    node2 = TextNode("Hello World", TextType.BOLD_TEXT)
    node3 = TextNode("Hello World", TextType.ITALIC_TEXT)
    node4 = TextNode("Hello World", TextType.ITALIC_TEXT)

    self.assertNotEqual(node, node2)
    self.assertEqual(node3, node4)

  def test_link(self):
    node = TextNode("Hello World", TextType.BOLD_TEXT, "google.com")
    node2 = TextNode("World Hello", TextType.BOLD_TEXT, "gmail.com")
    node3 = TextNode("Hello World", TextType.BOLD_TEXT, "google.com")

    self.assertEqual(node, node3)
    self.assertNotEqual(node, node2)

if __name__ == "__main__":
  unittest.main()