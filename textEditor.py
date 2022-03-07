def text_editor(operations:list) -> str:
    cursor_positon = 0
    edit = False
    highlignt_bool = False
    content = ""
    for operation in operations:
        if operations != "UNDO":
            opn = operation.split(" ")
            if opn[0] == "TYPE":
                previous_value = opn[1]
                content = content + opn[1]
                cursor_positon = len(content)+1
            elif opn[0] == "MOVE_CURSOR":
                cursor_positon = cursor_positon + opn[1]
            elif opn[0] == "SELECT":
                highlight = opn[1].split("")
                highlignt_bool = True
            elif opn[0] == "UNDO":
                if edit:
                    


                


   
    return content

inter = ["TYPE coding"]
text_editor(inter)