todos = []

def show_menu():
    print("-----Todo List-----")
    print("1.查看代辦事項")
    print("2.新增代辦事項")
    print("3.刪除代辦事項")
    print("4.修改代辦事項")
    print("5.離開")
    
#新增功能
def add_todo():
    item = input("請輸入代辦事項:")
    todos.append(item)
    print(f"已新增：{item}")
    
#查看功能
def view_todos():
    if not todos:
        print("目前無代辦項目")
    else:
        for i,item in enumerate(todos, start=1):
            print(f"{i}. {item}")
#刪除功能
def delete_todo():
    index = int(input("請輸入刪除項目:"))
    if 1 <= index <= len(todos):
        deleted = todos.pop(index-1)
        print(f"已刪除:{deleted}")            
    else:
        print("無該代辦選項")
#修改功能
def edit_todo():
    view_todos()
    if not todos:
        print("目前無代辦項目")
        return
    index = int(input("請輸入要修改的項目:"))
    if 1 <= index <= len(todos):
        new_item = input("請輸入新的代辦事項:")
        todos[index-1] = new_item
        print(f"已修改成：{new_item}")
    else:
        print("無該代辦選項")
def load_todos():
    with open("todo.txt", "r", encoding="utf-8") as file:  
        lines = file.readlines()
        for line in lines:
            todos.append(line.strip())
def save_todos():
    with open("todo.txt", "w", encoding="utf-8") as file:
        for item in todos:
            file.write(item + "\n")
        

load_todos()    

while True:
    show_menu()
    choice = input("請輸入:")
    if choice == "1":
        view_todos()
    elif choice == "2":
        add_todo()
        save_todos()
    elif choice == "3":
        delete_todo()
        save_todos()
    elif choice == "4":
        edit_todo()
        save_todos()    
    elif choice == "5":
        break
    else:
        print("輸入錯誤")