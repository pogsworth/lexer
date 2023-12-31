import sys

class token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return self.type + ' ' + str(self.value)

class lexer:
    def __init__(self, input):
        self.input = input
        self.current_char = self.input.read(1)
        self.consumed = False
        self.EOF = -1
    
    def get_next_char(self):
        if self.current_char == '':
            return self.EOF
        if not self.consumed:
            self.consumed = True
            return self.current_char
        self.current_char = self.input.read(1)
        return self.current_char

    # recognize strings and numbers        
    def get_next_token(self):
        while True:
            c = self.get_next_char()
            if c == self.EOF:
                return self.EOF

            elif c.isnumeric():
                current_number = ''
                while c.isnumeric():
                    current_number += c
                    c = self.get_next_char()
                self.consumed = False
                return token('number', int(current_number))
            
            elif c == '"':
                current_string = ''
                c = self.get_next_char()
                while c != '"':
                    current_string += c
                    c = self.get_next_char()
                return token('string', current_string)
            
            else:
                #unexpected!
                if not c.isspace():
                    print('unexpected char:',c)

def main():
    input = sys.stdin
    if len(sys.argv) > 1:
        input = open(sys.argv[1])
    l = lexer(input)
    t = True
    while t != l.EOF:
        t = l.get_next_token()
        print(t)

if __name__ == '__main__':
    main()