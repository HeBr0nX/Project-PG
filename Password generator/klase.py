from random import *
from string import *
from re import *

class pass_generator:
    def __init__(self):
        self.password=''
        self.requirements=[0,False,False,False]
        self.approve=[0,False,False,False]
    
    def __str__(self):
        return str(self.password)

    #aprove->[broj,veliko_slovo,broj,spec]
    #requirements->[broj karaktera,veliko slovo,broj,specijalni karakter]

    def generate(self,requirements=[0,False,False,False]):
        self.requirements=requirements
        lista=[0]

        if self.requirements[1]==True:
            lista.append(1)
        if self.requirements[2]==True:
            lista.append(2)
        if self.requirements[3]==True:
            lista.append(3) 

        for i in range(requirements[0]):
            j=choice(lista)
            if j==0:
                self.password+=self.generate_lower()
            elif j==1:
                 self.password+=self.generate_upper()
            elif j==2:
                 self.password+=self.generate_number()
            elif j==3:
                 self.password+=self.generate_spec()

            

        self.approve[0]=self.len_check()
        self.approve[1]=self.upper_check()
        self.approve[2]=self.number_check()
        self.approve[3]=self.spec_check()
        print(self.requirements)
        print(self.approve)
        print(self.password)
        if self.approve==self.requirements:
            print('Uspesno kreirana sifra')

        else:
            self.password=""
            print('Generise se nova sifra')
            self.generate(requirements)

        
        
    def generate_lower(self):
        return choice(ascii_lowercase)
    
    def generate_upper(self):
        return choice(ascii_uppercase)
    
    def generate_number(self):
        return str(randint(0,9))
    
    def generate_spec(self):
        return choice(punctuation)

    def len_check(self):
        if len(self.password)==self.requirements[0]:
            return self.requirements[0]


    def lower_check(self):
        if any(x.islower() for x in self.password):
            return True 
        else:
            return False

    def upper_check(self):
        if any(x.isupper() for x in self.password):
            return True
        else:
            return False
    
    def number_check(self):
        if any(x.isdigit() for x in self.password):
            return True
        else:
            return False
        
    def spec_check(self):
        for i in punctuation:
            if i in self.password:
                return True
        return False
        

p=pass_generator()
p.generate([7,True,False,True])
print(p)