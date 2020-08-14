class Company(object):
    def __init__(self,emploee_list,app):
        self.emploee = emploee_list
        self.app = app

    def __getitem__(self, item):
        return self.app[item],self.emploee[item]


compny = Company(['too','jojo','bot','aa','cc'],[1,2,3,4,5])

for i in compny:
    print(i)