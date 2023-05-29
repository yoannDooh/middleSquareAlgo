def random(seed,nbDigit,nbRandomNumber):
    randomList = []
    randNumber = seed

    
    if (nbDigit%2 != 0 ):
        return "Le nombre de chiffre voulu doit être paire"
    
    for i in range (nbRandomNumber):        
        if (randNumber == 0): 
            randomList.append(f'Période atteint au bout de {len(randomList)+1} valeurs')
            return randomList
            
        randNumber = str ( randNumber**2 )
        randNumberLen = len(randNumber)
        
        while (randNumberLen< nbDigit ): 
            randNumber = '0'+randNumber

        if (randNumberLen%2!= 0 ):
            randNumber = '0'+randNumber
        
        randNumberLen = len(randNumber)
        indexStart= (randNumberLen-nbDigit)//2 
        randNumber= int ( randNumber[indexStart : indexStart+nbDigit] )

        randomList.append(randNumber)
        
        


                  
    return randomList


         
        
print ( random(564,4,25) )


        
        
        
        
        

     
    


     
      
        
