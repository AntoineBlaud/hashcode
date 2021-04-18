def find_first(altitude_reading):
    start = altitude_reading[0]
    index = 0
    while(len(altitude_reading) > index):
        if(altitude_reading[index] > start):
            return 1
        if(altitude_reading[index] < start):
            return -1
        index += 1
    return 0

def up(altitude_reading, index):
    while(len(altitude_reading)  - 1 > index):
        if(altitude_reading[index + 1] < (altitude_reading[index])):
            return index
        index += 1
    return index + 1


def down(altitude_reading, index):
    while(len(altitude_reading) - 1 > index):
        if(altitude_reading[index + 1] > (altitude_reading[index])):
            return index
        index += 1
    return index + 1

def main():
    altitude_reading = list(map(int, input().split(" ")))
    count, index = 0, 0 
    first = find_first(altitude_reading)
    if first > 0:
        s = [up, down]
    elif first < 0:
        s = [down, up]
    else:
        return 1
    
    while(index < len(altitude_reading)):
        index = s[0](altitude_reading, index)
        count+=1
        s = s[::-1]
    return count
    

if __name__ == '__main__':
    print(main())

