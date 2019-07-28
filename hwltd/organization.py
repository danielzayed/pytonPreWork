from workers.structure import Group
from workers.Person import *

company = Group("HelloWorld", 'company Head Department', None)# company helloworld
# defining the sub groups of company
eng_dep = Group("Engineering Department","Engineering Head Department - responsible for all company's Engineering Aspects",company)
hr_dep =  Group("Hr Department","hr Head Department",company)
fin_dep=Group("Finance Department","Finance Department",company)
# insert  subgroups for company ( HelloWorld)
company.innerlist.append(eng_dep)
company.innerlist.append(hr_dep)
company.innerlist.append(fin_dep)
# defining the sub groups of eng_dep
sw_group=Group("SW Group","Software Group!",eng_dep)
hw_group=Group("HW Group","Hardware Group!!",eng_dep)
cto_group=Group("Cto Group","Cto Group!",eng_dep)
sys_group=Group("Sys Group","System Group",eng_dep)
# insert  subgroups for eng_dep
eng_dep.innerlist.append(sw_group)
eng_dep.innerlist.append(hw_group)
eng_dep.innerlist.append(cto_group)
eng_dep.innerlist.append(sys_group)
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
sw_group.innerlist.append(inf_team)
sw_group.innerlist.append(app_team)
sw_group.innerlist.append(dri_team)
sw_group.innerlist.append(qa_team)
# insert subgroups for hw group
hw_group.innerlist.append(chip_team)
hw_group.innerlist.append(broad_team)
hw_group.innerlist.append(power_team)
# insert subgroups for sys group
sys_group.innerlist.append(des_team)
sys_group.innerlist.append(poc_team)
# defining the sub groups of hr_dep
rec_group= Group("recruitment Group","recruitment Group-Hr Dep",hr_dep)
cul_group= Group("culture Group","culture Group-Hr Dep",hr_dep)
#inserting the sub groups of hr_dep
hr_dep.innerlist.append(rec_group)
hr_dep.innerlist.append(cul_group)
# defining the sub groups of rec_group
tech_team=Group("tech Team","Tech team-rec group",rec_group)
staff_team=Group("staff Team" , "Staff team-rec-group",rec_group)
# inserting the sub groups of rec_group
rec_group.innerlist.append(tech_team)
rec_group.innerlist.append(staff_team)
# defining the sub groups of fin_dep
sal_group=Group("salary Group","Salary Group-Finance dep",fin_dep)
bud_group=Group("budget Group","Budget Group-Finance dep",fin_dep)
# inserting hte sub groups of fin_dep
fin_dep.innerlist.append(sal_group)
fin_dep.innerlist.append(bud_group)
# defining the sub groups of bud_group
inc_team=Group("income Team","Income Team-Budget group",bud_group)
out_team=Group("outcome Team","Outcome Team -Budget group",bud_group)
#inserting the sub groups of bud_groups
bud_group.innerlist.append(inc_team)
bud_group.innerlist.append(out_team)


class Employees:
    def __init__(self,employees={}):
        self.employees=employees

class HelloWorld:
   head=company
   theEmployees=Employees({})
   def __init__(self,path_file):
       with open(path_file,'r') as f :
           for line in f :
               if(line[0]!='#'):
                  new_line=line.split(',')
                  name=new_line[1]
                  email=new_line[3]
                  HelloWorld.theEmployees.employees[email]=name
                  list_ph=new_line[4].split(';')
                  address=new_line[5].split(';')
                  if(len(address==4)) :  # then it is astreet address Baby!!
                     The_address=StreetAddress(address[0],address[1],address[2],address[3])

                  else :
                      The_address=PobAddress(address[0],address[1],address[2])
                  newPerson=Person.New_Person(name,new_line[0],new_line[2],email,list_ph,The_address)


   def find_branch(self, worker, dep_name, group):
       if type(group.list_under[0]) != Group:
          return
       for i in group.subgroups:
            if i.name == dep_name:
                i.subgroups.append(worker)
               self.find_branch(worker, dep_name, group.list_under[i])



