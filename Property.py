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
# property()
------------

class Sony:
    def __init__(self, project):
        self._project = project

    def getTeam(self):
        return self._project

    def setTeam(self, project):
        self._project = project

    def delTeam(self):
        del self._project

    project = property(getTeam, setTeam, delTeam)

s = Sony('PlayStation')

print(s.project)

s.project = 'SWQA'

print(s.project)

del s.project
-------------------------------------------------------------
