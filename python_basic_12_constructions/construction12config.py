class User:
    def __init__(self, group: str):
        self.group = group

user = User(group = 'admin')

# if user.group == 'admin':
#     prcess_admin_request(user, request)
# elif user.group == 'manager':
#     prcess_manager_request(user, request)
# elif user.group == 'client':
#     prcess_client_request(user, request)

group_to_process_method = {
    'admin': prcess_admin_request,
    'manager': prcess_manager_request,
    'client': prcess_client_request
}

group_to_process_method[user.group](user, request)