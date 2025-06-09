import hello as ho
import package.module_01 as pm1
from package.module_01 import say_hello


ho.say_hello()

print(ho.x)

from hello import say_hello
say_hello()

from hello import say_hello,greeting
print(greeting)

say_hello()

say_hello()
