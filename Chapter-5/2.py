#Dictionary Methods
dict={
    "shahid":100,
    "rohan":90,
    "aryan":80
}
print(dict.items())

print(dict.keys())

print(dict.values())

dict.update({"shahid":99,"renuka":100})
print(dict)

print(dict.get("shahid"))
print(dict["rohan"])