info={
    "name": "Manish Kumar", #string
    "City": "Delhi", #string
    "highest qualification": "MCA", #string
    "age":40, #int
    "salary":3.8, #float
    "marritial status": True, #bool
    "favourites":["movie","reading","playing"]
}
print("I live in",info["City"]) 
print("I love",info["favourites"])
print("I love",info.get("favorites","not found")) # error not coming
info.update({"email":"manish2801kumar@gmail.com"})

print(info.get.__doc__)

for key,value in info.items():
    print(key,value)

