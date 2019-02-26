## xml_parser
XML parser to parse XML documents and stores contents in a text file.  

### Description of Modules / Programs  
pars = open(filename)                      Opening XML file from INPUT  
class Handler( xml.sax.ContentHandler )    Handles the particular tags and attributes of the XML Doc  
func startElement(self, tag, attributes)   Call when an element or tag starts  
func endElement(self, tag)                 Call when an elements ends  
func characters(self, content)             Call when a character is read  
os.startfile('parsed.txt')                 Open the file where parsed contents are stored : PARSED.txt  
