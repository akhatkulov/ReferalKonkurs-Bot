import pandas as pd

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


def create_excel_file(filename, data):
    try:
        df = pd.DataFrame(data, columns=['Name', 'Phone Number'])
        df.to_excel(filename, index=False)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    