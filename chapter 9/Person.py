"""
Exercise 9.13: Represent people by a class hierarchy
Author: Weiyun Lu
"""

class Person:
    def __init__(self, name, address=None, phone=None, birth=None, nationality=None):
        self.name, self.address, self.phone, self.birth, self.nationality = \
            name, address, phone, birth, nationality
            
    def __str__(self):
        data = ''
        data += "Name = %s \nAddress = %s\nPhone number = %s\nBirthday = %s\nNationality = %s"\
            %(self.name, self.address, self.phone, self.birth, self.nationality)
        return data

class Worker(Person):
    def __init__(self, name, address=None, phone=None, birth=None, nationality=None, company=None,\
    company_address=None, workphone=None):
        Person.__init__(self, name, address, phone, birth, nationality)
        self.company, self.company_address, self.workphone = company, address, workphone
        
    def __str__(self):
        data = Person.__str__(self)
        data += "\nCompany = %s \nCompany Address = %s\nWork phone = %s"\
            %(self.company, self.company_address, self.workphone)
        return data
        
class Scientist(Worker):
    def __init__(self, name, address=None, phone=None, birth=None, nationality=None, company=None,\
    company_address=None, workphone=None, discipline=None, worktype=None):
        Worker.__init__(self, name, address, phone, birth, nationality, company, company_address,\
            workphone=None)
        self.discipline, self.worktype = discipline, worktype
    
    def __str__(self):
        data = Worker.__str__(self)
        data += "\nDiscipline = %s \nType = %s"\
            %(self.discipline, self.worktype)
        return data
        
class Researcher(Scientist):
    pass
        
if __name__ == '__main__':
    Jeff = Person('Jeff Schmidt', '123 Easy Street', '613 555-6666', 'January 12')
    print Jeff
    print
    Jacob = Worker('Jacob McDonald', '44 Jones Road', '613 999-9911', 'September 5', 'Canadian', \
        'Shopify', '125 Elgin Street', '613 222-2233 ext. 111')
    print Jacob
    print
    Phil = Researcher('Phil Scott', '99 Fake Avenue', '613 123-4567', 'Decembruary 32', 'Canadian',\
        'University of Ottawa', '585 King Edward Ave', '613 123-4444 ext. 9999', \
        discipline='Mathematics and computer science', worktype='Theoretical')
    print Phil