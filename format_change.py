import os

def rename_mp3_files(directory):
    # 检查目录是否存在
    if not os.path.isdir(directory):
        print(f"目录 {directory} 不存在")
        return

    # 获取目录中的所有文件
    files = os.listdir(directory)
    mp3_files = [file for file in files if file.endswith('.mp3')]

    for filename in mp3_files:
        # 构建完整的文件路径
        old_file_path = os.path.join(directory, filename)

        # 找到“ - ”并删除其前面的所有内容
        if ' - ' in filename:
            new_filename = filename.split(' - ', 1)[1].strip()
            new_file_path = os.path.join(directory, new_filename)

            # 检查新文件名是否已经存在，避免重命名冲突
            if os.path.exists(new_file_path):
                print(f"跳过: {new_filename} 已经存在")
                continue

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"重命名: {filename} -> {new_filename}")
        else:
            print(f"跳过: {filename} 不包含指定的分隔符")

# 示例使用
directory_path = r'C:\Users\Ziyang Chen\Desktop\music'  # 替换为你的MP3文件目录路径

rename_mp3_files(directory_path)

print("重命名完成")
