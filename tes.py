# class HandleChildrenData():
#     def __init__(self, data):
#         self.data = data
    
#     # 获取第一层级所有数据
#         def get_root_nodes(current_data):
#             pass
#             result = []
#             for item in data:
#                 if item["parent"] != current_data["id"]:
#                     continue
#                 children_node_list = get_root_nodes(item)
#                 item["children"] = children_node_list
#                 result.append(item) 
#             return result
            
#         root_node = []
#         for item in data:
#             if item["parent"]:  
#                 continue
#             root_node.append(item)
#         for root_item in root_node:
#             root_item["children"] = get_root_nodes(root_item)
#         return root_node
#     # 最子层级的所有数据
#     def get_child_nodes(self):
#         pass
#         # root_node = []
#         # for item in data:
#         #     if item["parent"]:
#         #         continue
#         #     root_node.append(item)
                
#         # for root_item in root_node:
#         #     root_item["children"] = get_children_data(root_item)
#         # return root_node(item)
# 获取第一层级所有数据
def init_data():
    def get_root_nodes(current_data):
        pass
        result = []
        for item in data:
            if item["parent"] != current_data["id"]:
                continue
            children_node_list = get_root_nodes(item)
            item["children"] = children_node_list
            result.append(item) 
        return result
            
    root_node = []
    for item in data:
        if item["parent"]:  
            continue
        root_node.append(item)
        
    for root_item in root_node:
        root_item["children"] = get_root_nodes(root_item)
    return root_node


# # 最子层级的所有数据
# def get_child_nodes(data):
#     pass
#     # root_node = []
#     # for item in data:
#     #     if item["parent"]:
#     #         continue
#     #     root_node.append(item)
            
#     # for root_item in root_node:
#     #     root_item["children"] = get_children_data(root_item)
#     # return root_node(item)
            
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
    res = init_data(data)
    print(res)