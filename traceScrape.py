import subprocess

# list all sites you want to scrap data from as strings within this array
sites = ['facebook.com', 'google.com', 'monoskop.org', 'foodnetwork.com', 'wikipedia.com']

# create file and file name
fileName = "file.txt"
file = open(fileName, "x")
file.close()

# write all traceroute website data to a file, marked with the website name
# at the top of each data chunk
for i in sites:
    ip = subprocess.run(['nslookup', i], stdout=subprocess.PIPE)
    ip = ip.stdout.decode('utf-8')
    ip = ip[ip.find("Name:"):len(ip)]
    ip = ip[(ip.find("Address: ")+9):len(ip)]
    ip = ip[0:len(ip)-2]

    info = subprocess.run(['traceroute', '-I', ip], stdout=subprocess.PIPE)
    info = info.stdout.decode('utf-8')

    file = open(fileName, "a")
    file.write(i[0:len(i)-4])
    file.write('\n')
    file.write(info)

file.close()

# to run: navigate to the diretory holding this file and run:
# python3 traceScrape.py
# the data will be written to a file in this directory
