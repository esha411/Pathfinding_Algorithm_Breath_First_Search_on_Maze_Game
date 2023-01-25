from PIL import Image
from ImageHandle import *
from Coordinate import *


yet_to_see = []
already_seen = []

sur_nodes = ((-1,0),(0,-1),(0,1),(1,0))

def bfs_img(img: Image) -> Image:

    matrix = imgToMatrix(img)
    start, goal = find_start_end(matrix)
    yet_to_see.append(Coordinate(start[0],start[1], None))
    goal_node = None

    while yet_to_see:

        cur_node = yet_to_see[0]
        del yet_to_see[0]
        
        found = False

        for r in sur_nodes:
            t_y = cur_node.y + r[0]
            t_x = cur_node.x + r[1]

            if matrix[t_y][t_x] != 'B' and not check_seen_coord(t_y,t_x):
                    tmp_node = Coordinate(t_y,t_x,cur_node)
                    yet_to_see.append(tmp_node)

                    if matrix[t_y][t_x] == 'F':
                        goal_node = tmp_node
                        found = True


        matrix[cur_node.y][cur_node.x] = 'A'

        if found:
            break

        already_seen.append(cur_node)


    if goal_node is not None:
        print("Path found in "+str(goal_node.count)+" steps.")
    else:
        print("Didn't find path to goal node!")

    while goal_node is not None:
        matrix[goal_node.y][goal_node.x] = 'P'
        goal_node = goal_node.parent

    matrix[start[0]][start[1]] = 'S'
    matrix[goal[0]][goal[1]] = 'F'

    outputImg = matrixToImg(matrix)

    return outputImg

def find_start_end(matrix: list) -> list:
    out = [(),()]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 'S':
                out[0] = (y,x)
            if matrix[y][x] == 'F':
                out[1] = (y,x)
    if out[0] == () or out[1] == ():
        print("Could not find Start/End")
    return out
    
def check_seen_coord(y:int, x:int) -> bool:
    for i in range(len(already_seen)):
        if already_seen[i].y == y and already_seen[i].x == x:
            return True

    for i in range(len(yet_to_see)):
        if yet_to_see[i].y == y and yet_to_see[i].x == x:
            return True
    return False


def main():
    maze_name = input("Enter the name of maze to search: ")
    img = Image.open("/Users/devumeshkumarparmar/Desktop/AI_Innovative/TestMazes/"+maze_name)
    result_img = bfs_img(img)
    result_img.show()

if __name__ == "__main__":
    main()
