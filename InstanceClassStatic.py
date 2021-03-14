class Sony:

    __division = 'Software Architecture Division'

    def __init__(self, fullname):
        self.fullname = fullname

    def email(self):
        self.first, self.last = self.fullname.split(' ')
        return self.first + '.' + self.last + '@sony.com'

    @classmethod
    def change_dept(cls, division):
        cls.__division = division

    @staticmethod
    def new_dept():
        return Sony.__division

s1 = Sony('Monish Kalaiselvan')
s2 = Sony('Sagar Ramesh')

#print(Sony._Sony__division)   #Private class variable can be accessed... 
                               #But not recommended
Sony.change_dept('SARD')

print(s1.new_dept())
print(s2.new_dept())

print(s1.email())
------------------------------------------------------------------

class Sony:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @classmethod
    def name(cls, fullname):
        first, last = fullname.split(' ')
        return cls(first, last)

    def email(self):
        return self.first + '.' + self.last + '@sony.com'

s = Sony.name('Monish Kalaiselvan')
print(s.email())
        
-------------------------------------------------------------------
