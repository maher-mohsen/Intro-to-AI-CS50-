
from xml.sax.saxutils import prepare_input_source
from logic import *
rain = Symbol("rain")
hagrid= Symbol("hagrid")
dumbledore=Symbol("dumbledore")
knowledge= And( Implication(Not(rain),hagrid), Or(hagrid,dumbledore), Not(And(hagrid,dumbledore)), 
               dumbledore)
print(knowledge.formula())
print(model_check(knowledge,rain))