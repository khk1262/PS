from pyo import *
from genetic import generate_genome, Genome

s = Server()
s.boot()
s.start()

s.amp = 0.1
a = Sine().out()

s.gui(locals())