


class Group :
    def __init__(self,name,desc,parent=None):
        self.name=name
        self.desc=desc
        self.parent=parent
        self.workers=[]
        self.subgroups=[]



    @property
    def get_workers(self):
        if self.workers!=[]:
         return [worker for worker in self.workers]
        elif self.subgroups!=[]:
            return [worker for subgroup in self.subgroups for worker in subgroup.workers]
        return []

    @property
    def get_parents(self):
        parent=self.parent
        while parent!=None:
            yield parent
            parent=parent.parent
class Worker:
    def __init__(self,Person,salary):
        self.Person=Person
        self.salary=salary


    def get_salary(self):
        return self.salary

class Engineer(Worker):

 def __init__(self,Person,salary,bonus):
     super().__init__(self,Person,salary)
     self.bonus=bonus

 def get_salary(self):
     return (self.salary+ self.bonus)


class SalesPerson(Worker):
    def __init__(self,Person,salary,commission,deals):
        super().__init__(self,Person,salary)
        self.commission=commission
        self.deals=deals

    def get_salary(self):
        return (self.salary+self.commission*sum(self.deals))


