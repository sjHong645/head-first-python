from datetime import datetime
import pprint

def convert2ampm(time24 : str) -> str : 
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data : 
        ignore = data.readline()
        flights = {}
        for line in data :
                k, v = line.strip().split(',')
                flights[k] = v
                
pprint.pprint(flights)
print()

flights2 = {}

for key in flights : 
    
    ampm = convert2ampm(key)
    
    # 시간을 ampm으로 변환 & 목적지의 앞 글자만 대문자로 나머지는 소문자로 변환
    for k, v in flights.items() : 
        flights2[convert2ampm(k)] = v.title()
    
    """ if flights[key].title() in flights2 : 
        
        flights2[flights[key].title()].append(ampm)
        
    flights2.setdefault(flights[key].title(), [ampm, ]) """
    
pprint.pprint(flights2)