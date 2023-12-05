print('2023 - Day 5')

with open('./2023/Day5/input.txt') as file:
    lines = [line.rstrip() for line in file]

seeds=[]
seed2soil=[]
soil2fertilizer=[]
fert2water=[]
water2light=[]
light2temp=[]
temp2hum=[]
hum2location=[]

for i,line in enumerate(lines):
    if 'seeds:' in line:
        seeds = [int(n) for n in line.split(':')[1].strip().split()]
    if 'seed-to-soil' in line:
        for line_ in lines[i+1:]:
            if line_=='':
                break
            seed2soil.append([int(n) for n in line_.split()])
        continue
    if 'soil-to-fertilizer' in line:
        for line_ in lines[i+1:]:
            if line_=='':
                break
            soil2fertilizer.append([int(n) for n in line_.split()])
        continue
    if 'fertilizer-to-water' in line:
        for line_ in lines[i+1:]:
            if line_=='':
                break
            fert2water.append([int(n) for n in line_.split()])
        continue
    if 'water-to-light' in line:
        for line_ in lines[i+1:]:
            if line_=='':
                break
            water2light.append([int(n) for n in line_.split()])
        continue
    if 'light-to-temperature' in line:
        for line_ in lines[i+1:]:
            if line_=='':
                break
            light2temp.append([int(n) for n in line_.split()])
        continue
    if 'temperature-to-humidity' in line:
        for line_ in lines[i+1:]:
            if line_=='':
                break
            temp2hum.append([int(n) for n in line_.split()])
        continue
    if 'humidity-to-location' in line:
        for line_ in lines[i+1:]:
            if line_=='':
                break
            hum2location.append([int(n) for n in line_.split()])
        continue

seed2soil.sort(key=lambda k: k[1])

def convert(input,conversionlist):
    conversionlist.sort(key=lambda k: k[1])
    output = [-1]*len(input)
    for i,obj in enumerate(input):
        for item in conversionlist:
            if item[1]<=obj<=item[1]+item[2]:
                p = obj-item[1]
                output[i] = item[0]+p
                break
        if output[i]==-1:
            output[i]=obj
    return output

def convertrange(input,conversionlist):
    input_=input.copy()
    conversionlist.sort(key=lambda k: k[1])

    output = []

    while len(input_)>0:
        start = input_.pop(0)
        rang = input_.pop(0)
        if start<conversionlist[0][1]:
            if start+rang<conversionlist[0][1]:
                output.extend([start,rang])
            else:
                output.extend([start,conversionlist[0][1]-start])
                input_.insert(0,rang-(conversionlist[0][1]-start))
                input_.insert(0,conversionlist[0][1])
        elif start>conversionlist[-1][1]+conversionlist[-1][2]:
            output.extend([start,rang])
        else:
            for item in conversionlist:
                if item[1]<=start<item[1]+item[2]: # Start is in this range of conversion
                    p = start-item[1]
                    start_ = item[0]+p
                    if item[1]<=start+rang<=item[1]+item[2]:
                        rang_ = rang
                    else:
                        rang_ = item[1]+item[2]-start
                        input_.insert(0,rang-rang_)
                        input_.insert(0,item[1]+item[2])
                    output.extend([start_,rang_])
                    break
    return output



soils = convert(seeds,seed2soil)
ferts = convert(soils,soil2fertilizer)
waters = convert(ferts,fert2water)
lights = convert(waters,water2light)
temps = convert(lights,light2temp)
hums = convert(temps,temp2hum)
locations = convert(hums,hum2location)

soils2 = convertrange(seeds,seed2soil)
ferts2 = convertrange(soils2,soil2fertilizer)
waters2 = convertrange(ferts2,fert2water)
lights2 = convertrange(waters2,water2light)
temps2 = convertrange(lights2,light2temp)
hums2 = convertrange(temps2,temp2hum)
locations2 = convertrange(hums2,hum2location)

print('------------------------')
print('Part 1:',min(locations))
print('------------------------')
print('Part 2:',min(locations2[::2]))
print('------------------------')