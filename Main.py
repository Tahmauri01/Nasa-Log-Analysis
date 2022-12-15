from collections import Counter
myFile = open("NASA_access_log_Jul95")

ip_addresses = []

try:
    for lines in myFile:
        x = lines.split(" ")[0]
        ip_addresses.append(x)

        
        
        #print(lines.split(" ")[0])
        
        #print("uh-oh")
except:
    print("uh oh")

print(Counter(ip_addresses))

