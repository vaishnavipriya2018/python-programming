d={"Eno":123,"Ename":"abc"}
print(d)
print(d["Eno"])
print(d.get("Ename"))
d["Ename"]="xyz"
print(d)
d["age"]=17
print(d)
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,':',value)
d.pop("Eno")
print(d)
d.popitem()
print(d)
d.clear()
print(d)

