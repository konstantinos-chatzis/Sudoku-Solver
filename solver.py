dock = [0,  0,  0,   6,  0,  0,   0,  0,  0,
        5,  0,  8,   0,  0,  0,   0,  0,  1,
        0,  0,  0,   0,  9,  1,   0,  0,  5,

        0,  0,  0,   0,  0,  0,   5,  0,  3,
        3,  4,  0,   8,  0,  0,   6,  0,  0,
        0,  0,  0,   4,  0,  7,   0,  0,  0,
        
        9,  0,  0,   3,  2,  4,   0,  0,  0,
        0,  0,  7,   0,  0,  0,   0,  1,  0,
        6,  0,  0,   0,  0,  0,   0,  0,  2]

#BOXES
box1_indexes = [0,1,2,9,10,11,18,19,20]
box2_indexes = [3,4,5,12,13,14,21,22,23]
box3_indexes = [6,7,8,15,16,17,24,25,26]

box4_indexes = [27,28,29,36,37,38,45,46,47]
box5_indexes = [30,31,32,39,40,41,48,49,50]
box6_indexes = [33,34,35,42,43,44,51,52,53]

box7_indexes = [54,55,56,63,64,65,72,73,74]
box8_indexes = [57,58,59,66,67,68,75,76,77]
box9_indexes = [60,61,62,69,70,71,78,79,80]

boxes = [box1_indexes, box2_indexes, box3_indexes, box4_indexes, box5_indexes, box6_indexes, box7_indexes, box8_indexes, box9_indexes]


#ROWS
row1_indexes = [0,1,2,3,4,5,6,7,8]
row2_indexes = [9,10,11,12,13,14,15,16,17]
row3_indexes = [18,19,20,21,22,23,24,25,26]

row4_indexes = [27,28,29,30,31,32,33,34,35]
row5_indexes = [36,37,38,39,40,41,42,43,44]
row6_indexes = [45,46,47,48,49,50,51,52,53]

row7_indexes = [54,55,56,57,58,59,60,61,62]
row8_indexes = [63,64,65,66,67,68,69,70,71]
row9_indexes = [72,73,74,75,76,77,78,79,80]

rows = [row1_indexes, row2_indexes, row3_indexes, row4_indexes, row5_indexes, row6_indexes, row7_indexes, row8_indexes, row9_indexes]

#COLUMNS
col1_indexes = [0,9,18,27,36,45,54,63,72]
col2_indexes = [1,10,19,28,37,46,55,64,73]
col3_indexes = [2,11,20,29,38,47,56,65,74]

col4_indexes = [3,12,21,30,39,48,57,66,75]
col5_indexes = [4,13,22,31,40,49,58,67,76]
col6_indexes = [5,14,23,32,41,50,59,68,77]

col7_indexes = [6,15,24,33,42,51,60,69,78]
col8_indexes = [7,16,25,34,43,52,61,70,79]
col9_indexes = [8,17,26,35,44,53,62,71,80]

columns = [col1_indexes, col2_indexes, col3_indexes, col4_indexes, col5_indexes, col6_indexes, col7_indexes, col8_indexes, col9_indexes]

def check_legal(number, cell_index):
    for box in boxes:
        for index in box:
            if index == cell_index:
                cell_box = box
                break
            else:
                continue

    for row in rows:
        for index in row:
            if index == cell_index:
                cell_row = row
                break
            else:
                continue

    for column in columns:
        for index in column:
            if index == cell_index:
                cell_column = column
                break
            else:
                continue

    for index in cell_box:
        if dock[index] == number:
            return False
    
    for index in cell_row:
        if dock[index] == number:
            return False

    for index in cell_column:
        if dock[index] == number:
            return False

    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_dock = dock

def solve():
    for row in rows:
        for index in row:
            if dock[index] == 0:
                for number in numbers:
                    if check_legal(number, index):
                        new_dock[index] = number
                        solve()
                        new_dock[index] = 0

                return
    print(new_dock)

solve()
