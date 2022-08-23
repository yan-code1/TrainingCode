def get_dev_info(str, start, end):
    things = list()
    while True:
        start_pos = str.find(start)
        if start_pos == -1:
            break

        end_pos = str.find(end)
        if end_pos == -1:
            break
        while True:
            startAnotherPos = str.find(start, start_pos + 1)
            if startAnotherPos == -1:
                break
            if startAnotherPos < end_pos:
                start_pos = startAnotherPos
            if start_pos > end_pos:
                end_another_pos = str.find(end, end_pos + 1)
                end_pos = end_another_pos
            else:
                break
        sub_str = str[start_pos:end_pos] + end
        things.append(sub_str)
        str = str[end_pos + len(end):]
    things_final = list()
    for thing in things:
        if thing.startswith(start):
            str_del_start = thing.replace(start,'')
            things_final.append(str_del_start.replace(end,''))
    return things_final
