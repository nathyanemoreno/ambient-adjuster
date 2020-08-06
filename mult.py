from multiprocessing import Process, Queue, Pool
import os  

def f(q):
    q.put([42, None, 'hello'])

def run_process(process):     
    os.system('python {}'.format(process)) 

if __name__ != '__main__':
	'''q = Queue()
	p = Process(target=f, args=(q,))
	p.start()
	print (q.get())    # prints "[42, None, 'hello']"
	p.join()'''
	processes = ('simulateTemp.py')
	other = ('process3.py',)
	pool = Pool(processes=1)
	pool.map(run_process, processes) 
	'''pool.map(run_process, other)'''

