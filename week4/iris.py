 # 提取花的名字
flower_names = []
start_extracting = False

with open('/mnt/data/iris.names', 'r') as file:
    for line in file:
        # 检测开始部分
        if "class:" in line.lower():
            start_extracting = True
            continue
        
        # 检测结束部分
        if start_extracting:
            if line.strip() == "":
                break  # 遇到空行停止
            flower_names.append(line.strip().replace("--", "").strip())

print("Flower Names:")
print(flower_names)
