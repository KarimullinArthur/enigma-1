import random
import base64


class Roter:
    def __init__(self, number: int, position: int, turn_position: int, max_char):
        MAX_CHR=max_char
        
        self.number = number
        self.position = position
        self.start_position = position
        self.turn_position = turn_position
        self.count_of_turns = 0

        self.commutation_table = {}

        full_abc = []
        for c in range(0, MAX_CHR+1):
            full_abc.append(c)

        for c in range(0, MAX_CHR+1):
#             self.commutation_table[c] = c
            foo = random.choice(full_abc)
            self.commutation_table[c] = foo
            print(foo)
            full_abc.remove(foo)

        self.commutation_table_inv = dict(zip(self.commutation_table.values(), self.commutation_table.keys()))


    def __repr__(self):
        return f"<Roter number={self.number} position={self.position} turn_position={self.turn_position} start_position={self.start_position}>"
    
        

class Enigma:
    MAX_CHR = 1114111
#     MAX_CHR = 256
    MAX_CHR = 10000
#     MAX_CHR = 127

    def __init__(self, count_roters: int = 3):
        self.roters = []
        for roter_number in range(1, count_roters+1):
            self.roters.append(Roter(number=roter_number,
                                     position=0,
                                     turn_position=1,
#                                      position=random.randint(1, 10),
#                                      turn_position=random.randint(1, 3),
                                     max_char=self.MAX_CHR
                                     )
                               )

            print(self.roters)
            print()

    def encrypt(self, value: str):
        result = []

        def enc(self, char_code):
            current_code = char_code
            for roter_number in range(len(self.roters)):
                roter = self.roters[roter_number]
                try:
                    current_code = roter.commutation_table[current_code+roter.position]
                except KeyError:
                    if current_code+roter.position >= self.MAX_CHR:
                        roter.position = self.MAX_CHR - current_code
#                         print(current_code)
#                         print('---')
#                         print(chr(current_code))
#                         print('---')
#                         print(roter.position)
                    current_code = roter.commutation_table[current_code+roter.position]

                roter.position += 1
                roter.count_of_turns += 1
                if roter.count_of_turns > roter.turn_position:
#                     print("PING")
#                     print(roter.count_of_turns)
#                     print(roter.turn_position)
                    roter.count_of_turns = 0
                    try:
                        self.roters[roter_number+1].position += 1
                    except IndexError:
                        pass
            return current_code

        for char in value:
            char_code = ord(char)
            result.append(chr(enc(self, char_code)))
                
        result = ''.join(result).encode()
        result = base64.b64encode(result)
        return result.decode()

    def decrypt(self, value: str):
        result = []
        value = base64.b64decode(value.encode()).decode()
        print()
        print(value)
        print()
        for ch in value:
            print(ord(ch), end=' ')
        print()

        def dec(char_code):
            current_code = char_code
            for roter_number in range(len(self.roters)):
                roter = self.roters[roter_number]
                try:
                    current_code = roter.commutation_table[current_code-roter.position]
                except KeyError:
                    if current_code+roter.position >= self.MAX_CHR:
                        roter.position = self.MAX_CHR - current_code
#                         print(current_code)
#                         print('---')
#                         print(chr(current_code))
#                         print('---')
#                         print(roter.position)
                    current_code = roter.commutation_table[current_code+roter.position]

                roter.position += 1
                roter.count_of_turns += 1
                if roter.count_of_turns > roter.turn_position:
#                     print("PING")
#                     print(roter.count_of_turns)
#                     print(roter.turn_position)
                    roter.count_of_turns = 0
                    try:
                        self.roters[roter_number+1].position += 1
                    except IndexError:
                        pass
            return current_code
#             return result
            return self.roter_1_com_inv[ord(char)]-self.roter1_start-self.roter2_start

        for char in value:
            try:
                result.append(chr(dec(char)))
            except ValueError:
                print('PINGD', end='')
                self.roter1_start = 0
                self.roter2_start = 0
                result.append(chr(dec(char)))

            self.roter1_start += 1
            self.roter2_start += 1
        return ''.join(result)


enigma = Enigma(count_roters=3)
"Привет бонч, ты должен УМЕРЕТЬ!!"
# enc = enigma.encrypt("Hello world!\nHello world!")
_str = '''00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

 Decoding Base64 string is exactly opposite to that of encoding. First we convert the Base64 strings into unencoded data bytes followed by conversion into bytes-like object into a string. The below example depicts the decoding of the above example encode string output.

Example:'''
# enc = enigma.encrypt("Hello World!\nHello world!")
# print(enc)
# print(enigma.decrypt(enc))


enc = enigma.encrypt(_str)
print()
print("Input")
print()
print(_str)
for ch in _str:
    print(ord(ch), end=' ')
print()
print("Encrypt:")
print(enc)
print()
dec_str = base64.b64decode(enc).decode()
for ch in range(len(dec_str)):
    print(dec_str[ch], end='')
print()
print()
for ch in range(len(dec_str)):
    print((ord(dec_str[ch]) - ord(dec_str[ch-1])), end=" ")
print()
print()
for ch in range(len(dec_str)):
    print((ord(dec_str[ch]), ord(dec_str[ch]) - ord(dec_str[ch-1])), end=' ')
print()
print()
print("Decrypt:")
print(enigma.decrypt(enc))
