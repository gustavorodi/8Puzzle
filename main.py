def organize(self):
    while self.listParams != sorted(self.listParams):
      self.randomMatrix(self.listParams.index(9))
      
  def randomMatrix(self, position):
    
    if position == 0:
      possibleMovements = [1,3]
     
    elif position == 1:
      possibleMovements = [0,2,4]
     
    elif position == 2:
      possibleMovements = [1,5]
      
    elif position == 3: 
      possibleMovements = [0,4,6]
      
    elif position == 4:
      possibleMovements = [1,3,5,7]
      

    elif position == 5:
      possibleMovements = [2,4,8]
     

    elif position == 6:
      possibleMovements = [3,7]
     

    elif position == 7:
      possibleMovements = [6,4,8]
     

    else:
      possibleMovements = [5,7]
     
