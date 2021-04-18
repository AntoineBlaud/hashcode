
def get_input():
    return input()



def generate_rotate(cards):

    buffer = []

   # rotate 1 time each item and look at list sorted
    for i in range(1, len(cards)+1):
            # do rotation, check results
            card_copy= cards[:len(cards)-i]+tuple((a,not b) for i in range(len(cards)-1,len(cards)-i-1,-1) for a,b in [cards[i]])
            # make next step from this rotation
            buffer.append(card_copy)

    return buffer



def solve(cards):

    stack1 = [cards]
    stack2 = []
    depth = 0
    done = set()
    goal = tuple((i,True) for i in range(1,len(cards)+1))
    if cards == goal:
        return 0


    while stack1:

        cards = stack1.pop()
        for position in generate_rotate(cards):
            if position == goal:
                return depth+1
            if position not in done:
                done.add(position)
                stack2.append(position)
        if not stack1:
            stack1, stack2 = stack2, stack1
            depth+=1
            

if __name__ == '__main__':

    ncard = int(get_input())
    cards_in = get_input().split(" ")
    cards_V_T= tuple((int(a), b=='R') for i in range(ncard) for a,b in [(cards_in[2*i],cards_in[2*i+1])])
    print(solve(cards_V_T))





 