class POI(object):
  def __init__(self,x,y,name):
    self.x=x
    self.y=y
    self.name=name
  def __str__(self):
    return "{x : "+str(self.x)+", y : "+str(self.y)+",name : "+str(self.name)+"}"