class Enigma:
    roter1 = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0',
             '1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z','{','|','}','~',
              ]

    roter2 = ['~', '}', '|', '{', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r',
              'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
              'd', 'c', 'b', 'a', '`', '_', '^', ']', '\\', '[', 'Z', 'Y', 'X',
              'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K',
              'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '@', '?', '>',
              '=', '<', ';', ':', '9', '8', '7', '6', '5', '4', '3', '2', '1',
              '0', '/', '.', '-', ',', '+', '*', ')', '(', "'", '&', '%', '$',
              '#', '"', '!'
              ]


    def encrypt(self, inp):
        return inp

    def decrypt(self, inp):
        pass


enigma = Enigma()

print(enigma.encrypt("Hello"))
