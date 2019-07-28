

def get_num_employees(department,depth) :

        num_of_workers=len(department.get_workers())
        print(department.name + " -" + num_of_workers + " workers")
        depth-=1
        i=1
        help_get_num(department, depth,1)







def help_get_num(department,depth,i) :
    if(depth==0):
     return

    for item in department.subgroups:
        num_of_workers = len(item.get_workers())
        print('\t' * i, end='')
        print(item.name + " -" + num_of_workers + " workers")
        help_get_num(department,depth-1,i+1)  888888888