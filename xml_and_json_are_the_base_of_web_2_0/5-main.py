from xml.dom import minidom
import json
from car import Car

'''copy originial JSON file content to new JSON file'''
json_file = open("5-main.json")
file_copy = json.load(json_file)
json_file.close()

'''arrays for cars and brands'''
cars = []
brands = []

'''initialize number of car doors'''
car_doors = 0

'''prepare DOM document and create root element'''
doc = minidom.Document()
all_cars = doc.createElement('cars')
doc.appendChild(all_cars)

for each in file_copy:
    objects = Car(each)
    cars.append(objects)
    if objects.get_brand() not in brands:
        brands.append(objects.get_brand())
    car_doors += objects.get_nb_doors()
    all_cars.appendChild(objects.to_xml_node(doc))

print len(brands)
print car_doors
print cars[3]
print doc.toxml(encoding = 'utf-8')
