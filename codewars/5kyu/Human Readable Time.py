def make_readable(seconds):
    return f"{(seconds // 3600):02}:{((seconds % 3600) // 60):02}:{(seconds % 60):02}"


print(make_readable(3599))
print(make_readable(86399))
print(make_readable(59))
print(make_readable(60))
