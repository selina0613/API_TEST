import os
import yaml

def read_yaml(yaml_path):
    with open('register.yaml', encoding='utf-8') as f:
    # with open(os.getcwd()+'/extract.yaml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

# def read_yaml(key):
#     with open('register.yaml', encoding='utf-8') as f:
#     # with open(os.getcwd()+'/extract.yaml', encoding='utf-8') as f:
#         value = yaml.load(stream=f, Loader=yaml.FullLoader)
#         return value[key]

#写入yaml文件,mode='a'表示追加的方式写入
def write_yaml(data):
    with open(os.getcwd()+'/extract.yaml', encoding='utf-8', mode='a') as f:
       yaml.dump(data, stream=f, allow_unicode=True)

#清空yaml文件，mode='w'写入,覆盖写入
def clear_yaml():
    with open(os.getcwd()+'/extract.yaml', encoding='utf-8',mode='w') as f:
       f.truncate()

if __name__ == '__main__':
    print(read_yaml('register.yaml'))