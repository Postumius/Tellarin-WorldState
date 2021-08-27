def save(ls, weather, location):
    def toLine(ls):
        s = ''
        for n in ls:
            s = s + str(n) + ' '
        return s
    
    file = open("today.txt", 'w')
    file.write("{}\n{}\n{}".
        format(toLine(ls), weather, location))

def load():
    def fromLine(s):
        ls = []
        for n in s.split():
            ls.append(int(n))
        return ls

    blank = ([0, 0, 0, 0, 0, 0], '', '')
    
    try:
        file = open("today.txt", 'r')
        s = file.readline()
        if s == '':
            return blank
        else:
            return (
                fromLine(s),
                file.readline().strip(),
                file.readline()
            )    
    except:
        return blank
