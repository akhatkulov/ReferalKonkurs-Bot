import pandas as pd
import os

def mini_crypt(a: str) -> str:
    l = {'0': 'a', '1': 'x', '2': 'p', '3': 't', '4': 's', '5': 'l', '6': 'r', '7': 'f', '8': 'u', '9': 'e'}
    res = ""
    for char in a:
        res += l[char]
    return res


def mini_decrypt(a: str) -> str:
    l = {'a': '0', 'x': '1', 'p': '2', 't': '3', 's': '4', 'l': '5', 'r': '6', 'f': '7', 'u': '8', 'e': '9'}
    res = ""
    for char in a:
        res += l[char]
    return res



def create_data(file_path: str, name: str, phone: str):
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=['Index', 'Ism', 'Raqam'])
        df.to_excel(file_path, index=False)
    else:

        df = pd.read_excel(file_path)

    new_index = len(df) + 1
    new_data = pd.DataFrame({'Index': [new_index], 'Ism': [name], 'Raqam': [phone]})
    df = pd.concat([df, new_data], ignore_index=True)
    
    df.to_excel(file_path, index=False)
    