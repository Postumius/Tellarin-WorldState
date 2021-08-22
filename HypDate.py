
def multiBaseAddition(xs, ys, bs):

    def tail(ls):
        cp = ls.copy()
        cp.pop(0)
        return cp

    if len(bs) == 0:
        return [ xs[0] + ys[0] ]
    else:
        rest = multiBaseAddition(
            tail(xs), tail(ys), tail(bs))
        return [
            xs[0] + ys[0] + rest[0] // bs[0],
            rest[0] % bs[0]
        ] + tail(rest)


class HypDate:

    def __init__(
    self, 
    year=0, 
    season=0, 
    cycle=0, 
    day=0, 
    hour=0, 
    minute=0):
        self.year = year
        self.season = season 
        self.cycle = cycle
        self.day = day
        self.hour = hour
        self.minute = minute

    
    def plus(self, other):
        minuteSum = self.minute + other.minute
        hourSum = self.hour + other.hour + minuteSum // 60
        daySum = self.day + other.day + hourSum // 24
        cycleSum = self.cycle + other.cycle + daySum // 10
        seasonSum = self.season + other.season + cycleSum // 9
        yearSum = self.year + other.year + seasonSum // 4
        return HypDate(yearSum, seasonSum % 4, 
            cycleSum % 9, daySum % 10)
    
    def toList(self): 
        return [self.year, self.season, self.cycle, self.day,
            self.hour, self.minute]

    def seasonName(self):
        return['Seed', 'Harvest', 'Scorch', 'Frost'][self.season]

    def cycleName(self):
        return {
            0 : '1st',
            1 : '2nd',
            2 : '3rd'
        }.get(self.cycle, str(self.cycle + 1) + 'th')

    def dayName(self):
        return ['Silth', 'Est', 'Kross', 'Oust', 'Rest', 'Streth', 
            'Eith', 'Kesh', 'Orseh', 'Rath'][self.day]

    def dateName(self):
        return '{} {} of {}, {} YoR'.format(
            self.cycleName(), self.dayName(), 
            self.seasonName(), str(self.year))
        

    
