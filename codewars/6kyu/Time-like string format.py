def solution(hour):
    hour = str(hour)
    if len(hour) < 3 or len(hour) > 4:
        raise "Function should raise an exception"
    
    return f"{hour[0]}:{hour[1:]}" if len(hour) == 3 else f"{hour[:2]}:{hour[2:]}"