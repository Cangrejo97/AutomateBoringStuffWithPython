print("\033c", end="")

def hello() :
    
    print ( 'Hello my Friend <3 <3 <3')
    print ( 'I hope you are doing good?', end="\n\n")
    print ( 'Es gibt 3 Gegenstände!\nWählen sie eines aus und nennen sie mir die Nummer!' )  

def getItemNameFromListNum(item) :
    while True :

        if '1' == item   :
            
            return 'Kreis'
            
        
        elif '2' == item   :
            
            return 'Viereck'
        
        elif '3' == item   :
            
            return 'Dreieck'
        
        else:

            print ( 'STOP that! Your input was Out of scope!')
            print ( 'Enter Again!')
            item = input()


hello()
print( getItemNameFromListNum ( input() ) )
