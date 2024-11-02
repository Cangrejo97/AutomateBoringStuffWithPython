print( "\033c", end="" )

def collatz ( number ) :
    
    try:
               
        number = int( number )
                   
        if number % 2 == 0  :

            number //= 2
                
        elif number % 2 == 1 :
            
            number = 3 * number + 1

        print ( number )
 
        if number > 1 :
            
               collatz ( number )          
       
    except :
   
        print ( 'Thats not a Number!')

print ( 'Enter Number: ')
collatz ( input() )


    