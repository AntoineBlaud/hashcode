

def main():
    sum_width, sum_height = 0, 0
    points = []
    size = int(input())
    for _ in range(size):
        nextpoint = tuple(map(int, input().split(" ")))
        points.append(nextpoint)
        sum_width += nextpoint[0]
        sum_height += nextpoint[1]

    width_up , height_down, width_down , height_up = 0, 0, 0, 0
    center_x, center_y = int(sum_height / size), int(sum_width / size)
    for w, h in points:
        # width processing 
        if w < center_x:
            width_down +=  max(0, abs(w -center_x ) - width_down)  
        else:
            width_up += max(0, abs(w - center_x ) - width_up)
        # height processing
        if h < center_y:
            height_down += max(0, abs(h - center_y) - height_down)
        else:
            height_up += max(0, abs(h - center_y) - height_up)
    
    print(width_up + width_down, height_up + height_down)

if __name__ == '__main__':
    main()
