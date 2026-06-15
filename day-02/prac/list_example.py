a=[200,400,600,True,4.6] #List @mthod1
print(type(a))
a.append(500)
print(a)
clouds=list() #list @method2
clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("oracle")
clouds.append("utho")
print(clouds)
print("Length of list is:",len(clouds))
print("World Leader for Cloud Provider is",clouds[0])
print("Indian Cloud Service provider is:",clouds[-1])
print((clouds.count.__doc__)) # get all list descriptions
print(clouds.reverse.__doc__) # get reverse details
print(clouds.extend.__doc__) 
for cloud in clouds:
    print(cloud)
    if cloud=="aws":
        print(f"{cloud} Market leader")
    elif cloud=="utho":
        print(f"{cloud}Indian Cloud")
    elif cloud=="azure" or cloud=="gcp":
        print(f"{cloud} DevOps- will cover in batch 10")
    else:
        print("No cloud available")
