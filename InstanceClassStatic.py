class Sony:

    division = 'Software Architecture Division'

    def __init__(self, fullname):
        self.ename = fullname

    def email(self):
        self.first, self.last = self.ename.split(' ')
        return self.first + '.' + self.last + '@sony.com'

    @classmethod
    def change_dept(cls, division):
        cls.division = division

    @staticmethod
    def new_dept():
        return Sony.division

s1 = Sony('Monish Kalaiselvan')
s2 = Sony('Sagar Ramesh')

print(Sony.division)

Sony.change_dept('SARD')

print(s1.new_dept())
print(s2.new_dept())

print(s1.email())
