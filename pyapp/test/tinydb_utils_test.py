from tinydb import TinyDB, Query, table

db = TinyDB('pyflow_data.json', indent=2)
_ = Query()

# 插入数据
# db.insert({'name': 'John', 'birthday': {'year': 2020}})
# db.insert({'name': 'Mark', 'birthday': {'year': 2018}})
# db.insert_multiple([
#     {'name': 'John', 'age': 22, 'role': ['admin']},
#     {'name': 'Mark', 'age': 37, 'role': ['sudo', 'admin']}
# ])

# 查询
# print(db.search(_.name == 'John'))
# print(db.search(_.name.exists()))

# 筛选
# print(db.search(_.role.any(['sudo', 'admin'])))

# 组合条件查询
# db.search((_.name == 'John') & (_.age <= 30))
# print(db.search((_.name == 'John') | (_.name == 'Mark')))


# UID_KEY_NAME = 'uid'
# CONFIG_KEY = 'config'

# db.upsert({UID_KEY_NAME: CONFIG_KEY,'password': 'xxx'}, _[UID_KEY_NAME] == CONFIG_KEY)
# print(db.get(_[UID_KEY_NAME] == CONFIG_KEY)) # 只获取一个

# 配置表
# config = db.table('config')
# config.insert({ "password": "xxx"})
# config.insert({ "password": "yyy"})

# config.remove(_.password == "xxx")
# print(config.all())
