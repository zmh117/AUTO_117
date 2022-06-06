import threading,time


class a():

    def a1(self):
        global sos
        for i in range(2):
            sos=str(i)
            time.sleep(1)
            print("a-"+sos)
        return sos

class b(a):


    def b1(self):
        global sos
        for i in range(1000):
            sos=str(i)+"--"+ self.a1()
            print("b-"+sos)
class c():
    global sos

    def c1(self):
        for i in range(1000):
            print( "c-"+sos)
            time.sleep(1)


print(globals())
sos="sss"
t1=threading.Thread(target=b().b1)
t2=threading.Thread(target=c().c1)


t1.start()
t2.start()
