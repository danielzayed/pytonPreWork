from  hwltd.organization  import *

''' 
function thats finds the department in the structure
'''
def find_dep_in_org(head,department) :
    dep = None
    if(head.name == department ) :
         return head
    if  head.workers ==[ ] :
        return None
    for group in  head.workers :
          if group.name ==department:
                  return dep
          if(dep !=None and dep.name==department) :
              return dep
          else :
                dep= find_dep_in_org(group,department)
    return dep

def help_get_num(department,depth,i) :
    if(i==1 ) :
         num_of_workers=len(department.get_workers)
         print('\t' * i, end='')
         print(department.name + " -" + num_of_workers + " workers")
         i=i+1
         depth=depth-1
    if (depth <= 0):
        return
    if(department.workers==[] or not isinstance(department.workers[0],Group)) :
         return
    for item in department.workers:
        num_of_workers = len(item.get_workers())
        print('\t' * i, end='')
        print(item.name + " -" + num_of_workers + " workers")
        if isinstance(department.workers,Group):
           help_get_num(item,depth-1,i+1)


def get_num_employees(department,depth) :
        if depth <= 0 :
            return

        i=1
        head_dep= find_dep_in_org(department)
        if(head_dep==None) :
            return
        help_get_num(head_dep, depth,1)


def get_avg_salary(group) :
     list_of_workers=group.get_workers()
     sum=0
     for i in list_of_workers : 
         sum+= i.salary
         
     return sum /len(list_of_workers)
def  search_for_worker(worker,head) :
    if(isinstance(head,Group)) :
      for i in head.workers :
          if(not isinstance(i,Group)) :
              if(i.first_name == worker.first_name ) :
                  return head
          else :
             head=search_for_worker(worker,i)
      return head



def get_relational_salary(worker) :
    dict ={}
    salary = worker.salary
    department = search_for_worker(worker,HelloWorld.head)
    for _worker  in department  :
        if worker.id != _worker :
            dict[_worker]=_worker.salary/salary



    return dict