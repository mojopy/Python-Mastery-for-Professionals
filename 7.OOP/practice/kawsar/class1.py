'''class parent:
    def func1(self):
        print("This is a parent class.")


class child (parent):
    def func2(self):
        print("This is a child class.")

object = child()
object.func1()
object.func2()


if ( 2% != 0): and (6<=n or n>=20 ):
    print("weird")
else:
    print("Not Weird")'''

def my_func(x,y,z,n):
    my_list = list()
    
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                 if i+j+k != n:
                    my_list.append([i,j,k])
                    
    print(my_list)
   

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    my_func(x,y,z,n)