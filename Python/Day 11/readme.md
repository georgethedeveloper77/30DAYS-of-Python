## sheet
# python -i animals.py

>>> Animal
<class '__main__.Animal'>
>>> obj = Animal()
>>> obj
<__main__.Animal object at 0x7fa694ffce80>
>>> obj.noise
'Rrrr'
>>> obj.make_noise()
hello
>>> 

#  python -i animals.py
>>> obj = Animal()
>>> obj.noise
'Rrrr'
>>> obj.make_noise()
Rrrr
>>> Animal().make_noise()
Rrrr
>>> 

#  python -i animals.py
>>> Wolf
<class '__main__.Wolf'>
>>> a = Wolf()
>>> a.make_noise()
grrr
>>> 
 
## python -i templates.py
>>> Template()
Hello there
<__main__.Template object at 0x7f64313b4e80>
>>> 
>>>Template(template_name='hello.txt', context={"name":"Justin"})
<__main__.Template object at 0x7f0185784e80>
>>> 
>>> obj = Template(template_name='hello.txt', context={"name":"Justin"})
>>> obj.context
{'name': 'Justin'}
>>> 
## python -i templates.py
Template(template_name='hello.txt', context={"name":"George"})
tmpl =  Template(template_name='hello.txt', context={"name":"George"})
tmpl.render()
tmpl.render( context={"name":"Abc"})
tmpl 

>>>
obj = Emailer(subject="Hello world", context={"name": "Justin"}, template_name="hello.txt" to_emails={'moodsync0@gmail.com'}, test_send=True)


