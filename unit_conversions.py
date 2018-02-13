class Length:

  __metric = {"mm" : 0.001,
              "cm" : 0.01,
              "m"  : 1, 
              "km" : 1000,
              "in" : 0.0254, 
              "ft" : 0.3048, 
              "yd" : 0.9144,
              "mi" : 1609.344}

  def __init__(self, value, unit = "m"):
    self.value = value
    self.unit = unit

  def convert_to_meters(self):
    return self.value * Length.__metric[self.unit]
    
  def __add__(self, other):
    # Add Length objects
    l = self.convert_to_meters() + other.convert_to_meters()
    return Length(l / Length.__metric[self.unit], self.unit)
    
  def __sub__(self, other):
    # Subtract Length objects 
    l = self.convert_to_meters() - other.convert_to_meters()
    return Length(1 / Length.__metric[self.unit], self.unit)

  def __mul__(self, other):
    # Multiply Length objects
    l = self.convert_to_meters() * other.convert_to_meters()
    return Length(1 / Length.__metric[self.unit], self.unit)

  def __truediv__(self, value, unit):
    # Divide Length objects
    l = self.convert_to_meters() / other.convert_to_meters()
    return Length(1 / Length.__metric[self.unit], self.unit)

  def __str__(self):
    return str(self.convert_to_meters())

  def __repr__(self):
    return "Length(" + str(self.value) + ", '" + self.unit + "')"


  # Accessor Methods
  def get_value(self):
    return self.value

  def get_unit(self):
    return self.unit

  # Mutator Methods
  def set_value(self, value):
    self.value = value

  def set_unit(self, unit):
    self.unit = unit