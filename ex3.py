def percent_to_gpv(percent):      
   '''(int)->float
       Takes a percentage (int) and then returns the gpa (float)
       REQ: grade>=0
       >>>percent_to_gpv(90)
       4.0
       >>>percent_to_gpv(84)
       3.7
       >>>percent_to_gpv(78)
       3.3
       >>>percent_to_gpv(73)
       3.0
       >>>percent_to_gpv(72)
       2.7
       >>>percent_to_gpv(68)
       2.3
       >>>percent_to_gpv(65)
       2.0
       >>>percent_to_gpv(60)
       1.7
       >>>percent_to_gpv(57)
       1.3
       >>>percent_to_gpv(54)
       1.0
       >>>percent_to_gpv(50)
       0.7
       >>>percent_to_gpv(49)
       0.0
       '''   
 #Percent must be an int in the range of 0-100
 #user enters a value less than 49 returns gpa of 0.
   if(49>=percent>=0):
      result=0.0
      return (result)
    #user enters a value between than 50 and 52 returns gpa of 0.7
   elif(52>=percent>=50):
      result = 0.7            
      return (result)
   #user enters a value between than 53 and 56 returns gpa of 1
   elif(56>=percent>=53):
      result = 1.0            
      return (result)  
   #user enters a value between than 57 and 59 returns gpa of 1.3
   elif(59>=percent>=57):
      result = 1.3            
      return (result)  
   #user enters a value between than 60 and 62 returns gpa of 1.37   
   elif(62>=percent>=60):
      result = 1.7            
      return (result)  
    #user enters a value between than 64 and 66 returns gpa of 2.0
   elif(66>=percent>=63):
      result = 2.0            
      return (result)  
    #user enters a value between than 67 and 69 returns gpa of 2.3 
   elif(69>=percent>=67):
      result = 2.3            
      return (result) 
    #user enters a value between than 70 and 72 returns gpa of 2.7 
   elif(72>=percent>=70):
      result = 2.7            
      return (result)   
   #user enters a value between than 73 and 76 returns gpa of 3.0 
   elif(76>=percent>=73):
      result = 3.0            
      return (result)   
   #user enters a value between than 77 and 79 returns gpa of 3.3
   elif(77>=percent>=79):
         result = 3.3            
         return (result)  
   #user enters a value between than 80 and 84 returns gpa of 3.7 
   elif(84>=percent>=80):
      result = 3.7            
      return (result)
   #user enters a value between than 85 and 89 returns gpa of 4.0
   elif(89>=percent>=85):
      result = 4.0            
      return (result)
   #user enters a value between than 90 and 100 returns gpa of 4.0
   elif(100>=percent>=90):
      result = 4.0            
      return (result)   
   
def card_namer(value, suit):   
   '''(str,str)->str
       takes two  strings, value and suit and and returns the full name of the  card
       REQ: x=value and y=suits
       REQ: value is , T, J, Q, K, between 1-9 or A.
       >>> card_namer('Q','D')
       'Queen of Diamonds'
       >>> card_namer('9','S')
       '9 of Spades'
       >>> card_namer('8','T')
       'CHEATER!'
       ''' 
   #naming the suit1 and value1 as a string.
   suit1 = ""    
   value1 = "" 
   #if the value A is true, value1 is equal to Ace
   if (value == 'A'):        
      value1= "Ace"    
   #otherwise if the value T is true, value1 is equal to 10   
   elif (value == 'T'):        
      value1= "10"    
   #otherwise if the value J is true, value1 is equal to Jack    
   elif (value == 'J'):        
      value1= "Jack"    
   #otherwise if the value Q is true, value1 is equal to Queen 
   elif (value == 'Q'):
      value1= "Queen"  
  #otherwise if the value K is true, value1 is equal to King 
   elif (value == 'K'):
      value1 = "King"
   #otherwise if none of the above are true  
   else:
      #let value1 = value
      value1 = value 
   #if suit D is true, D is equivalent to Diamonds 
   if (suit == 'C'): 
      suite = "Clubs "
  
   #otherwise if the suit C is true, value1 is equal to Clubs      
   elif  (suit == 'D'):
      suite = "Diamonds" 
   #otherwise if the suit H is true, value1 is equal to Hearts   
   elif (suit == 'H'):
      suite = "Hearts"  
   #otherwise if the suit S is true, value1 is equal to Spades
   elif (suit == 'S'):
      suite = "Spades"
   #Otherwise
   else:   
      #Return Cheater
      return "CHEATER!"
   #return Value1+ of + Suite
   return value1 + " of " + suite