
#f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD2/AllSums/1.in", 'r')


def get_input():
    return input().strip()
    #return f.readline().strip()



if __name__ == '__main__':

    n,ns = map(int, get_input().split(" "))
    values = list(map(int, get_input().split(" ")))
    done = {}
    s,done[-1]  = 0,0
    for i,v in enumerate(values):
        s+=v
        done[i] = s

    for _ in range(ns):
        borneinf, bornesup = map(int,get_input().split(" "))
        print(done[bornesup] - done[borneinf-1])
    

    

    

    


    