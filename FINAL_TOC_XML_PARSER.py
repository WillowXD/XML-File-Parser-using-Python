import xml.sax                                                 #SAX (Simple API for XML) is an event-driven algorithm for parsing XML documents
import os                                                      #For opening parsed.txt
import re
import sys
from time import sleep                                         #Typewritter text
def tag(str,a):
    for i in range(a,len(str)):
        if  str[i]=='>' or str[i]=='"' or str[i]==' ' or str[i]=='=':
            break
    return i;
attr=[]
l=0
filename = input('Enter a file name: ')
pars = open(filename)   #Opening XML file from INPUT
parsed = open("attributes.txt","w+")    #Parsed Content of the XML Doc to be stored here
for str in pars.readlines():
    str=str.lstrip()
    if str[0]=='<':
        i=tag(str,1)
        if str[i]==' ':
            w=i
            j=tag(str,w+1)
            parsed.write(str[1:i].rstrip()+"\n"+str[w+1:j].rstrip()+"\n")
            #attr[1]=str[1:i]
        else:
            parsed.write(str[1:i]+"\n")
    else:
        print("\n\nSyntax Error !!!!")
        input()
        exit(0)
pars.close()
parsed.close()
pars = open("parsed.txt","w+")                                 #Parsed Content of the XML Doc to be stored here
parsed = open("attributes.txt","r")
parsed.readline().strip()
lis = [parsed.readline().strip()]
w='/'+lis[0]+'\n'
for q in parsed.readlines():
   if q==w:
      break
   else:
      lis.append(q[0:-1])
if len(lis)<8:
   for i in range(0,(8-len(lis))):
      lis.append("")
parsed.close()
parsed = open("attributes.txt","w")
parsed.seek(0)
parsed.truncate()
parsed.writelines(["%s\n" % item  for item in lis])
parsed.close()
class Handler( xml.sax.ContentHandler ):                       #Handles the particular tags and attributes of the XML Doc.
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   def startElement(self, tag, attributes):                    #Call when an element or tag starts
      self.CurrentData = tag                                   #Reads evey word of XML Doc
      if tag == lis[0]:
         print("\n\n")
         title = attributes[lis[1]]
         print (lis[1],"\t\t  :  ", title)
         pars.write("\n\n"+lis[1]+" : "+title+"\n")

   def endElement(self, tag):                                  #Call when an elements ends
      if self.CurrentData == lis[2]:
         print (lis[2],"\t\t  :  ", self.type)
         pars.write(lis[2]+" : "+self.type+"\n")
      elif self.CurrentData == lis[3]:
         print (lis[3],"\t\t  :  ", self.format)
         pars.write(lis[3]+" : "+self.format+"\n")
      elif self.CurrentData == lis[4]:
         print (lis[4],"\t\t  :  ", self.year)
         pars.write(lis[4]+" : "+self.year+"\n")
      elif self.CurrentData == lis[5]:
         print (lis[5],"\t\t  :  ", self.rating)
         pars.write(lis[5]+" : "+self.rating+"\n")
      elif self.CurrentData == lis[6]:
         print (lis[6],"\t\t  :  ", self.stars)
         pars.write(lis[6]+" : "+self.stars+"\n")
      elif self.CurrentData == lis[7]:
         print (lis[7],"  :  ", self.description + "\n")
         pars.write(lis[7]+" : "+self.description+"\n\n")
      self.CurrentData = " "

   def characters(self, content):                              #Call when a character is read
      if self.CurrentData == lis[2]:
         self.type = content
      elif self.CurrentData == lis[3]:
         self.format = content
      elif self.CurrentData == lis[4]:
         self.year = content
      elif self.CurrentData == lis[5]:
         self.rating = content
      elif self.CurrentData == lis[6]:
         self.stars = content
      elif self.CurrentData == lis[7]:
         self.description = content

  
if ( __name__ == "__main__"):
   parser = xml.sax.make_parser()
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)
   Handler = Handler()                                         #Initializes the above defined ContextHandler
   parser.setContentHandler( Handler )
   if filename[-4:]!=".xml":
      print("Not a valid XML Doc")
      exit();
   parser.parse(filename)                                      #Opening XML file from INPUT to PARSE
pars.close()
input()
print("_______________________________________________________________________________")
q=("\nPress Enter to open the Parsed File : " + pars.name + "\n")
for x in q:
   print(x,end='')
   sleep(0.01)
input()
for x in ("\nOPENING FILE : " + pars.name + "\n"):
   print(x,end='')
   sleep(0.009)
os.startfile('parsed.txt')                                     #Open the file where parsed contents are stored : PARSED.txt
