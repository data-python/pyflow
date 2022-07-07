from tinydb import TinyDB, Query
from tinydb.table import Document
from tinydb.operations import delete

# db = TinyDB('pyflow_data.json')
# db = TinyDB('pyflow_data.json', indent=2)
db = TinyDB('pyflow_data.json')
_ = Query()

UID_KEY_NAME = "_uid"

# 查询全部
def list_table(table_name):
    table = db.table(table_name)
    return table.all()

# 获取第一个元素
def get_table(table_name):
    table = db.table(table_name)
    res = table.all() 
    if len(res) > 0:
        return res[0]       
    return None

# 获取第一个元素
def get_table_first(table_name):
    return get_table(table_name)

# 获取最后一个元素
def get_table_last(table_name):
    table = db.table(table_name)
    res = table.all() 
    if len(res) > 0:
        return res[0]   
    return None

# 按键值查询
def get_table_by_condition(table_name, key, value):
    table = db.table(table_name)
    return table.get(_[key] == value)

# 插入一条数据
def insert_table(table_name, data):
    table = db.table(table_name)
    return table.insert(data)

# 插入多条数据
def insert_table_multiple(table_name, array):
    table = db.table(table_name)
    return table.insert_multiple(array)

# @todo 选择UID更新
# def update_table_by_uid(table_name, data, uid):
#     table = db.table(table_name)
#     data[UID_KEY_NAME] = uid
#     return table.update(data, _[UID_KEY_NAME] == uid)

def update_table_by_condition(table_name, data, key, value):
    table = db.table(table_name)
    return table.update(data, _[key] == value)

# 按ID插入或更新
def upsert_table(table_name, data, id):
    table = db.table(table_name)
    return table.upsert(Document(data, doc_id=id))

# 按键值插入或更新
def upsert_table_by_condition(table_name, data, key, value):
    table = db.table(table_name)
    return table.upsert(data, _[key] == value)

# 删除表格
def delete_table(table_name):
    return db.drop_table(table_name)

# 按ID删除
def remove_table(table_name, id):
    table = db.table(table_name)
    return table.remove(doc_ids=[id])

# 按键值删除
def remove_table_by_condition(table_name, key, value):
    table = db.table(table_name)
    return table.remove(_[key] == value)

# 按IDs批量删除
def remove_table_batch(table_name, ids):
    table = db.table(table_name)
    return table.remove(doc_ids=ids)

# table_name = "temp"


# 新增或更新操作
# upsert_table(table_name, {"user": "1xxx"}, 1)
# insert_table(table_name, {"user": "2yyy"})
# update_table_by_condition(table_name, {"user": "1zzz"}, 'user', '1xxx')
# insert_table_multiple(table_name, [{"user": "root"}, {"user": "admin"}])

# 查询操作
# print(get_table(table_name))
# print(get_table_last(table_name))
# print(get_table_by_condition(table_name, 'user', '2xxx')) 

# 删除操作(找不到ID会报错)
# remove_table(table_name, 4)
# remove_table_batch(table_name, [4,5])
# delete_table(table_name)

# 输出数据
# print(list_table(table_name))
