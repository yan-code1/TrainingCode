#问题示例：1.找所给字符串的最大无重复字符长度。或者和不大于s的最短数组
# 字符数组s，索引辅助数组idxList,索引起点 终点，缓存字符序列
def slidWin(array,value):
    start = 0
    end = 0
    result = []
    length = len(array)
    #--------------------------------------
    # 保存所有结果的方式，方便功能扩展，但冗余多
    # while end < length and start < length :
    #     sequence = array[start:end]
    #     if sum(sequence) > value:#大于，保存结果，继续探索更短的
    #         if not start > end:
    #             start += 1
    #             result.append(sequence)
    #         else:
    #             end += 1
    #     else:#小于，不满足条件，扩充
    #         end += 1
    #         continue
    #     print(sequence)
    # temp = len(result[0])
    # temp_idx = 0
    # for i in range(len(result)):
    #     if len(result[i]) < temp:
    #         temp = len(result[i])
    #         temp_idx = i
    #
    # return result[temp_idx]
    #---------------------------------
    # 仅保存需要的结果，求快
    temp = array
    while end < length and start < length :
        sequence = array[start:end]
        if sum(sequence) > value:#大于，保存结果，继续探索更短的
            if not start > end:
                start += 1
                if len(temp) > len(sequence):#若比缓存序列还短，更新
                    temp = sequence
            else:
                end += 1
        else:#小于，不满足条件，扩充
            end += 1
            continue
    return temp
print(slidWin([2,3,2,4,3,3,1,1,2],6))
