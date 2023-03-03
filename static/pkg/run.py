from js import document
import urllib.parse

def getAndReturnText()-> str:
 abctext = document.getElementById("abcinput")
 return abctext.value

def download(filename, text):
 element = document.createElement('a')
 element.setAttribute('href', 'data:text/plain;charset=utf-8,' + urllib.parse.quote_plus(text))
 element.setAttribute('download', filename)
 element.style.display = 'none'
 document.body.appendChild(element)
 element.click()
 document.body.removeChild(element)

def convert():
  text = getAndReturnText()
  download("test.musicxml", text)
