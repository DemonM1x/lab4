import time
import With_hands
import With_lib
import With_reg

t0_hands = time.time()
for i in range(10):
    With_hands.start('Tuesdayj.json','Tuesdayx.xml')
t1_hands = time.time()
print("Time for program (10x) made with hands:", t1_hands - t0_hands, '\n')


t0_lib = time.time()
for i in range(10):
    With_lib.start('Tuesdayj.json', 'Tuesdayx2.xml')

t1_lib = time.time()
print("Time for program (10x) made with libraries:", t1_lib - t0_lib, '\n')

t0_re = time.time()
for i in range(10):
    With_reg.start('Tuesdayj.json', "Tuesdayx3.xml")

t1_re = time.time()
print("Time for program (10x) made with regulars:", t1_re - t0_re, '\n')