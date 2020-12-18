src_file = open("1.jpg", "rb")
target_file = open("copy1.jpg", "wb")

target_file.write(src_file.read())

target_file.close()
src_file.close()
