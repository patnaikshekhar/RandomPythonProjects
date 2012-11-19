import threading

class MyThread(threading.Thread):
    def run(self):
        print 'Insert some threads stuff here'
        print 'It will be executed'
        print 'Thread completed already'

for i in range(2):
    x = MyThread()
    x.start()

print "Random text"

