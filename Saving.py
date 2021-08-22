def save(ls):
    def toString(ls):
        s = ''
        for n in ls:
            s = s + str(n) + ' '
        return s
    
    file = open("today.txt", 'w')
    file.write(toString(ls))

def load():
    def fromString(s):
        ls = []
        for n in s.split():
            ls.append(int(n))
        return ls
    
    file = open("today.txt", 'r')
    s = file.read()
    if s == '':
        return [0, 0, 0, 0, 0, 0]
    else:
        return fromString(s)