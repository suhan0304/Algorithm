import sys
input = sys.stdin.readline

t = int(input())

def rotate_direction(cube, d):
    for _ in range(2):
        temp = cube[d][0][0]
        cube[d][0][0] = cube[d][1][0]
        cube[d][1][0] = cube[d][2][0]
        cube[d][2][0] = cube[d][2][1]
        cube[d][2][1] = cube[d][2][2]
        cube[d][2][2] = cube[d][1][2]
        cube[d][1][2] = cube[d][0][2]
        cube[d][0][2] = cube[d][0][1]
        cube[d][0][1] = temp

def rotate(cube, command) : 
    direction, cnt = command
    cnt = 1 if cnt == '+' else 3
    for _ in range(cnt) :
        move(cube, direction)

def move(cube, direction) :
    if direction == 'U' :
        tmp = cube['f'][0]
        cube['f'][0] = cube['r'][0]
        cube['r'][0] = cube['b'][0]
        cube['b'][0] = cube['l'][0]
        cube['l'][0] = tmp
        rotate_direction(cube,'u')

    elif direction == 'D' :
        tmp = cube['f'][2]
        cube['f'][2] = cube['l'][2]
        cube['l'][2] = cube['b'][2]
        cube['b'][2] = cube['r'][2]
        cube['r'][2] = tmp
        rotate_direction(cube,'d')

    elif direction == 'F' :
        temp = cube['u'][2]
        cube['u'][2] = [cube['l'][2][2], cube['l'][1][2], cube['l'][0][2]]
        cube['l'][0][2], cube['l'][1][2], cube['l'][2][2] = cube['d'][0]
        cube['d'][0] = [cube['r'][2][0], cube['r'][1][0], cube['r'][0][0]]
        cube['r'][0][0], cube['r'][1][0], cube['r'][2][0] = temp
        rotate_direction(cube,'f')

    elif direction == 'B' :
        temp = cube['u'][0]
        cube['u'][0] = [cube['r'][0][2], cube['r'][1][2], cube['r'][2][2]]
        cube['r'][2][2], cube['r'][1][2], cube['r'][0][2] = cube['d'][2]
        cube['d'][2] = [cube['l'][0][0], cube['l'][1][0], cube['l'][2][0]]
        cube['l'][2][0], cube['l'][1][0], cube['l'][0][0] = temp
        rotate_direction(cube,'b')

    elif direction == 'L' :
        temp = [cube['f'][0][0], cube['f'][1][0], cube['f'][2][0]]
        cube['f'][0][0], cube['f'][1][0], cube['f'][2][0] = cube['u'][0][0], cube['u'][1][0], cube['u'][2][0]
        cube['u'][0][0], cube['u'][1][0], cube['u'][2][0] = cube['b'][2][2], cube['b'][1][2], cube['b'][0][2]
        cube['b'][0][2], cube['b'][1][2], cube['b'][2][2] = cube['d'][2][0], cube['d'][1][0], cube['d'][0][0]
        cube['d'][0][0], cube['d'][1][0], cube['d'][2][0] = temp
        rotate_direction(cube,'l')

    elif direction == 'R' :
        temp = [cube['f'][0][2], cube['f'][1][2], cube['f'][2][2]]
        cube['f'][0][2], cube['f'][1][2], cube['f'][2][2] = cube['d'][0][2], cube['d'][1][2], cube['d'][2][2]
        cube['d'][0][2], cube['d'][1][2], cube['d'][2][2] = cube['b'][2][0], cube['b'][1][0], cube['b'][0][0]
        cube['b'][0][0], cube['b'][1][0], cube['b'][2][0] = cube['u'][2][2], cube['u'][1][2], cube['u'][0][2]
        cube['u'][0][2], cube['u'][1][2], cube['u'][2][2] = temp
        rotate_direction(cube,'r')



for __ in range(t) :

    cube = {
        'u':[['w' for _ in range(3)] for _ in range(3)],
        'd':[['y' for _ in range(3)] for _ in range(3)],
        'f':[['r' for _ in range(3)] for _ in range(3)],
        'b':[['o' for _ in range(3)] for _ in range(3)],
        'l':[['g' for _ in range(3)] for _ in range(3)],
        'r':[['b' for _ in range(3)] for _ in range(3)]
    }

    n = int(input())
    commands = list(map(str, input().split()))
    for command in commands :
        rotate(cube, command)


    for i in range(3):
        for j in range(3):
            print(cube['u'][i][j],end="")
        print()