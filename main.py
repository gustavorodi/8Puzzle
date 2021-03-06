import random
class GridBox:

  def __init__(self):
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

  def organize(self):

    while self.listParams != sorted(self.listParams):
      self.randomMatrix(self.listParams.index(9))
      
  def randomMatrix(self, position):

    if position == 0:
      possibleMovements = [1,3]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

    elif position == 1:
      possibleMovements = [0,2,4]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

    elif position == 2:
      possibleMovements = [1,5]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

    elif position == 3: 
      possibleMovements = [0,4,6]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

    elif position == 4:
      possibleMovements = [1,3,5,7]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

    elif position == 5:
      possibleMovements = [2,4,8]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

    elif position == 6:
      possibleMovements = [3,7]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

    elif position == 7:
      possibleMovements = [6,4,8]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

    else:
      possibleMovements = [5,7]
      if self.lastNumber in possibleMovements:
        possibleMovements.remove(self.lastNumber)

      newPosition = random.sample(possibleMovements,1)
      self.movement(position, newPosition[0])

  def movement(self, oldIndex, newIndex):

      paramSpaceTemp = self.listParams.pop(oldIndex)

      if 8 == newIndex:
        newIndex = newIndex - 1
      
      paramNumberTemp = self.listParams.pop(newIndex)

      self.listParams.insert(newIndex,paramSpaceTemp)
      self.listParams.insert(oldIndex,paramNumberTemp)

      self.lastNumber = newIndex



grid = GridBox()
grid.setGridBox()
