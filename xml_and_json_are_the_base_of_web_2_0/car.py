import json

class Car:
    def __init__(self, *args, **kwargs):
        '''initialization'''
        if len(args) > 0 and isinstance(args[0], dict):
            name = args[0].get('name')
            brand = args[0].get('brand')
            nb_doors = args[0].get('nb_doors')

        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        '''error handling'''
        if name == "" or not isinstance(name, basestring):
            raise Exception("name is not a string")
        if brand == "" or not isinstance(brand, basestring):
            raise Excpetion("brand is not a string")
        if type(nb_doors) != int or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")

        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    '''Getters'''
    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_nb_doors(self):
        return self.__nb_doors

    def set_nb_doors(self, number):
        self.__nb_doors = number

    ''' return a string in JSON format'''
    def to_json_string(self):
        return json.dumps(self.to_hash())

    ''' return a DOM element'''
    def to_xml_node(self, doc):
        car = doc.createElement('car')

        car.setAttribute('nb_doors', str(self.__nb_doors))

        name = doc.createElement('name')
        nameInfo = doc.createCDATASection(self.__name)
        name.appendChild(nameInfo)
        car.appendChild(name)

        brand = doc.createElement('brand')
        brandInfo = doc.createTextNode(self.__brand)
        brand.appendChild(brandInfo)
        car.appendChild(brand)

        return car

    '''return a dictionary data structure'''
    def to_hash(self):
        return {'name': self.__name, 'brand': self.__brand, 'nb_doors': self.__nb_doors}

    '''return a string with the car info'''
    def __str__(self):
        return "%s %s (%s)" % (self.__name, self.__brand, self.__nb_doors)
