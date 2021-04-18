import re 

def convert_into_cm(value, unit):
    if unit == 'mm':
        return value/10
    if unit == 'cm':
        return value
    if unit == 'dm':
        return 10 * value;
    if unit == 'm':
        return 10**2 * value;
    if unit == 'dam':
        return 10**2*10*value
    if unit == 'hm':
        return 10**2*10**2*value
    if unit == 'km':
        return 10**2*10**3*value


n = int(input())
minu, maxi, pminu, pmaxi  = None,None,None,None
pointer = 1
for _ in range(n):
    s = input()
    value = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)
    unit = re.findall('(?:cm|dam|km|dm|mm|m|hm)', s )
    value = convert_into_cm(float(value[0]), unit[0])
    if minu == None or value < minu:
        minu = value
        pminu= pointer
    if maxi== None or value > maxi:
        maxi= value
        pmaxi = pointer

    pointer+=1

print("{} {}".format(pminu,pmaxi))