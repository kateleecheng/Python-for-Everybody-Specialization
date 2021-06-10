#Week_6_Class.py
import json

data='''{
"name":"Chuck",
"phone":{
    "type":"intl",
    "number":"+1 734 303 4456"
    },
"email":{
    "hide":"yes"
    }
}'''

info=json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

#Name: Chuck
#Hide: yes
import json

input='''[

    {"id":"001",
    "x":"2",
    "name":"Chuck"},
    {"id":"009",
    "x":"7",
    "name":"Chuck"}
]'''

info2=json.loads(input)
print(info2)
#[{'id': '001', 'x': '2', 'name': 'Chuck'}, {'id': '009', 'x': '7', 'name': 'Chuck'}]
print('User count:', len(info2))
for item in info2:
    print('Name',item['name'])
    print('Id',item['id'])
    print('Attribute',item['x'])

#User count: 2
#Name Chuck
#Id 001
#Attribute 2
#Name Chuck
#Id 009
#Attribute 7
