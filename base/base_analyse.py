import yaml

def base_analyse(file_name,key):
    file = "./data/" + file_name
    with open(file, "r",encoding="utf-8") as f:
        data= yaml.load(f, Loader=yaml.FullLoader)
        dict_data=data[key]
        list_data=list()
        # print(dict_data)
        for i in dict_data.values():
            list_data.append(i)
        return list_data


if __name__ == '__main__':
    print(base_analyse())
