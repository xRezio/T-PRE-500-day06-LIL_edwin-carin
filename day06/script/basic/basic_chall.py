import time
a = time.time_ns()
def c(x):
    print(42**x)
(c(651651651651))
b = time.time_ns()- a
 
print(b)