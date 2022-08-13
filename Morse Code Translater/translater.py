MORSE_CODE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
# Reverse dictionary for morse to english conversion.
REVERSE_MORSE_CODE = {value: key for key, value in MORSE_CODE.items()}

class Translater():


    def to_morse_code(self):
        translated = ''
        for char in self:
            if char == ' ':
                # Replacing space with '-' to separate words when converted back to english.
                word_break = " " + MORSE_CODE['-'] + " "
                # word_break = ' '
                translated += word_break

            else:
                translated += MORSE_CODE[char.upper()]
                translated += " "
        return translated

    def to_english(self):
        words = self.split(' ')
        translated = ''
        for word in words:
            if word == '':
                pass
            else:
                translated += REVERSE_MORSE_CODE[word]

        return translated
