from multiprocessing import Process
import os
from time import sleep
import platform

def hijoWindow():
    print("Padre: %d, Hijo: %d\n" %(os.getppid(),os.getpid()))
    sleep(5)
    print("he muerto con %d" %(os.getpid()))
    os._exit(0)
    
def padreWindow():
    numeroHijos = int(input("introduce el numero de procesos que quiere que haya"))
    n = 1
    while n <= numeroHijos:
        p = Process(target=hijoWindow)
        p.start()
        print("Nuevo hijo creado",p.pid)
        p.join(0)
        
        n=n+1
def hijo():
    print("\n >><< Nuevo hijo creado con pid %d " %os.getpid())
    sleep(5)
    print("muerto hijo con pid %d" %os.getpid())
    os._exit(0)

def padre():
    numeroHijos = int(input("introduce un numero de procesos hijos ha crear"))
    n =1
    while n <= numeroHijos:
        newpid = os.fork()
        if newpid == 0:
            hijo()
        else:  
            pids =(os.getpid(),newpid)
            print ("Padre: %d, Hijo: %d\n" % pids)   
           
        n= n+1
if __name__ == '__main__':
    plataforma = platform.platform().split("-")
    if plataforma[0] == "windows":
        padreWindow()
    else:
         padre()