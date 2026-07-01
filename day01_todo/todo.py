todos = []
while True:
    print("-----Todo List-----")
    print("1.查看代辦事項")
    print("2.新增代辦事項")
    print("3.刪除代辦事項")
    print("4.離開")
#接收使用者輸入
    choice = input("請輸入:")

#新增功能
    if choice == "2":
        item = input("請輸入代辦事項:")
        todos.append(item)
        print("新增成功!")
    
#查看功能
    if choice == "1":
        if len(todos) == 0:
            print("目前無代辦項目")
        else:
            for i,item in enumerate(todos, start=1):
                print(f"{i}. {item}")
#刪除功能
    if choice == "3":
        index = input("請輸入刪除項目")
        if 1 <= len(todos)
            todos.pop(index)
        else
            print("輸入")
    if choice == "4":
        break
    else
        print("輸入錯誤")