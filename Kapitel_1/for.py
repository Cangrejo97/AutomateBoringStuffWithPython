print ( "\033c", end="" )      #Clear Console

print ( 'Give me your name' )

name = input()

if len( name ) >= 1 :

    for i in range ( 1000 )   :
        
        print (str (i+1), '.', name, "ist der Beste!" )

