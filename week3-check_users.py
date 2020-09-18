def check_users(current_users, new_users):
    pass
    current_users = ('adam', 'steve', 'bob', 'billy', 'joe')
    new_users = ('redman', 'adam', 'buckaroe', 'janet', 'griffin')
    for new_user in new_users:
        if new_us.lower() in current_users:
            print ("That name has been taken")
        else:
            print ("That name is available")
if __name__ == "__main__":
    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)