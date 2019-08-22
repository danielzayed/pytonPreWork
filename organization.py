from workers.structure import *
from workers.Person import *
import  hwltd.organization




'''
company = Group("HelloWorld", 'company Head Department', None)# company helloworld
# defining the sub groups of company
eng_dep = Group("Engineering Department","Engineering Head Department - responsible for all company's Engineering Aspects",company)
hr_dep =  Group("Hr Department","hr Head Department",company)
fin_dep=Group("Finance Department","Finance Department",company)
# insert  subgroups for company ( HelloWorld)
company.subgroups.append(eng_dep)
company.subgroups.append(hr_dep)
company.subgroups.append(fin_dep)
# defining the sub groups of eng_dep
sw_group=Group("SW Group","Software Group!",eng_dep)
hw_group=Group("HW Group","Hardware Group!!",eng_dep)
cto_group=Group("Cto Group","Cto Group!",eng_dep)
sys_group=Group("Sys Group","System Group",eng_dep)
# insert  subgroups for eng_dep
eng_dep.subgroups.append(sw_group)
eng_dep.subgroups.append(hw_group)
eng_dep.subgroups.append(cto_group)
eng_dep.subgroups.append(sys_group)
# defining the sub groups for sw group
inf_team=Group("Infrastructure Team","Infrastructure Team -Engineering dep.!!!",sw_group)
app_team=Group("App Team","App Team-SW group",sw_group)
dri_team=Group("Drivers Team","Drivers Team-SW group",sw_group)
qa_team=Group("QA Team","QA team -SW group",sw_group)
# defining the sub groups for hw group
chip_team=Group("Chip Team","Chip Team-HW group",hw_group)
broad_team=Group("Broad Team","Broad Team-HW group",hw_group)
power_team=Group("Power Team","Power Team-HW group",hw_group)
# defining the sub groups for sys group
des_team=Group("Design Team","Design Team-System group",sys_group)
poc_team=Group("Poc Team","Poc Team - System group",sys_group)
# insert  subgroups for sw group
sw_group.subgroups.append(inf_team)
sw_group.subgroups.append(app_team)
sw_group.subgroups.append(dri_team)
sw_group.subgroup.append(qa_team)
# insert subgroups for hw group
hw_group.subgroups.append(chip_team)
hw_group.subgroups.append(broad_team)
hw_group.subgroups.append(power_team)
# insert subgroups for sys group
sys_group.subgroups.append(des_team)
sys_group.subgroups.append(poc_team)
# defining the sub groups of hr_dep
rec_group= Group("recruitment Group","recruitment Group-Hr Dep",hr_dep)
cul_group= Group("culture Group","culture Group-Hr Dep",hr_dep)
#inserting the sub groups of hr_dep
hr_dep.subgroups.append(rec_group)
hr_dep.subgroups.append(cul_group)
# defining the sub groups of rec_group
tech_team=Group("tech Team","Tech team-rec group",rec_group)
staff_team=Group("staff Team" , "Staff team-rec-group",rec_group)
# inserting the sub groups of rec_group
rec_group.subgroups.append(tech_team)
rec_group.subgroups.append(staff_team)
# defining the sub groups of fin_dep
sal_group=Group("salary Group","Salary Group-Finance dep",fin_dep)
bud_group=Group("budget Group","Budget Group-Finance dep",fin_dep)
# inserting hte sub groups of fin_dep
fin_dep.subgroups.append(sal_group)
fin_dep.subgroups.append(bud_group)
# defining the sub groups of bud_group
inc_team=Group("income Team","Income Team-Budget group",bud_group)
out_team=Group("outcome Team","Outcome Team -Budget group",bud_group)
#inserting the sub groups of bud_groups
bud_group.subgroups.append(inc_team)
bud_group.subgroups.append(out_team)
'''

import json

def help_get_sons(new_dict,i,head) :
 sons=[]
 for key,value in new_dict.items() :
     sons.append(HelloWorld.make_Group(key,"-\n"*i,head))
 return sons



def search_for_head(head, key):
     dep=None
     if(head.name== key):
        return head
     if(head.workers==[]):
       return None

     for group in head.workers:
         if group.name == key:
             dep=group
             return dep
         if(dep!=None and dep.name==key) :
             return dep
         elif group.workers !=[]:
              dep=search_for_head(group,key)
     return dep



class Employees:
    def __init__(self,employees={}):
        self.employees=employees

class HelloWorld:

   theEmployees=Employees({})
   # function that prints the structure of the organization hello world
   @staticmethod
   def print_Hello_World_Structure(head,helloworld_head,i):
     if(not isinstance(head,Group)) :
         return
     if(head.workers==[]) :
         return
     if(head.name==helloworld_head.name) :
         print('\t'*i+head.name)
         i=i+1

     for group in head.workers :
         if(not isinstance(group,Group)) :
             print('\t' * i + group.Person.name)
         else :
               print ('\t'*i+group.name)
         HelloWorld.print_Hello_World_Structure(group,helloworld_head,i+1)
   @staticmethod
   def make_Group(name, desc, Parent):
       return Group(name, desc, Parent)


   @staticmethod
   def build_org_structure(head_dict,i,head,company_head):
       for key, value in head_dict.items() :
            if(isinstance(value,dict)) :
                head = search_for_head(company_head,key)
                head.workers=help_get_sons(value,i,head)
                HelloWorld.build_org_structure(value,i+1,head,company_head)
       return

   @staticmethod
   def insert_branch( worker, dep_name,head):

       for i in head:
          if  not isinstance(i, Group) :
               if head.name == dep_name :
                  head.workers.append(worker)
                  return
          else :
                HelloWorld.insert_branch(worker,dep_name,i.workers)



       return

   def __init__(self,path_file):
       with open ('hwltd/structure_organization.json') as hello:
           j_obj = json.load(hello)
           hello_world_dict = j_obj['Company']
           self.head=HelloWorld.make_Group("Hello World","-",None)
           HelloWorld.build_org_structure(hello_world_dict,1,self.head,self.head)
           with open(path_file, 'r') as f:
             i = 0
             for line in f :

               if(line[0]!='#'):
                  new_line=line.split(',')
                  name=new_line[1]
                  email=new_line[3]
                  if(email[0]==" "):
                      email=email[1:]
                  HelloWorld.theEmployees.employees[email]=name
                  list_ph=new_line[4].split(';')
                  new_phone=list_ph[0]
                  if (new_phone[0] == " " ):
                      new_phone = new_phone[1:]
                  new_phone=Phone(new_phone)

                  address=new_line[5].split(';')
                  if(len(address)==4) :  # then it is astreet address Baby!!
                     The_address=StreetAddress(address[0],address[1],address[2],address[3])

                  else :
                      The_address=PobAddress(address[0],address[1],address[2])
                  newPerson=Person.New_Person(name,new_line[0],new_line[2],email,list_ph,The_address)
                  role=new_line[7]
                  new_Worker=None
                  if(role=='staff') :
                      new_Worker=Worker(newPerson,new_line[8])
                  elif(role=='engineer') :
                      sal,bonus=new_line[8].split(';')
                      new_Worker=Engineer(newPerson,sal,bonus)
                  elif(role=='sales'):
                      list=new_line[8].split(';')
                      new_Worker=SalesPerson(newPerson,list[0],list[1],list[2:])

                  HelloWorld.insert_branch(new_Worker,new_line[6],self.head.workers)






