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
        self.next_char = -1
        self.current_line = self.input.readline()
        self.current_pos = 0
        self.EOF = -1
    
    def get_next_char(self):
        if self.next_char == '':
            return self.EOF
        self.next_char = self.input.read(1)
        return self.next_char

    # recognize strings and numbers        
    def get_next_token(self):
        current_number = ''
        current_string = ''

        while True:
            c = self.get_next_char()
            if c == self.EOF:
                return self.EOF
            elif c.isnumeric():
                while c.isnumeric():
                    current_number += c
                    c = self.get_next_char()
                # do we need a put_char so that next token can start with this char?
                return token('number', int(current_number))
            
            elif c == '"':
                c = self.get_next_char()
                while c != '"':
                    current_string += c
                    c = self.get_next_char()
                # do we need a put_char so that next token can start with this char?
                return token('string', current_string)
            
            else:
                #unexpected!
                if not c.isspace():
                    print('unexpected char:',c)

def main():
    l = lexer(sys.stdin)
    t = True
    while t != l.EOF:
        t = l.get_next_token()
        print(t)

if __name__ == '__main__':
    main()