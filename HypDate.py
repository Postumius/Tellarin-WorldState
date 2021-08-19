class HypDate:

    def __init__(self, year, season, cycle, day):
        self.year = year
        self.season = season 
        self.cycle = cycle
        self.day = day

    def plus(self, other):
        daySum = self.day + other.day
        cycleSum = self.cycle + other.cycle + daySum // 10
        seasonSum = self.season + other.season + cycleSum // 9
        yearSum = self.year + other.year + seasonSum // 4
        return HypDate(yearSum, seasonSum % 4, 
            cycleSum % 9, daySum % 10)
    
    def show(self): 
        return (self.year, self.season, self.cycle, self.day)

  
    def dayName(self):
        return ['Silth', 'Est', 'Kross', 'Oust', 'Rest', 'Streth', 
            'Eith', 'Kesh', 'Orseh', 'Rath'][self.day]

    def seasonName(self):
        return['Seed', 'Harvest', 'Scorch', 'Frost'][self.season]
