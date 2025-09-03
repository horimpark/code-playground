def shortener(message):
    split_msgs = message.split(' ')
    margin = len(message) - 160
    if margin <= 0:
        return message
    
    res = ""
    res += ' '.join(split_msgs[:-margin])
    res += ''.join([f"{x[0].upper()}{x[1:]}" for x in split_msgs[-margin:]])
    return res
    