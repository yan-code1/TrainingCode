# coding:utf-8
import copy
array = [[2],[3,4],[6,5,7],[4,1,5,7]]
# array=[[1],[5,2],[2,7,5],[2,6,4,1]]
a = '11'
b='22'
logging.basicConfig(level=logging.INFO,format='(a)%s,(b)%s')
loger = logging.getLogger('array')
temp =copy.deepcopy(array)
for i in range(len(temp)):
    for key,value in enumerate(temp[i]):
        temp[i][key] = -1

def triangle(array,floor_idx,line_idx):
    if floor_idx == len(array)-1:
        temp[floor_idx][line_idx] = array[floor_idx][line_idx]
        return temp[floor_idx][line_idx]

    if temp[floor_idx][line_idx] == -1:
        temp[floor_idx][line_idx] = min(triangle(array, floor_idx + 1, line_idx), triangle(array, floor_idx + 1, line_idx + 1)) + \
                    array[floor_idx][line_idx]
    # 直接更新每层的最小值会导致选择相邻节点的限制被违背
    # else:
    #     temp[floor_idx] = min(temp[floor_idx], min(triangle(array, floor_idx + 1, line_idx), triangle(array, floor_idx + 1, line_idx + 1)) + \
    #                         array[floor_idx][line_idx])
    loger.info('log:')
    # print('log:', floor_idx, line_idx,array[floor_idx][line_idx])
    return temp[floor_idx][line_idx]
print(triangle(array,0,0))
