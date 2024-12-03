import random
import base64


class Roter:
    def __init__(self, number: int, position: int, turn_position: int, max_char):
        MAX_CHR=max_char
        
        self.number: int = number
        self.position: int = position
        self.start_position: int = position
        self.turn_position: int = turn_position
        self.count_of_turns: int = 0

        self.commutation_table = {}

        full_abc = []
        for c in range(0, MAX_CHR+1):
            full_abc.append(c)

        for c in range(0, MAX_CHR+1):
#             self.commutation_table[c] = c
            foo = random.choice(full_abc)
            self.commutation_table[c] = foo
            full_abc.remove(foo)
        
        self.commutation_table_inv = dict(zip(self.commutation_table.values(), self.commutation_table.keys()))
        print(self.commutation_table)
        print(self.commutation_table_inv)

    def __repr__(self):
        return f"<Roter number={self.number} position={self.position} turn_position={self.turn_position} router_count_of_turns={self.count_of_turns} start_position={self.start_position}>"
    
        

class Enigma:
    MAX_CHR = 1114111
#     MAX_CHR = 256
#     MAX_CHR = 10000
    MAX_CHR = 127

    def __init__(self, count_roters: int = 3):
        self.roters = []
        for roter_number in range(1, count_roters+1):
            self.roters.append(Roter(number=roter_number,
                                     position=0,
                                     turn_position=1,
#                                      position=random.randint(40, 50),
#                                      turn_position=random.randint(1, 3),
                                     max_char=self.MAX_CHR
                                     )
                               )

            print(self.roters)
            print()

    def encrypt(self, value: str) -> str:
        result = []

        def enc(self, char_code):
            current_code = char_code
            for roter_number in range(len(self.roters)):
                roter = self.roters[roter_number]

#                 if current_code+roter.position >= self.MAX_CHR:
#                     roter.position = self.MAX_CHR - current_code
#                     roter.position = 0
#                     current_code = 0 

                current_code = roter.commutation_table[current_code]#roter.position
#                 if current_code+roter.position >= self.MAX_CHR:
# #                     roter.position = current_code - self.MAX_CHR
#                     roter.position = 0 
#                     current_code = roter.commutation_table[char_code]

#                 if roter.position+current_code >= self.MAX_CHR:
#                     roter.position = 0
#                     roter.position += 1
#                 else:
#                     roter.position += 1
                    
#                     print(current_code)
#                     print('---')
#                     print(chr(current_code))
#                     print('---')
#                     print(roter.position)
#                current_code = roter.commutation_table[char_code]+roter.position

                roter.count_of_turns += 1
                roter.position += 1 
#                 if roter.count_of_turns > roter.turn_position:
# #                     print("PING")
# #                     print(roter.count_of_turns)
# #                     print(roter.turn_position)
#                     roter.count_of_turns = 0
#                     try:
#                         self.roters[roter_number+1].position += 1
#                     except IndexError:
#                         pass
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

        def dec(char_code):
            current_code = char_code
            for roter_number in range(len(self.roters)-1, 0-1, -1):
#             for roter_number in range(len(self.roters)):
                roter = self.roters[roter_number]
#                 if current_code+roter.start_position >= self.MAX_CHR:
#                     roter.start_position = self.MAX_CHR - current_code
#                     roter.start_position = 0
#                     current_code = 0 
                current_code = roter.commutation_table_inv[current_code]#roter.start_position

#                 if roter.start_position >= self.MAX_CHR:
#                     roter.start_position = 0
#                     roter.start_position += 1
#                 else:
#                     roter.start_position += 1
# 
#                 if current_code+roter.start_position >= self.MAX_CHR:
#                     roter.start_position = self.MAX_CHR - current_code
#                     roter.start_position = 0
#                     print(current_code)
#                     print('---')
#                     print(chr(current_code))
#                     print('---')
#                     print(roter.position)
#                 current_code = roter.commutation_table_inv[ord(char_code)]#-roter.start_position

                roter.start_position += 1
                roter.count_of_turns += 1
#                 if roter.count_of_turns > roter.turn_position:
# #                     print("PING")
# #                     print(roter.count_of_turns)
# #                     print(roter.turn_position)
#                     roter.count_of_turns = 0
#                     try:
#                         self.roters[roter_number-1].position -= 1
#                     except IndexError: 5 followers · 3 following  5 followers · 3 following 
#                         pass  
#             print('===')
#             print(current_code)
#             print('===')'
            return chr(current_code)

        for char in value:
            result.append(dec(ord(char)))
        return ''.join(result)


enigma = Enigma(count_roters=2)
"Привет бонч, ты должен УМЕРЕТЬ!!"
_str = '''!!!!!!!!
Hello, World!'''

_str = '''Hello world!'''

enc = enigma.encrypt(_str)
print()
print("Input")
print()
print(_str)
print()
for ch in _str:
    print(ord(ch), end=' ')
print()
print("Encrypt:")
print(enc)
print()
enc_str = base64.b64decode(enc).decode()
for ch in range(len(enc_str)):
    print(enc_str[ch], end='')
# print()
# print()
# for ch in range(len(enc_str)):
#     print((ord(enc_str[ch]) - ord(enc_str[ch-1])), end=" ")
print()
print()
for ch in range(len(enc_str)):
    print((ord(enc_str[ch]), ord(enc_str[ch]) - ord(enc_str[ch-1])), end=' ')
print()
print()
print("Decrypt:")
dec = enigma.decrypt(enc)
print(dec)
# for ch in range(len(dec)):
#     print((ord(dec[ch]) - ord(dec[ch-1])), end=" ")
print()
for ch in dec:
    print(ord(ch), end=' ')
