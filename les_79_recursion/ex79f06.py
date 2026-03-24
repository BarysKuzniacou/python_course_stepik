def sum_tree(node):
    if node is None:
        return 0

    return node['data'] + sum_tree(node['left']) + sum_tree(node['right'])


tree_root = {'data': 1,
             'left': {'data': 2,
                      'left': {'data': 7, 'left': None, 'right': None},
                      'right': {'data': 3, 'left': None, 'right': None}
                      },
             'right': {'data': 5,
                       'left': {'data': -4, 'left': None, 'right': None},
                       'right': {'data': 8, 'left': None, 'right': None}
                       }
             }

res = sum_tree(tree_root)
print(res)