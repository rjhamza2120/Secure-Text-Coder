
import os 

while True:
    print("Welcome Confidential Person:\n1). Check the rules \n2). Encode or Decode \n3). Exit")
    c=int(input("Enter your choice whether you want to check the rules or encode or decode a messege:"))
    os.system("cls")
    
    if(c==1):
        while True:
            code=["bravo","dragon","itshello"]
            cd=input("Enter your code to access the rules: ")

            if cd == code[0] or cd == code[1] or cd == code[2]:
                print("These are the coding rules:\n")
                print("\tEncoding Rules:")
                print("1) If the word contains atleast 3 characters, remove the first letter and append it at the end")
                print("2) Now append three random characters at the starting and the end")
                print("3) else:\n\tsimply reverse the string\n")

                print("\tDecoding Rules:")
                print("1) If the word contains less than 3 characters, reverse it")
                print("2) else:\n\tremove 3 random characters from start and end. Now remove the last letter and append it to the beginning\n")
                break

            else:
                print("Enter the correct code to get access")

    elif(c==2):
        while True:
            print("\nEncoder And Decoder:\n")

            print("You Want to encode or decode the messege:\n")
            print("1). ENCODE     2). DECODE\n")
            a=int(input("Enter your choice:"))
            os.system("cls")

            if (a==1):
                en=input("Enter the message you want to encode:")
                a=en.lower()
                a = a + " "
                cnt=en.count(" ")
                fen = str()
                for x in range(cnt+1):
                    i=0
                    i = a.find(" ")
                    if len(a[0:i]) == 1:
                        fen = fen + " " + a[0]
                        a = a[i+1:]
                        
                    elif len(a[0:i]) == 2:
                        fen = fen + " " + a[1] + a[0] 
                        a = a[i+1:]

                    else:    
                        b = a[1:i] + a[0]
                        a = a[i+1:]
                        add = "cbi"
                        fen = fen + " " + add + b + add

                print("Encoded Messege: ",fen,"\n")
                break            

            elif (a==2):
                de=input("Enter the messaege you want to decode:")
                a=de.lower()
                a = a + " "
                cnt=de.count(" ")
                fde = str()
                for x in range(cnt+1):
                    i=0
                    i = a.find(" ")
                    if len(a[0:i]) == 1:
                        fde = fde + " " + a[0]
                        a = a[i+1:]
                
                    elif len(a[0:i]) == 2:
                        fde = fde + " " + a[1] + a[0] 
                        a = a[i+1:]

                    else:    
                        b = a[0:i]
                        c=b[0:3]
                        d=b[i-3:]
                        b=b.removeprefix(c)
                        b=b.removesuffix(d)
                        l=len(b)
                        
                        fde = fde + " " + b[l-1] + b[0:l-1]
                        a = a[i+1:]
                print("Decoded Messege: ",fde,"\n")  
                break

            else:
                print("Enter the correct choice")
                exit

    elif(c==3):
        break

    else:
        print("Enter the correct choice")
        exit

