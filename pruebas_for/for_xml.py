#probando a hacer el for para sacar todos los datos del archivo xml

archivo_xml = pd.read_csv("./data_xml_clean.xml")
archivo_xml.head(4)

import xml.etree.ElementTree as ET

tree = ET.parse("data_xml_clean.xml")
root = tree.getroot()


edad = []
time = []
gender = []
index = []

for child in root:
    for subchild in child:
        if subchild.tag == "age":
            edad.append(subchild.text)
        elif subchild.tag == "time":
            time.append(subchild.text)
        elif subchild.tag == "gender":
            gender.append(subchild.text)
        elif subchild.tag == "index":
            index.append(subchild.text)
print(time)


    
# archivo_xml.to_csv("xml_csv.csv")
# archivo_xml.head()
