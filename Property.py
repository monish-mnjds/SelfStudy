# @property 
-----------
class Sony:
    def __init__(self, team):
        self.team = team

    @property
    def project(self):
        return self.team

    @project.setter
    def project(self, team):
        self.team = team

    @project.deleter
    def project(self):
        del self.team

s = Sony('PlayStation')

print(s.team)

del s.team

s.team = 'SWQA'

----------------------------------------
