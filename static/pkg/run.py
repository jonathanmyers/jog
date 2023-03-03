import urllib.parse
from js import document
from pkg import abc2xml

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
  download("test.musicxml", xml_str)
