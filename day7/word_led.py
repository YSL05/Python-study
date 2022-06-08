import os
import time


def  main ():
    content = '北京理工大学建校80周年******'
    while True:
        #clear the procreen
        os.system('cls')
        print(content)
        #delay 200ms
        time.sleep(0.5)
        content = content[1:] + content[0]

if __name__ == '_main_':
    main ()

main()