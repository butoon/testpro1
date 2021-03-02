import yaml


def get_datas():
    with open('data.yml') as f:
        datas = yaml.safe_load(f)
    return datas


print(get_datas())
