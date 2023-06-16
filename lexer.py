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
        if len(self.current_line) != 0:
            self.next_char  =  self.EOF

        if self.current_pos >= len(self.current_line):
            self.current_line = self.input.readline()
            self.current_pos = 0

        if self.current_pos < len(self.current_line):
            self.next_char = self.current_line[self.current_pos]
            self.current_pos += 1
        else:
            self.next_char = self.EOF

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
                break
            elif c == '"':
                c = self.get_next_char()
                break
            else:
                #unexpected!
                if not c.isspace():
                    print('unexpected char:',c)

        while c.isnumeric():
            current_number += c
            c = self.get_next_char()
        if current_number and c.isspace() or c == self.EOF:
            return token('number', int(current_number))

        while c != '"':
            current_string += c
            c = self.get_next_char()
        if current_string and c=='"':
            return token('string', current_string)
        
        return None

def main():
    l = lexer(sys.stdin)
    t = True
    while t:
        t = l.get_next_token()
        print(t)

if __name__ == '__main__':
    main()