class Addres():

   def __init__(self, country="israel", city="bnai brak", street=None, num_house=None):
      self._country = country
      self._city = city
      self._street = street
      self._num_house = num_house

   @property
   def addres_details(self):
      return """country : %s, in city %s
              str. %s num. %d"""%(self._country, self._city, self._street, self._num_house)