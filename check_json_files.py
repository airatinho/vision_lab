import json
PATH_TO_JSON_1= "files/name.json"
PATH_TO_JSON_2= "files/name1.json"
def check_equal_json(path_to_file_1:str,path_to_file_2:str)->bool:
    """Load and check equality of json-s pair"""
    file_json_1 =json.load(open(path_to_file_1, encoding='utf-8'))
    file_json_2 =json.load(open(path_to_file_2, encoding='utf-8'))
    if len(file_json_1)!=len(file_json_2):
        return False
    else:
        for i in file_json_1.keys():
            if not isinstance(file_json_1[i],type(file_json_2[i])):
                return False
            else:
                if not isinstance(file_json_1[i],str):
                    if round(file_json_1[i],5)!=round(file_json_2[i],5):
                        return False
                elif file_json_1[i] != file_json_2[i]:
                    return False
    return True
if __name__ == '__main__':
    print(check_equal_json(PATH_TO_JSON_1,PATH_TO_JSON_2))
