print("\033c", end="")

def openFile ():
  
    try :

        f = open("/projects/AutomateBoringStuffWithPython/Kapitel_1/demofile.txt")
        try:
            
            f.write("Lorum Ipsum")
       
        except:
            
            print("Something went wrong when writing to the file")
       
        finally:
            
            f.close()
   
    except:
   
        print("Something went wrong when opening the file")

openFile()