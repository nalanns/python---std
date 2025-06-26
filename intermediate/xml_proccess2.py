import xml.dom.minidom

# This script reads an XML file, processes it to extract and print details of each person,
# modifies the XML structure by adding a new person, and writes the modified XML back to the file.
# Parse the XML file
domtree = xml.dom.minidom.parse("intermediate/data.xml")
group = domtree.documentElement

# Extract the group element
persons = group.getElementsByTagName("person")

# Iterate through each person element and print their details
for person in persons:
    print("-----PERSON-----")
    if person.hasAttribute("id"):
        print("ID: {}".format(person.getAttribute("id")))
    
    # Extract and print the details of each person
    print("Name: {}".format(person.getElementsByTagName("name")[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName("age")[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName("weight")[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName("height")[0].childNodes[0].data))
    
# persons[2].getElementsByTagName("name")[0].childNodes[0].nodeValue = "New Name"
# persons[0].setAttribute("id", "1000")
# persons[3].getElementsByTagName("age")[0].childNodes[0].nodeValue = "-10"
# domtree.writexml(open("intermediate/data.xml", "w"))


# Adding a new person to the XML document
newperson = domtree.createElement("person")
newperson.setAttribute("id", "6")

# Create elements for the new person
name = domtree.createElement("name") 
name.appendChild(domtree.createTextNode("Paul Green"))

age = domtree.createElement("age") 
age.appendChild(domtree.createTextNode("22"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("70"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("175"))

# Append the new elements to the new person element
newperson.appendChild(name)
newperson.appendChild(age) 
newperson.appendChild(weight)
newperson.appendChild(height)

# Append the new person to the group element
group.appendChild(newperson)

# Write the modified XML back to the file
domtree.writexml(open("intermediate/data.xml", "w")) 

