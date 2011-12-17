# Terminal command: python wine-data.py

class Wine:
    def __init__(self):
        self.name = ''
        self.tel1 = ''
        self.addr = ''
	self.city = ''
	self.zip = ''
    def __unicode__(self):
        return ':'.join(['name',self.name, 'telephone',self.tel1, 'address', self.addr, 'location', self.city, 'zip', self.zip])

    def read_line(self,line,index):
        if index == 0:
            self.name = line
        if len(line.split('tel.'))>1:
            self.tel1 = line.split('tel. ')[1]
        if index == 2:
            self.addr = line
	if index == 3:
		self.city = line.split(',')[0]
		try:
			self.zip = line.split(',')[1]
		except:
			pass



count = 0
current = []
for line in open('wine.csv'):
    current.append(line)
    if line.split('\n') == ['','']:
        count = count + 1
        current = map(lambda x: x.strip('\n'), current)
        if not current == ['']:
            wine = Wine()
            for i in range(len(current)):
                wine.read_line(current[i], i)
            print unicode(wine)
        current = []


