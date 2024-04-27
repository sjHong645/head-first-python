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

        # 딕셔너리 컴프리헨션 적용
        fts = {line.strip().split(',')[0] : line.strip().split(',')[1] for line in data}
                
pprint.pprint(flights)
print()



for key in flights : 
    
    ampm = convert2ampm(key)
    
    # 시간을 ampm으로 변환 & 목적지의 앞 글자만 대문자로 나머지는 소문자로 변환
    flights2 = {}
    for k, v in flights.items() : 
        flights2[convert2ampm(k)] = v.title()

    # 딕셔너리 컴프리헨션 적용
    fts2 = {convert2ampm(k) : v.title() for k, v in flights.items()}
    
    """ if flights[key].title() in flights2 : 
        
        flights2[flights[key].title()].append(ampm)
        
    flights2.setdefault(flights[key].title(), [ampm, ]) """
    
pprint.pprint(flights2)


flight_times = []
for ft in flights.keys() : 
    flight_times.append(convert2ampm(ft))

print(flight_times)

destinations = []
for dest in flights.values() : 
    destinations.append(dest.title())

print(destinations)