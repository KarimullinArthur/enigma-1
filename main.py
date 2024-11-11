import random
import base64


class Enigma:
    MAX_CHR = 1114111

    roter_1 = 0
    roter_2 = 0
    roter1_start = roter_1
    roter2_start = roter_2
    
    roter_1_com = {}
    roter_2_com = {}

    for c in range(0, MAX_CHR):
        roter_1_com[c] = c 
        roter_2_com[c] = c 

    roter_1_com_inv = dict(zip(roter_1_com.values(), roter_1_com.keys()))
    roter_2_com_inv = dict(zip(roter_2_com.values(), roter_1_com.keys()))


    
    def encrypt(self, value: str):
        result = []

        def enc(self, char_code):
            return self.roter_1_com[char_code]+self.roter_1+self.roter_2

        for char in value:
            char_code = ord(char)
            try:
                result.append(chr(enc(self, char_code)))
            except ValueError:
                print('PING')
                self.roter_1 = 0
                self.roter_2 = 0
                result.append(chr(enc(self, char_code)))

            self.roter_1 += 1
            self.roter_2 += 1
        result = ''.join(result).encode()
        result = base64.b64encode(result)
        return result.decode()

    def decrypt(self, value: str):
        result = []
        value = base64.b64decode(value.encode()).decode()
        print()
        print(value)
        str(value)
        print()

        def enc(self):
            return self.roter_1_com_inv[ord(char)]-self.roter1_start-self.roter2_start

        for char in value:
            try:
                result.append(chr(enc(self)))
            except ValueError:
                print('PINGD', end='')
                self.roter1_start = 0
                self.roter2_start = 0
                result.append(chr(enc(self)))

            self.roter1_start += 1
            self.roter2_start += 1
        return ''.join(result)


enigma = Enigma()
# enc = enigma.encrypt("Hello world!\nHello world!")
_str = '''000000000
Привет бонч, ты должен УМЕРЕТЬ!!

 Decoding Base64 string is exactly opposite to that of encoding. First we convert the Base64 strings into unencoded data bytes followed by conversion into bytes-like object into a string. The below example depicts the decoding of the above example encode string output.

Example:'''
# enc = enigma.encrypt("Hello World!\nHello world!")
# print(enc)
# print(enigma.decrypt(enc))


enc = enigma.encrypt(_str)
print(enc)
print(enigma.decrypt(enc))
