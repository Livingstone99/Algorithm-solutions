"""A text editor is a type of computer program that edits plain text. 
It consists of a string with a cursor. In the initial state, the string
 is empty with the cursor at the beginning of the string. Some modern 
 text editors have a clipboard manager - they save a history of copied text.

Your task is to simulate the working process of a text editor with a simple
 clipboard manager which can handle six types of operations:

TYPE <text> - insert <text> after the current position of the cursor, where
 <text> consists of at most 50 characters including English letters, digits,
  whitespaces, and symbols .,?!-. The cursor moves to the end of the inserted text.
SELECT <start_index> <end_index> - select the substring of the current text
 [text[start_index] ... text[end_index]] (inclusive indices, 0-based) of 
 length end_index - start_index + 1. It is guaranteed that the indices are 
 valid. The cursor changes its position to the end of the selected area.
MOVE_CURSOR <offset> - change the cursor's current position. The <offset> 
specifies the direction and the value change - if it is negative the cursor
 moves to the left, and if it's positive the cursor moves to the right. At 
 all times, the cursor is either located at the beginning of the string 
 (before the first character), between two characters, or at the end of the 
 string (after the last character) - the cursor should always be within the 
 text bounds. If the <offset> is larger than the cursor can move, the cursor 
 will move in that direction as much as it can. If there is a selected area,
  it should be cleared after this operation.
COPY - add the text from the selected area to the clipboard. If there is no 
selected area then do nothing.
PASTE <steps_back> - insert the copied text from the clipboard manager. 
The number <steps_back> specifies which of the stored copied texts to insert. 
If <steps_back> is 1 then insert the last copied text, if it is 2 then insert 
the text copied before the last, and so on. It <steps_back> is greater than the
 clipboard history size then ignore this operation. The cursor moves to the
  end of the inserted text.
PASTE - do the same as if the operation is PASTE 1.
Note: If a selected area is not empty and the next operaion is 
either TYPE or PASTE then the following updating process is expected 
during the TYPE or PASTE operation:

Delete the selected text.
Insert the new text in the place of the deleted text.
The cursor position should move to the end of the new text.
You are given operations, an array of strings where each is an 
operation of one of the six types above. Your task is to find the 
resulting text after performing the given operations.
"""

def textEditor(operations):
    cursor_position = 0
    edit = False
    highlight_bool = False
    content = ""
    for operation in operations:
        if operation != "UNDO":
            opn = operation.split(" ")
            if opn[0] == "TYPE":
                previous_value = opn[1]
                content = content + opn[1]
                cursor_position = len(content)+1
            elif opn[0] == "MOVE_CURSOR":
                cursor_position = cursor_position + opn[1]
            elif opn[0] == "SELECT":
                highlight = opn[1].split("")
                highlight_bool = True
            elif opn[0] == "UNDO":
                if edit:
                    return content
textEditor(["TYPE hello", "MOVE_CURSOR 2", "SELECT 0 5", "UNDO", "TYPE world", "PASTE 1", "PASTE"])


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