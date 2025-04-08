


def ipv4_address(address):
    print(address)
    address = address.split('.')
    
    try:
        addr = [int(x) for x in address]
    except:
        return False
    if len(address) != 4:
        return False
    if any(x>255 or x < 0 for x in addr):
        return False
    if any(str(x)!=address[i] for i, x in enumerate(addr)):
        return False
    
    return True
    
