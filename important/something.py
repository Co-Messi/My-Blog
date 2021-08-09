class HandleChildrenData():
    def __init__(self, data):
        self.data = data
    
    # 获取第一层级所有数据
    def get_root_nodes(self): 
        pass
        print(self)
    # 最子层级的所有数据
    def get_child_nodes(self):
        pass
        data()
        print(data)
if __name__ == "__main__":
    data = [
        {"id": 1, "name":"node_1", "parent": None}, 
        {"id": 2, "name":"node_2", "parent": None},
        {"id": 3, "name":"node_1_1", "parent": 1},
        {"id": 4, "name":"node_1_2", "parent": 1},
        {"id": 5, "name":"node_2_1", "parent": 2},
        {"id": 6, "name":"node_2_2", "parent": 2},
        {"id": 8, "name":"node_1_2_1", "parent": 4},
        {"id": 9, "name":"node_2_2_2", "parent": 6},
    ]