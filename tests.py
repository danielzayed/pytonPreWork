import json
from workers.Person import *
new_Address=PobAddress("israel","jersaluem",10)
new_phone=Phone("097-098O98")
print(new_phone.phone)
print(new_Address.ret_address())
new_person=Person.New_Person("donalad","trump",1995,"ptheneighbors@web.africa.mgmt.hwltd.com",new_phone,new_Address)
print(new_person.email)

'''
with open('hwltd/structure_organization.json') as hello:
    j_obj = json.load(hello)
    hello_world_dict = j_obj['Company']
    for key ,value in hello_world_dict.items():
        print(key)
        pri
        for x in  i  :
            print(x)

'''


@staticmethod
def print_Hello_World_Structure(head, helloworld_head, i):
    if (not isinstance(head,Group)):
        return
    if (head.workers == [] or head.workers == None):
        return
    if (head.name == helloworld_head.name):
        print('\t' * i + head.name)
        i = i + 1

    for group in head.workers:
        if (not isinstance(group, Group)):
            print('\t' * i + group.Person.name)
        else:
            print('\t' * i + group.name)
        HelloWorld.print_Hello_World_Structure(group, helloworld_head, i + 1)