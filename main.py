import hwltd.organization
from hwltd.reports import *
def main () :
    #hello_world=hwltd.organization.HelloWorld("prework-python-data.txt")
   # hello_world.print_Hello_World_Structure(hello_world.head,hello_world.head,0)
    #get_num_employees("Hello World",4)
    #print(get_avg_salary("drivers Team"))
    dict =get_relational_salary("Teorge W.")
    for key , value in dict.items( ):
        print(key.Person.first,end=' ')
        print(value)



if __name__ == '__main__':
    main()