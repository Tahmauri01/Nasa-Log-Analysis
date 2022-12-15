from collections import Counter
myFile = open("NASA_access_log_Jul95")

ip_addresses = []
dates = []
directories = []


try:
    for lines in myFile:
        x = lines.split(" ")[0]
        y = lines.split(" ")[3]
        y = y.split(":")[0]
        z = lines.split('"')[1]
        z = z.split('.')[1]
        z = z.split(" ")[0]
        ip_addresses.append(x)
        dates.append(y)
        directories.append(z)

        
        
        #print(lines.split(" ")[0])
        
        #print("uh-oh")
except:
    print("uh oh")



print("The most frequent IP address was " + str(Counter(ip_addresses).most_common(1)))
print("The most frequent date was " + str(Counter(dates).most_common(1))) 
print("The most frequent file type was " + str(Counter(directories).most_common(7)))

