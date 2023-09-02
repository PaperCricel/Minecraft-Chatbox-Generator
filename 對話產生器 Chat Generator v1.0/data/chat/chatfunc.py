import os
import shutil
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tkfd
import ctgnrt.complement as aw
import ctgnrt.main as main

# temp variable
Sign_Pos = "0 0 0"

# file place
here = __file__.replace("chatfunc.py", "").replace("\\", "/")
f    = f"{here}/ctgnrt/data.txt"

# window attributes
win = tk.Tk()
win.title("Minecraft 對話產生器 ;)  |  v1.0")
win.geometry("740x580+0+0")
win.resizable(False,False)
win.iconbitmap(f"{here}/ctgnrt/icon.ico")
win.columnconfigure((0,1),weight=1)

# insert files
def insert_file():
    global Fileplace,Sound,Ta,Space,SpaceLong,Pos,Text,IsDotSlow,OptionIsDotSlow2,IsShortSentenceRapid,OptionIsShortSentenceRapid2,OptionIsShortSentenceRapid3,GenerateSkip,OptionGenerateSkip2,Mode,VisiblePlayer,Serfix,Prefix,here,f,Billboard,Background,LineWidth,Alignment,SeeThrough,Scale1,Scale2,TextOpacity,GenerateSkip ,GenerateStart ,GenerateSetup ,GenerateEnd,GenerateClear ,GenerateTick, GenerateBackup, GenerateSpace
    GenerateSkip   = True
    GenerateStart  = True
    GenerateSetup  = True
    GenerateSpace  = True
    GenerateEnd    = True
    GenerateClear  = True
    GenerateTick   = True
    GenerateBackup = True
    with open(f,"r",encoding='utf-8') as f:
        temp = f.readlines()
        for i in range(len(temp)):
            temp[i] = temp[i].replace("\n","")
            #if i != 1 or i != 6:temp[i] = temp[i].replace(" ","")
        Fileplace                   = temp[0]
        Sound                       = temp[1]
        Ta                          = temp[2]
        Space                       = temp[3]
        SpaceLong                   = temp[4]
        Pos                         = temp[5]
        Prefix                      = temp[6]
        Text                        = temp[7]
        Serfix                      = temp[8]
        IsDotSlow                   = bool(temp[9].replace("False", ""))
        OptionIsDotSlow2            = temp[10]
        IsShortSentenceRapid        = bool(temp[11].replace("False", ""))
        OptionIsShortSentenceRapid2 = temp[12]
        OptionIsShortSentenceRapid3 = temp[13]
        GenerateSkip                = bool(temp[14].replace("False", ""))
        OptionGenerateSkip2         = temp[15]
        Mode                        = int(temp[16])
        VisiblePlayer               = temp[17]
        Billboard                   = int(temp[18])
        Alignment                   = int(temp[19])
        SeeThrough                  = bool(temp[20].replace("False", ""))
        Background                  = bool(temp[21].replace("False", ""))
        Scale1                      = float(temp[22] or 1)
        Scale2                      = float(temp[23] or 1)
        LineWidth                   = str(temp[24])
        TextOpacity                 = temp[25]
        f.close
insert_file()

# save data
def save_data():
    global enFilePlace,enSound,enTa,enSpace,enSpaceLong,enPos,enText,varIsDotSlow,enIsDotSlow,varIsShortSentenceRapid,enIsShortSentenceRapid1,enIsShortSentenceRapid2,varGenerateSkip,enGenerateSkip,enVisiblePlayer,enPrefix,enSerfix,enBillboard,varBackground,enLineWidth,enAlignment,varSeeThrough,enScale1,enScale2,ScTextOpacity
    with open(f"{here}/ctgnrt/data.txt","w+",encoding='utf-8') as f:
        f.write(str(enFilePlace.get()).replace("\n", "")+"\n")
        f.write(str(enSound.get()).replace("\n", "")+"\n")
        f.write(str(enTa.get()).replace("\n", "")+"\n")
        f.write(str(enSpace.get()).replace("\n", "")+"\n")
        f.write(str(enSpaceLong.get()).replace("\n", "")+"\n")
        f.write(str(enPos.get()).replace("\n", "")+"\n")
        f.write(str(enPrefix.get()).replace("\n", "")+"\n")
        f.write(str(enText.get("1.0","end-1c").split("\n"))+"\n")
        f.write(str(enSerfix.get()).replace("\n", "")+"\n")

        f.write(str(varIsDotSlow.get()).replace("\n", "")+"\n")
        f.write(str(enIsDotSlow.get()).replace("\n","")+"\n")

        f.write(str(varIsShortSentenceRapid.get()).replace("\n","")+"\n")
        f.write(str(enIsShortSentenceRapid1.get()).replace("\n","")+"\n")
        f.write(str(enIsShortSentenceRapid2.get()).replace("\n","")+"\n")
        
        f.write(str(varGenerateSkip.get()).replace("\n","")+"\n")
        f.write(str(enGenerateSkip.get()).replace("\n", "")+"\n")
        
        f.write(str(Mode).replace("\n", "")+"\n")
        f.write(str(enVisiblePlayer.get()).replace("\n", "")+"\n")
        
        f.write(str(aw.billboard_turn_int(enBillboard)).replace("\n", "")+"\n")
        f.write(str(aw.alignment_turn_int(enAlignment)).replace("\n", "")+"\n")
        f.write(str(varSeeThrough.get()).replace("\n", "")+"\n")
        f.write(str(varBackground.get()).replace("\n", "")+"\n")
        f.write(str(enScale1.get()).replace("\n", "")+"\n")
        f.write(str(enScale2.get()).replace("\n", "")+"\n")
        f.write(str(enLineWidth.get()).replace("\n", "")+"\n")
        f.write(str(ScTextOpacity.get()).replace("\n", "")+"\n")
        f.close
        temp_save = tk.Label(win, text="儲存成功!", fg="#19AF50")
        temp_save.grid(row=19,column=0,columnspan=2)
        win.after(3000, lambda: temp_save.grid_remove())

# insert inputs
def insert_en():
    enGenerateSkip.delete(0,tk.END)
    enGenerateSkip.insert(0,OptionGenerateSkip2)
    enIsShortSentenceRapid2.delete(0,tk.END)
    enIsShortSentenceRapid2.insert(0, OptionIsShortSentenceRapid3)
    enIsShortSentenceRapid1.delete(0,tk.END)
    enIsShortSentenceRapid1.insert(0, OptionIsShortSentenceRapid2)
    enIsDotSlow.delete(0,tk.END)
    enIsDotSlow.insert(0, OptionIsDotSlow2)
    enText.delete(1.0,tk.END)
    enText.insert(1.0, str(Text).replace("[\"", "").replace("\"]", "").replace("['", "").replace("']", "").replace("\n", "").replace("', '","\n"))
    enPrefix.delete(0,tk.END)
    enPrefix.insert(0, Prefix)
    enSerfix.delete(0,tk.END)
    enSerfix.insert(0, Serfix)
    enVisiblePlayer.delete(0,tk.END)
    enVisiblePlayer.insert(0, VisiblePlayer)
    enPos.delete(0,tk.END)
    enPos.insert(0, Pos)
    enSpaceLong.delete(0,tk.END)
    enSpaceLong.insert(0, SpaceLong)
    enSpace.delete(0,tk.END)
    enSpace.insert(0, Space)
    enTa.delete(0,tk.END)
    enTa.insert(0, Ta)
    enSound.delete(0,tk.END)
    enSound.insert(0, Sound)
    enFilePlace.delete(0,tk.END)
    enFilePlace.insert(0, Fileplace)
    enBillboard.delete(0,tk.END)
    enBillboard.current(Billboard)
    enLineWidth.delete(0,tk.END)
    enLineWidth.insert(0,LineWidth)
    enAlignment.delete(0,tk.END)
    enAlignment.current(Alignment)
    enScale1.delete(0,tk.END)
    enScale1.insert(0,Scale1)
    enScale2.delete(0,tk.END)
    enScale2.insert(0,Scale2)
    ScTextOpacity.set(TextOpacity)
    cbIsDotSlow.deselect()
    if IsDotSlow == True: cbIsDotSlow.select()
    cbIsShortSentenceRapid.deselect()
    if IsShortSentenceRapid == True: cbIsShortSentenceRapid.select()
    cbGenerateSkip.deselect()
    if GenerateSkip == True: cbGenerateSkip.select()
    cbBackground.deselect()
    if Background == True: cbBackground.select()
    cbSeeThrough.deselect()
    if SeeThrough == True: cbSeeThrough.select()

# import data
def import_data():
    global f
    f = tkfd.askopenfilename(initialdir=here+"/functions/",title='選擇backup檔案',filetypes=[("Text Files", ".txt")])
    insert_file()
    if Mode == 0:area()
    elif Mode == 1:text()
    else:marker()
    text_label = ['1.19.4前漂浮文字','1.19.4後漂浮文字','Actionbar文字']
    mode_temp.set(text_label[Mode])
    insert_en()

# generate
def generate_cmd():
    global Textnum, Texttrigger_num,Textcolor_sort,Textcolor_color,Mode, IsDotSlow, IsShortSentenceRapid, SpaceDot, DefShort, SpaceShort, SkipCoolDown,GenerateSkip ,GenerateStart ,GenerateSetup ,GenerateEnd,GenerateClear ,GenerateTick, GenerateBackup ,GenerateSpace
    # run file
    # ----- 基本設定 ----- # 

    FilePlace   = str(enFilePlace.get()).replace("\n", "").replace("\\","/")
    Sound       = str(enSound.get()).replace("\n","")
    Ta          = str(enTa.get()).replace("\n","")
    Space       = str(enSpace.get()).replace("\n","") or "2"
    SpaceLong   = str(enSpaceLong.get()).replace("\n","") or "20"
    Pos         = str(enPos.get()).replace("\n","") or "positioned ~ ~ ~"
    Text        = enText.get("1.0","end-1c").split("\n")
    Mode        = int(Mode)

    # ----- 選項 ----- #

    # ...是否要變速 
    if enIsDotSlow.get() != "":
        SpaceDot  = int(enIsDotSlow.get())
        IsDotSlow = varIsDotSlow.get()
    else:
        SpaceDot  = Space
        IsDowSlow = False

    # 太少字是否要快速帶過
    if enIsShortSentenceRapid1.get() != "" and enIsShortSentenceRapid2.get() != "":
        DefShort   = int(enIsShortSentenceRapid1.get() or -1)
        SpaceShort = int(enIsShortSentenceRapid2.get() or Space)
        IsShortSentenceRapid = varIsShortSentenceRapid.get()
    else: 
        DefShort             = -1
        SpaceShort           = Space
        IsShortSentenceRapid = False

    # 是否生成Skip檔案
    if enGenerateSkip.get() != "":
        SkipCoolDown   = int(enGenerateSkip.get())
        GenerateSkip   = varGenerateSkip.get()
    else: 
        SkipCoolDown = 0
        GenerateSkip = False

    # 使用actionbar而不是文字顯示
    VisiblePlayer  = str(enVisiblePlayer.get()).replace("\n","") or "@a"
    Prefix         = str(enPrefix.get().replace("\n","") or '')
    if Prefix != '': Prefix = Prefix+','
    Serfix         = str(enSerfix.get().replace("\n","") or '')
    if Serfix != '': Serfix = ','+Serfix

    # Text Display
    Billboard   = int(aw.billboard_turn_int(enBillboard)) or 0
    Alignment   = int(aw.alignment_turn_int(enAlignment)) or 0
    SeeThrough  = varSeeThrough.get()
    Background  = varBackground.get()
    Scale1      = float(enScale1.get() or 1.0)
    Scale2      = float(enScale2.get() or 1.0)
    LineWidth   = enLineWidth.get() or 200
    TextOpacity = str(ScTextOpacity.get() or 100)

    # ----- 初始化 ----- #
    import ctgnrt.error_file as er_file
    error = False

    # 目前檔案位置
    Current_file = here+"functions/"
    # 生成位產生的資料夾
    if FilePlace[-1] != "/": FilePlace = FilePlace+"/"
    dir_all = FilePlace.split("/")
    dir_this = ""
    for i in range(len(dir_all)-1):
        dir_this = dir_this+dir_all[i]+"/"
        try : 
            if not os.path.isdir(Current_file+dir_this):os.mkdir(Current_file+dir_this)
            if i == len(dir_all)-2:
                # 生成skip資料夾
                if GenerateSkip == True and not os.path.isdir(Current_file+dir_this+"skip/"):os.mkdir(Current_file+dir_this+"skip/")
                # 生成basic資料夾
                if not os.path.isdir(Current_file+dir_this+"basic/"):os.mkdir(Current_file+dir_this+"basic/")
        except: 
            error = er_file.error_7(win, FilePlace, lbFilePlace, enFilePlace, error)
        else:
            lbFilePlace.config(fg="#000000")
            enFilePlace.config(fg="#000000")
    
    File_start  = f'{Current_file+FilePlace}-start.mcfunction'
    File_end    = f'{Current_file+FilePlace}-end.mcfunction'
    File_setup  = f'{Current_file+FilePlace}basic/setup.mcfunction'
    File_space  = f'{Current_file+FilePlace}basic/space_loop.mcfunction'
    File_clear  = f'{Current_file+FilePlace}basic/clear.mcfunction'
    File_backup = f'{Current_file+FilePlace}backup.txt'
    File_Trans  = f'{Current_file+FilePlace}basic/transformation.mcfunction'
    
    File_skip   = f'{Current_file+FilePlace}-skip.mcfunction'
    File_skipl  = f'{Current_file+FilePlace}skip/loop.mcfunction'
    File_skips  = f'{Current_file+FilePlace}skip/store.mcfunction'
    
    File_tick   = f'{Current_file}space.mcfunction'
    
    Ta = 'ta'+str(Ta)
    Textlen = len(Text)
    Texts = []

    # ----- error detect ----- #

    # error options
    if error == False: error = er_file.error_1(win, File_tick, FilePlace, Ta, lbTa, lbTa1, enTa, lbFilePlace, enFilePlace, error)
    if error == False: error = er_file.error_2(win, FilePlace, lbFilePlace, enFilePlace, error)
    if error == False: error = er_file.error_3(win, Ta, lbTa, lbTa1, enTa, error)
    if error == False: error = er_file.error_4(win, Text, lbText, enText, error)
    if error == False: error = er_file.error_5(win, Prefix, lbPrefix, enPrefix, error)
    if error == False: error = er_file.error_6(win, Serfix, lbSerfix, enSerfix, error)
    
    if error == False: 
        # ----- Start ----- #
    
        if GenerateStart == True:
            main.start(File_start, File_Trans, Ta, Pos, FilePlace, Mode, Billboard, Alignment, SeeThrough, Background, Scale1, Scale2, LineWidth, TextOpacity)

        # ----- Setup ----- #

        if GenerateSetup == True:
            Events = main.setup(File_setup, Textlen, Text, Texts, FilePlace, Ta, Prefix, IsDotSlow, SpaceDot, Space, DefShort, IsShortSentenceRapid, SpaceShort, SpaceLong, GenerateSkip, Serfix)
        else: Events = []

        # ----- Space ----- #

        if GenerateSpace == True:
            main.space(FilePlace, File_space, Ta, GenerateSkip, Mode, VisiblePlayer, Sound, Events, i, Sign_Pos)

        # ----- End ----- #

        if GenerateEnd == True:
            main.end(File_end, Ta, FilePlace)

        # ----- Clear ----- #

        if GenerateClear == True:
            main.clear(File_clear, Ta)

        # ----- Skip ----- #

        if GenerateSkip == True:
            main.skip(File_skip, File_skipl, File_skips, Ta, SkipCoolDown, FilePlace)
        else:
            try:
                shutil.rmtree(Current_file+dir_this+"skip/")
                os.remove(File_skip) 
            except: pass

        # ----- Tick ----- #

        if GenerateTick == True:
            main.tick(File_tick,Ta,FilePlace)

        # ----- Save File ----- #

        save_data()

        # ----- Back up ----- #

        if GenerateBackup == True:
            shutil.copy(f"{here}/ctgnrt/data.txt",File_backup)

        print("[Success] 生成成功")
        temp_success = tk.Label(win, text="生成成功!", fg="#19AF50")
        temp_success.grid(row=19,column=0,columnspan=2)
        win.after(3000, lambda: temp_success.grid_remove())
    GenerateStart  = True
    GenerateSetup  = True
    GenerateSpace  = True
    GenerateEnd    = True
    GenerateClear  = True
    GenerateTick   = True
    GenerateBackup = True

# ----- Settings ----- #

ttk.Separator(win, orient=tk.HORIZONTAL).grid(row=1,column=0,columnspan=2, sticky="new",pady=10)

# Basic Options
BasicOptions = ttk.Frame(win)
ttk.Separator(BasicOptions,orient=tk.VERTICAL).grid(row=0,column=1,rowspan=100, sticky="nsw",padx=20)
lbFilePlace     = tk.Label(BasicOptions,text= '檔案位置',font=('Microsoft JhengHei',12))
lbSound         = tk.Label(BasicOptions,text= '音效'    ,font=('Microsoft JhengHei',12))
lbTa            = tk.Label(BasicOptions,text= 'Tag'     ,font=('Microsoft JhengHei',12))
lbSpace         = tk.Label(BasicOptions,text= '短空格'  ,font=('Microsoft JhengHei',12)).grid(row=3,column=0,pady=3)
lbSpaceLong     = tk.Label(BasicOptions,text= '長空格'  ,font=('Microsoft JhengHei',12)).grid(row=4,column=0,pady=3)
lbPos           = tk.Label(BasicOptions,text= '位置'    ,font=('Microsoft JhengHei',12))
lbVisiblePlayer = tk.Label(BasicOptions,text= '顯示玩家',font=('Microsoft JhengHei',12))
lbPrefix        = tk.Label(BasicOptions,text= '前綴'    ,font=('Microsoft JhengHei',12))
lbText          = tk.Label(BasicOptions,text= '文字'    ,font=('Microsoft JhengHei',12))
lbSerfix        = tk.Label(BasicOptions,text= '後綴'    ,font=('Microsoft JhengHei',12))
lbFilePlace     .grid(row=0,column=0,pady=3)
lbSound         .grid(row=1,column=0,pady=3)
lbTa            .grid(row=2,column=0,pady=3)
lbPrefix        .grid(row=7,column=0,pady=3)
lbText          .grid(row=8,column=0,pady=3)
lbSerfix        .grid(row=9,column=0,pady=3)

enFilePlace     = tk.Entry(BasicOptions,font=('Microsoft JhengHei',12),width=30)
enSound         = tk.Entry(BasicOptions,font=('Microsoft JhengHei',12),width=30)
FmTa            = tk.Frame(BasicOptions)
lbTa1           = tk.Label(FmTa,text='ta ',font=('Microsoft JhengHei',12))
enTa            = tk.Entry(FmTa,font=('Microsoft JhengHei',12),width=8)
lbTa1           .grid(row=0,column=0,sticky="w")
enTa            .grid(row=0,column=1,sticky="w")
FmTa            .grid(row=2,column=2,sticky="w")

enSpace         = tk.Entry(BasicOptions,font=('Microsoft JhengHei',12),width=11)
enSpaceLong     = tk.Entry(BasicOptions,font=('Microsoft JhengHei',12),width=11)
enFilePlace     .grid(row=0,column=2,sticky="w")
enSound         .grid(row=1,column=2,sticky="w")
enSpace         .grid(row=3,column=2,sticky="w")
enSpaceLong     .grid(row=4,column=2,sticky="w")

FmPos           = tk.Frame(BasicOptions)
lbPos1          = tk.Label(FmPos,text= 'execute '                 ,font=('Microsoft JhengHei',12))
enPos           = tk.Entry(FmPos                                  ,font=('Microsoft JhengHei',12),width=20)
lbPos2          = tk.Label(FmPos,text= ' run summon chat box here',font=('Microsoft JhengHei',12))
lbPos1          .grid(row=0,column=0,sticky="w")
enPos           .grid(row=0,column=1,sticky="w")
lbPos2          .grid(row=0,column=2,sticky="w")
FmPos.grid(row=5,column=2,sticky="w")

enVisiblePlayer = tk.Entry(BasicOptions,font=('Microsoft JhengHei',12),width=20) #.grid(row=6,column=2,sticky="w")
enPrefix        = tk.Entry(BasicOptions,font=('Microsoft JhengHei',12),width=64)
enText          = tk.Text(BasicOptions,font=('Microsoft JhengHei',15),width=48,height=5)
enSerfix        = tk.Entry(BasicOptions,font=('Microsoft JhengHei',12),width=64)
enPrefix        .grid(row=7,column=2,sticky="w")
enText          .grid(row=8,column=2,sticky="w")
enSerfix        .grid(row=9,column=2,sticky="w")
BasicOptions.grid(row=2,column=0,rowspan=14,columnspan=1000,sticky="ew")

# More Options
MoreOptions = ttk.Frame(win)
MoreOptions.columnconfigure((0,1),weight=1)

FmIsDotSlow = tk.Frame(MoreOptions,bd=1,relief="solid")
tk.Label(FmIsDotSlow,text="每個...會變成",font=('Microsoft JhengHei',12)).grid(row=1,column=0)
varIsDotSlow = tk.BooleanVar()
cbIsDotSlow = tk.Checkbutton(FmIsDotSlow,text="...需不需要變速",variable=varIsDotSlow,font=('Microsoft JhengHei',12))
cbIsDotSlow.grid(row=0,column=0,sticky="w",columnspan=1000)
if IsDotSlow == True: cbIsDotSlow.select()
enIsDotSlow = tk.Entry(FmIsDotSlow,width=2,font=('Microsoft JhengHei',12))
enIsDotSlow .grid(row=1,column=1)
tk.Label(FmIsDotSlow,text=" ticks 間隔",font=('Microsoft JhengHei',12)).grid(row=1,column=2)
FmIsDotSlow.grid(row=0,column=0,sticky="w",padx=10,pady=5)

FmIsShortSentenceRapid = tk.Frame(MoreOptions,bd=1,relief="solid")
tk.Label(FmIsShortSentenceRapid,text="句子只有",font=('Microsoft JhengHei',12)).grid(row=1,column=0)
enIsShortSentenceRapid1 = tk.Entry(FmIsShortSentenceRapid,width=2,font=('Microsoft JhengHei',12))
enIsShortSentenceRapid1 .grid(row=1,column=1)
tk.Label(FmIsShortSentenceRapid,text="個字的時候，會變成",font=('Microsoft JhengHei',12)).grid(row=1,column=2)
enIsShortSentenceRapid2 = tk.Entry(FmIsShortSentenceRapid,width=2,font=('Microsoft JhengHei',12))
enIsShortSentenceRapid2 .grid(row=1,column=3)
tk.Label(FmIsShortSentenceRapid,text="ticks 間隔",font=('Microsoft JhengHei',12)).grid(row=1,column=4)
varIsShortSentenceRapid = tk.BooleanVar()
cbIsShortSentenceRapid = tk.Checkbutton(FmIsShortSentenceRapid,text="太少字是否要加速",variable=varIsShortSentenceRapid,font=('Microsoft JhengHei',12))
cbIsShortSentenceRapid.grid(row=0,column=0,sticky="w",columnspan=1000)
if IsShortSentenceRapid == True: cbIsShortSentenceRapid.select()
FmIsShortSentenceRapid.grid(row=1,column=0,sticky="w",padx=10,pady=5)

FmGenerateSkip = tk.Frame(MoreOptions,bd=1,relief="solid")
tk.Label(FmGenerateSkip,text="每個句子被跳過之前，會有",font=('Microsoft JhengHei',12))
enGenerateSkip = tk.Entry(FmGenerateSkip,width=2,font=('Microsoft JhengHei',12))
enGenerateSkip .grid(row=1,column=0)
tk.Label(FmGenerateSkip,text="ticks 的冷卻時間",font=('Microsoft JhengHei',12)).grid(row=1,column=2)
varGenerateSkip = tk.BooleanVar()
cbGenerateSkip = tk.Checkbutton(FmGenerateSkip,text="是否要生成Skip文件",variable=varGenerateSkip,font=('Microsoft JhengHei',12))
cbGenerateSkip.grid(row=0,column=0,sticky="w",columnspan=1000)
if GenerateSkip == True: cbGenerateSkip.select()
FmGenerateSkip.grid(row=2,column=0,sticky="w",padx=10,pady=5)

# Text Display
FmTextDisplay = tk.Frame(MoreOptions, bd=1, relief="solid")
ttk.Separator(FmTextDisplay,orient=tk.VERTICAL).grid(row=0,column=1,rowspan=100, sticky="nsw",padx=20)
tk.Label(FmTextDisplay,text="顯示形式"  ,font=('Microsoft JhengHei',12)).grid(row=0,column=0,pady=3)
tk.Label(FmTextDisplay,text="文字靠邊"  ,font=('Microsoft JhengHei',12)).grid(row=1,column=0,pady=3)
tk.Label(FmTextDisplay,text="文字大小"  ,font=('Microsoft JhengHei',12)).grid(row=4,column=0,pady=3)
tk.Label(FmTextDisplay,text="最長句子"  ,font=('Microsoft JhengHei',12)).grid(row=5,column=0,pady=3)
tk.Label(FmTextDisplay,text="文字透明度",font=('Microsoft JhengHei',12)).grid(row=6,column=0,pady=3)

bb = tk.StringVar()
rbb = ["center(預設)","fixed","horizontal"]
enBillboard = ttk.Combobox(FmTextDisplay,values=rbb, textvariable=bb, state='readonly',width=15,font=('Microsoft JhengHei',10))
enBillboard .grid(row=0,column=2)

ag = tk.StringVar()
rag = ["center(預設)","left","right"]
enAlignment = ttk.Combobox(FmTextDisplay,values=rag, textvariable=ag, state='readonly',width=15,font=('Microsoft JhengHei',10))
enAlignment .grid(row=1,column=2)

varBackground = tk.BooleanVar()
cbBackground = tk.Checkbutton(FmTextDisplay,text="是否有背景框",variable=varBackground,font=('Microsoft JhengHei',12))
cbBackground.grid(row=2,column=2,sticky="w")
if Background == True: cbBackground.select()

varSeeThrough = tk.BooleanVar()
cbSeeThrough = tk.Checkbutton(FmTextDisplay,text="文字顯示穿透過方塊",variable=varSeeThrough,font=('Microsoft JhengHei',12))
cbSeeThrough.grid(row=3,column=2,sticky="w")
if SeeThrough == True: cbSeeThrough.select()

FmScale = tk.Frame(FmTextDisplay)
enScale1 = tk.Entry(FmScale,width=5,font=('Microsoft JhengHei',12))
enScale1 .grid(row=0,column=0,sticky="w")
tk.Label(FmScale,text="寬 ✖ ",font=('Microsoft JhengHei',12)).grid(row=0,column=1,sticky="w")
enScale2 = tk.Entry(FmScale,width=5,font=('Microsoft JhengHei',12))
enScale2 .grid(row=0,column=2,sticky="w")
tk.Label(FmScale,text="高",font=('Microsoft JhengHei',12)).grid(row=0,column=3,sticky="w")
FmScale.grid(row=4,column=2,sticky="w")

FmLineWidth = tk.Frame(FmTextDisplay)
tk.Label(FmLineWidth,text="到",font=('Microsoft JhengHei',12)).grid(row=0,column=0,sticky="w")
enLineWidth = tk.Entry(FmLineWidth,width=3,font=('Microsoft JhengHei',12))
enLineWidth .grid(row=0,column=1,sticky="w")
tk.Label(FmLineWidth,text="個字元的時候換行",font=('Microsoft JhengHei',12)).grid(row=0,column=2,sticky="w")
FmLineWidth.grid(row=5,column=2,sticky="w")

varTextOpacity = tk.IntVar()
ScTextOpacity = tk.Scale(FmTextDisplay,from_=0,to=100,orient="horizontal")
ScTextOpacity.set(100)
ScTextOpacity.grid(row=6,column=2,sticky="we")

FmTextDisplay.grid(row=0,column=1,rowspan=3)
#MoreOptions.grid(row=2,column=0,columnspan=1000,sticky="ew")

ttk.Separator(MoreOptions, orient=tk.HORIZONTAL).grid(row=4,column=0,columnspan=1000,sticky="new",pady=20)

FmGenerateActive = tk.Frame(MoreOptions)
def generate_cmd_quick(i):
    global GenerateStart ,GenerateSetup ,GenerateSpace ,GenerateEnd,GenerateClear ,GenerateTick,GenerateBackup
    if i != 0 :GenerateStart  = False
    if i != 1 :GenerateEnd    = False
    if i != 2 :GenerateSetup  = False
    if i != 3 :GenerateTick   = False
    if i != 4 :GenerateSpace  = False
    if i != 5 :GenerateBackup = False
    GenerateClear  = False
    generate_cmd()
tk.Label(FmGenerateActive,text="快速微調生成\n(建議搞懂後再使用.w.)",font=('Microsoft JhengHei',12)).grid(row=0,column=0,columnspan=1000,sticky="new",pady=(0,10))
Generates = ["Start","End","Setup","Tick","Space","Backup"]
for i in range(len(Generates)):
    btGenerateQuick = tk.Button(FmGenerateActive,text=f"生成{Generates[i]}" ,command=lambda m=i: generate_cmd_quick(m),font=('Microsoft JhengHei',10),relief="solid")
    btGenerateQuick.grid(row=1,column=i,sticky="w",padx=10)
FmGenerateActive.grid(row=5,column=0,columnspan=6)

# ----- End ----- #
ttk.Separator(win, orient=tk.HORIZONTAL).grid(row=17,column=0,columnspan=2, sticky="new",pady=20)
def PageBasicOptions():
    BasicOptions.grid(row=2,column=0,rowspan=14,columnspan=1000,sticky="ew")
    MoreOptions.grid_remove()

def PageMoreOptions():
    BasicOptions.grid_remove()
    MoreOptions.grid(row=2,column=0,columnspan=1000,sticky="ew")

BtBasicOption = tk.Button(win,text="基礎設定",command=PageBasicOptions, font=('Microsoft JhengHei',12)).grid(row=0,column=0,sticky="we")
BtMoreOption  = tk.Button(win,text="更多設定",command=PageMoreOptions, font=('Microsoft JhengHei',12)).grid(row=0,column=1,sticky="ew")

create = tk.Button(win, text="產生對話",command=generate_cmd,font=('Microsoft JhengHei',12),activeforeground="#F9CC4F")
create.grid(row=18,column=0,columnspan=2)

# ----- Menu ----- #
top_menu = tk.Menu(win)
# file
file_menu = aw.File(top_menu, '檔案', ['導入Backup檔案','儲存Backup檔案'],[import_data,save_data])

# mode
def area():
    global Mode, temp
    Mode = 0
    lbPos.grid(row=5,column=0,pady=3)
    lbPos1.grid(row=5,column=2,pady=3)
    enPos.grid(row=5,column=3,pady=3)
    lbPos2.grid(row=5,column=4,pady=3)
    
    FmTextDisplay.grid_remove()
    lbVisiblePlayer.grid_remove()
    enVisiblePlayer.grid_remove()
def text():
    global Mode, temp
    Mode = 1
    lbPos.grid(row=5,column=0,pady=3)
    lbPos1.grid(row=5,column=2,pady=3)
    enPos.grid(row=5,column=3,pady=3)
    lbPos2.grid(row=5,column=4,pady=3)
    
    FmTextDisplay.grid(row=0,column=1,rowspan=3)
    lbVisiblePlayer.grid_remove()
    enVisiblePlayer.grid_remove()
def marker():
    global Mode, temp
    Mode = 2
    lbPos.grid_remove()
    lbPos1.grid_remove()
    enPos.grid_remove()
    lbPos2.grid_remove()
    
    FmTextDisplay.grid_remove()
    lbVisiblePlayer.grid(row=5,column=0,pady=3)
    enVisiblePlayer.grid(row=5,column=2,pady=3,sticky="w")

mode_temp = tk.StringVar()
Mode_menu = aw.Mode(top_menu, '模式', ['1.19.4前漂浮文字','1.19.4後漂浮文字','Actionbar文字'],[area,text,marker],Mode,mode_temp)

if Mode == 0:area()
elif Mode == 1:text()
else:marker()

insert_en()
win.configure(menu=top_menu)
win.mainloop()