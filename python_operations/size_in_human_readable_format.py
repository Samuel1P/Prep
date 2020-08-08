def humanize_size(sizen):
    for i in ["B", "KiB", "MiB", "GiB", "TiB","PiB"]:
        if sizen < 1024:
            break
        sizen = sizen / 1024
    return f"{sizen:.2f} {i}"
byte_size = 65432876987
print (humanize_size(byte_size))