
class GridBox:

  def _init_(self):
    self.lastNumber = None
    self.listParams = [1,2,3,4,5,6,7,8, 9]
            
  def setGridBox(self):
    self.listParams = random.sample(self.listParams, 9)
    indexGrid = 0
    indexList = 0


    while indexGrid < 3:
      print(f"{self.listParams[0+indexList]}|{self.listParams[1+indexList]}|{self.listParams[2+indexList]}")

      if indexGrid < 2:
        print("- - -")

      indexGrid += 1
      indexList += 3



    indexGrid = 0
    indexList = 0

    self.organize()
    print("")

    while indexGrid < 3:
      print(f"{self.listParams[0+indexList]}|{self.listParams[1+indexList]}|{self.listParams[2+indexList]}")

      if indexGrid < 2:
        print("- - -")
      
      indexGrid += 1
      indexList += 3
