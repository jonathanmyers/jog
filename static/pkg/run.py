from js import document
from pkg import abc2xml
import xml.etree.ElementTree as ET

def getAndReturnText()-> str:
 abctext = document.getElementById("abcinput")
 return abctext.value

def download(filename, text):
 element = document.createElement('a')
 element.setAttribute('href', 'data:text/plain;charset=utf-8,' + text)
 element.setAttribute('download', filename)
 element.style.display = 'none'
 document.body.appendChild(element)
 element.click()
 document.body.removeChild(element)

def convert():
  text = getAndReturnText()
  xml = abc2xml.getXmlDocs(text)
  xml_str = abc2xml.fixDoctype(xml[0])
  title = get_title(xml_str)
  download(title, xml_str)

def get_title(xml):
  tree = ET.ElementTree(ET.fromstring(xml))
  root = tree.getroot()
  title = root.find("work/work-title")
  return title.text
