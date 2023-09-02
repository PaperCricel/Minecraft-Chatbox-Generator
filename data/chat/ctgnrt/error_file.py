import tkinter as tk
class Error_display():
    def __init__(self, master, text):
        print(f"[Error] {text}")
        temp_error = tk.Label(master=master, text=text, fg="#FF0000")
        temp_error.grid(row=19,column=0,columnspan=2)
        master.after(3000, lambda: temp_error.grid_remove())


# Tag、檔案重複錯誤
def error_1(win, File_tick, FilePlace, Ta, lbTa, lbTa1, enTa, lbFilePlace, enFilePlace, error):
    with open(File_tick,'r',encoding='utf-8') as f:
        temp = f.readlines()
        for i in temp:
            if (i.find(FilePlace) >= 0 and i.find(Ta) == -1) or (i.find(Ta) >= 0 and i.find(FilePlace) == -1):
                error = True
                Error_display(win, "Tag、檔案重複錯誤")
    return error

# 未找到檔案位置
def error_2(win, FilePlace, lbFilePlace, enFilePlace, error):
    if FilePlace == "":
        error = True
        Error_display(win, "未找到檔案位置")
    return error

# 未找到Tag
def error_3(win, Ta, lbTa, lbTa1, enTa, error):
    if Ta == "ta":
        error = True
        Error_display(win, "未找到Tag")
    return error

# 對話中有空白錯誤
def error_4(win, Text, lbText, enText, error):
    for i in range(len(Text)):
        if Text[i] == "":
            error = True
            Error_display(win, "對話中有空白錯誤")
            break
        elif i == len(Text)-1:
            pass
    return error

# 前綴沒有被大括弧包起
def error_5(win, Prefix, lbPrefix, enPrefix, error):
    if Prefix != '' and (Prefix[:1] != "{" or Prefix[-2:] != "},"):
        error = True
        Error_display(win, "前綴沒有被大括弧包起")
    return error

# 後綴沒有被大括弧包起
def error_6(win, Serfix, lbSerfix, enSerfix, error):
    if Serfix != '' and (Serfix[:2] != ",{" or Serfix[-1:] != "}"):
        error = True
        Error_display(win, "後綴沒有被大括弧包起")
    return error

# 檔案路徑格式錯誤
def error_7(win, FilePlace, lbFilePlace, enFilePlace, error):
    error = True
    Error_display(win, "檔案路徑格式錯誤")
    return error