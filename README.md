## xml_parser
XML parser to parse XML documents and stores contents in a text file.  

### Description of Modules / Programs  
<pre>
pars = open(filename)                      Opening XML file from INPUT  
class Handler( xml.sax.ContentHandler )    Handles the particular tags and attributes of the XML Doc  
func startElement(self, tag, attributes)   Call when an element or tag starts  
func endElement(self, tag)                 Call when an elements ends  
func characters(self, content)             Call when a character is read  
os.startfile('parsed.txt')                 Open the file where parsed contents are stored : PARSED.txt  
</pre>

### Execution Screenshots
####1.  
![File Not Found](https://github.com/WillowXD/xml_parser/blob/master/Exec1.jpg)  
  
  
####2.  
![File Not Found](https://github.com/WillowXD/xml_parser/blob/master/Exec2.jpg)

### Conclusion
This code provides a simple and effective interface to parse XML documents
using Python Language and SAX Parsing Techniques.
The developed XML parser shows that the functional approach accomplishes
the task of parsing and validating XML by using fewer lines of code and
producing a very short and compact program in contrast to tiresome
languages.

