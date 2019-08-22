'''
function that returns alist of all dep workers
'''


def get_workers_list(workers_list):
    wor_list = []
    if workers_list == [] or not isinstance(workers_list[0], Group):
        return workers_list
    else:
        for subgroup in workers_list:
            if subgroup.workers != [] and isinstance(subgroup.workers[0], Group):
                wor_list += get_workers_list(subgroup.workers)

    return wor_list


class Group:

    def __init__(self,name,desc,parent=None):
        self.name=name
        self.desc=desc
        self.parent=parent
        self.workers=[]  # list of workers or subgroups //




    @property
    def get_workers(self):
      workers_list=self.workers
      return get_workers_list(workers_list)


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
     self.bonus = bonus

  def get_salary(self):
     return (self.salary+ self.bonus)


class SalesPerson(Worker):
    def __init__(self,Person,salary,commission,deals):
        super().__init__(self,Person,salary)
        self.commission=commission
        self.deals=deals

    def get_salary(self):
        return (self.salary+self.commission*sum(self.deals))




