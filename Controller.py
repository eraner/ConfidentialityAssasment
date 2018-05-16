import Utils.Database.DBHelper as DBHandler
import Utils.NVD.NVD_Handler as NVD_Handler
import AuthorizationSystem.AuthCheck as AuthCheck


def add_user(username, role, main_window):
    #print "Please insert the required data: \n"
    #username = raw_input("Username: ")
    #role = raw_input("Role: ")

    if DBHandler.add_user(username, role, main_window):
        main_window.print_to_log("Controller", "Added " + username + " successfully!")
    else:
        main_window.print_to_log("Controller", "Something went wrong!")


def delete_user(username, main_window):
    #username = raw_input("Please insert User to delete: ")
    if DBHandler.delete_user(username, main_window):
        main_window.print_to_log("Controller", username + " was removed")


def add_role(role_name, rank, main_window):
   # print "Please insert the required data: \n"
   # role_name = raw_input("Role name: ")
   # rank = raw_input("Rank (1-5): ")
    if DBHandler.add_role(role_name, rank, main_window):
        main_window.print_to_log("Controller", role_name + " was added")


def delete_role(role_name, main_window):
    #role_name = raw_input("Role name: ")
    DBHandler.delete_role(role_name, main_window)


def add_resource(resource_name, resource_type, main_window):
  #  print "Please insert the required data: \n"
  #  resource_name = raw_input("Resource name: ")
  #  resource_type = raw_input("Resource type: ")
    if DBHandler.add_resource(resource_name, resource_type, main_window):
        main_window.print_to_log("Controller", "Resource: " + resource_name + " was added")


def delete_resource(resource_id, main_window):
 #   resource_id = raw_input("Please insert resource ID to remove: ")
    if DBHandler.delete_resource_by_id(resource_id, main_window):
        main_window.print_to_log("Controller", "Resource id: " + resource_id + " was removed")


def add_rule(role, resource_id, permission, main_window):
#    print "Please insert the required data: \n"
#    permissions = ["rw", "r", "x", "rwx"]
#    role = raw_input("Role name: ")
#    resource_id = raw_input("Resource id: ")
#    for i in range(len(permissions)):
#        print str(i) + ". " + permissions[i]
#    perm_index = raw_input("Please choose the permission index: ")
#    if int(perm_index) not in range(len(permissions)):
#        print "Invalid permission index!"
#        return
    print permission
    if DBHandler.add_rule(role, resource_id, permission, main_window):
        main_window.print_to_log("Controller", "Rule was added")


def delete_rule(role, resource_id, main_window):
   # print "Please insert the required data: \n"
   # role = raw_input("Role: ")
   # resource_id = raw_input("Resource ID: ")
    if DBHandler.delete_rule(role, resource_id, main_window):
        main_window.print_to_log("Controller", "Rule was removed!")


def edit_auth_menu():
    while True:
        edit_choice = input("\nEdit Auth Menu: "
                            "\n1. Add user."
                           "\n2. Delete user."
                           "\n3. Add role."
                           "\n4. Delete role."
                           "\n5. Add Resource."
                           "\n6. Delete Resource."
                           "\n7. Add Rule."
                           "\n8. Delete Rule."
                           "\n9. Return to main menu."
                           "\nYour choice: ")
        if edit_choice == 1:
            add_user()
        elif edit_choice == 2:
            delete_user()
        elif edit_choice == 3:
            add_role()
        elif edit_choice == 4:
            delete_role()
        elif edit_choice == 5:
            add_resource()
        elif edit_choice == 6:
            delete_resource()
        elif edit_choice == 7:
            add_rule()
        elif edit_choice == 8:
            delete_rule()
        elif edit_choice == 9:
            return


def check_auth_system(main_window):

    curr_users = {"Eran Laudin": "Cleaner",
                  "Ohad Cohen": "Cleaner",
                  "Yael Gershenshtein": "Guard",
                  "Avi": "Guard",
                  "Keren": "Guard",
                  "Or": "Guard",
                  "Dvir": "Guard",
                  "Amir": "Guard",
                  "Yosi": "Guard",
                  "Nir Levi": "Developer",
                  "Omri Koresh": "QA"}

    curr_roles = {"Manager": 1,
                  "Cleaner": 5,
                  "Developer": 4,
                  "Team Leader": 4,
                  "Validation": 4,
                  "Architecture": 4,
                  "FW Developer": 4,
                  "Guard": 2,
                  "QA": 3}
    result = ""

    main_window.print_to_log("Controller", "#"*15 + "Users" + "#"*15)
    main_window.print_to_log("Controller", "Comparing current Users with optimal Users..")
    results = AuthCheck.check_users_roles_optimal_current(curr_users, curr_roles, main_window)
    main_window.print_to_log("Controller", "Results: Damage assessment to Users' table: " + str(results))

    # result += "\n" + "#"*15 + "Roles" + "#"*15 + "\n\n"
    # result += "Comparing current Roles with optimal Roles..\n"
    # results = AuthCheck.check_roles_optimal_current(curr_roles)
    # result += "Results: Damage assessment to roles' table: " + str(results[1])
    return results


def print_auth_system(main_window):
    main_window.print_to_log("Controller", "Printing Auth System")
    DBHandler.print_authorization_system(main_window)

if __name__ == "__main__":
    while True:
        choice = input("\nMenu: \n1. Print Authorization Details."
                       "        \n2. Print NVD."
                       "        \n3. Check Authorization system."
                       "        \n4. Edit Authorization system."        
                       "        \n9. Exit"
                       "        \nYour choice: ")
        if choice == 1:
            DBHandler.print_authorization_system()
        elif choice == 2:
            NVD_Handler.get_vulnerability_db()
        elif choice == 3:
            check_auth_system()
        elif choice == 4:
            edit_auth_menu()
        elif choice == 9:
            print "Goodbye"
            break
        else:
            print "Wrong Input!"



