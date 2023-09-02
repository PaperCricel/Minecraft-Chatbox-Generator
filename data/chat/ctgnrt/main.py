import os
def start(File_start,File_Trans,Ta,Pos,FilePlace,Mode,Billboard,Alignment,SeeThrough,Background,Scale1,Scale2,LineWidth,TextOpacity):
    with open(File_start,'w+',encoding='utf-8') as f:
        f.write(f"# ----- {Ta} ----- #\n")
        f.write(f"# 位置\n")
        f.write(f"kill @e[type=#minecraft:text,tag={Ta}]\n")
        if Mode == 0: f.write(f"execute {Pos} run summon area_effect_cloud ~ ~ ~ {{Tags:[chat,master,{Ta}],CustomNameVisible:1b,CustomName:'{{\"text\":\"\"}}',Duration:1000000000}}\n")
        elif Mode == 1: 
            f.write(f"execute {Pos} run summon text_display ~ ~ ~ {{Tags:[chat,master,{Ta}],CustomNameVisible:0b,text:'{{\"text\":\"\"}}'")
            if   Billboard == 0: f.write(f",billboard:\"center\"")
            elif Billboard == 1: f.write(f",billboard:\"fixed\"")
            elif Billboard == 2: f.write(f",billboard:\"horizontal\"")

            if   Alignment == 0: f.write(f",alignment:\"center\"")
            elif Alignment == 1: f.write(f",alignment:\"left\"")
            elif Alignment == 2: f.write(f",alignment:\"right\"")

            if SeeThrough == True: f.write(f",see_through:1b")

            if Background == False: f.write(f",background:0")
            if LineWidth  != 200  : f.write(f",line_width:{LineWidth}")

            f.write(f",text_opacity:{str(int((int(TextOpacity)-100)*2.3))}")

            f.write("}\n")
        else: f.write(f"summon marker 0 0 0 {{Tags:[chat,master,{Ta}],CustomNameVisible:0b,CustomName:'{{\"text\":\"\"}}'}}\n")
        f.write(f"\n")
        f.write(f"# 文字設定\n")
        f.write(f"function chat:{FilePlace}basic/setup\n")
        if Mode == 1 and (float(Scale1) != 1.0 or float(Scale2) != 1.0): f.write(f"schedule function chat:{FilePlace}basic/transformation 1t\n")
        f.write(f"\n")
        f.write(f"# 聊天循環\n")
        f.write(f"scoreboard players set #len({Ta}) text_space 0\n")
        f.write(f"function chat:{FilePlace}basic/space_loop\n")
        f.write(f"\n")
        f.write(f"# ----- 指令擴充 ----- #\n")
        f.close
    if Mode == 1 and (float(Scale1) != 1.0 or float(Scale2) != 1.0): 
        with open(File_Trans,'w+',encoding='utf-8') as f:
            f.write(f"execute as @e[type=#minecraft:text,tag={Ta}] run data merge entity @s {{transformation:{{scale:[{Scale1}f,{Scale2}f,1.0f]}}}}")
    else:
        try:    os.remove(File_Trans)
        except: pass

def setup(File_setup,Textlen,Text,Texts,FilePlace,Ta,Prefix,IsDotSlow,SpaceDot,Space,DefShort,IsShortSentenceRapid,SpaceShort,SpaceLong,GenerateSkip, Serfix):
    global Textnum,Textcolor_sort,Textcolor_color,Texttrigger_num,Events
    Textnum = 0
    Events = []
    Textlen = len(Text)  
    Texts = []           
    Textcolor_sort = []
    Textcolor_color = []
    Textnum = 0
    Texttrigger_num = 0

    def color_cmd_vanish(i):
        global temp_one,temp_last,temp_color,Textcolor_color,Textcolor_sort,Textnum
        while "$color:" in i:
            temp_one = i.find("$color:")
            temp_last = i.find("$",temp_one+1)
            temp_color = i[temp_one+7:i.find("$",temp_last)]
            i = i.replace("$color:","",1)
            i = i.replace(""+temp_color+"$","",1)
        return i

    def trigger_cmd_vanish(i):
        global Textnum
        i = i.replace("#a","")
        i = i.replace("#\\a","#a")
        return i

    def all_cmd_vanish(i):
        global Textnum
        i = color_cmd_vanish(i)
        i = trigger_cmd_vanish(i)
        Textnum += len(i)
        return i, Textnum

    def color_command(i):
        global temp_one,temp_last,temp_color,Textcolor_color,Textcolor_sort,Textnum
        i = trigger_cmd_vanish(i)
        while "$color:" in i:
            temp_one = i.find("$color:")
            temp_last = i.find("$",temp_one+1)
            temp_color = i[temp_one+7:i.find("$",temp_last)]
            i = i.replace("$color:","",1)
            i = i.replace(""+temp_color+"$","",1)
            Textcolor_sort.append(temp_one)
            Textcolor_color.append(temp_color)
        i = i.replace("$\\","$")
        return i

    def trigger_command(i):
        global Texttrigger_num,Textnum
        #Texttrigger_num = int()
        i = color_cmd_vanish(i)
        temp = 0
        while '#a' in i:
            temp = i[:i.find("#a")].count("#\\a")
            Texttrigger_num -= temp
            Events.append(i.find("#a")+Texttrigger_num+1)
            i = i.replace("#a","",1)
        Texttrigger_num += len(i)
        return Events

    with open(File_setup,'w+',encoding='utf-8') as f:
        # (註解)顯示所有會產生出來的字 & 總字數
        if Textlen == 1:
            i = Text[0]
            temp = all_cmd_vanish(i)
            f.write('#String '+temp[0]+' ('+str(temp[1])+')')
        else:
            f.write('#String\n')
            for i in Text:
                temp = all_cmd_vanish(i)
                f.write('#'+temp[0]+' ('+str(temp[1])+')\n')


        for i in Text:

            Textcolor_sort = []
            Textcolor_color = []

            # 指令 "#a"
            Events = trigger_command(i)

            # 指令 "$color:"
            i      = color_command(i)

            for t in range(int(len(i))):
                Texts.append(i[0:t+1])

                # 把所有變色的地方都放上 #b
                for r in range(len(Textcolor_sort)): 
                    if len(Texts[-1]) >= Textcolor_sort[r]+r*2+1:
                        temp_list = list(Texts[-1])
                        temp_list.insert(Textcolor_sort[r]+r*2, "#b")
                        Texts[-1] = ''.join(temp_list)

                Texts[-1] = Texts[-1].replace("\\","\\\\\\\\")
                Texts[-1] = Texts[-1].replace("\"","\\\\\"")
                Texts[-1] = Texts[-1].replace("\'","\\\'")

                # 讓所有#b都變成顏色
                for r in range(len(Textcolor_color)): 
                    Texts[-1] = Texts[-1].replace("#b", "\"},{\"color\":\""+Textcolor_color[r]+"\",\"text\":\"",1)

                if int(len(i)) == (t+1):
                    Texts.append('$command$:long_string')


        f.write('\n\n')
        f.write(f'function chat:{FilePlace}basic/clear')
        f.write('\n\n')

        for i in range(int(len(Texts))):
            if Texts[i] != '$command$:long_string':
                f.write(f'data modify storage {Ta} Text append value \'["",{Prefix}{{"text":"{Texts[i]}"}}{Serfix}]\'')
                f.write('\n')
                if Texts[i+1] != '$command$:long_string':
                    f.write(f'data modify storage {Ta} Space append value ')
                    if Texts[i][-1] == '.' and IsDotSlow == True:
                        f.write(str(SpaceDot))
                    else:
                        f.write(str(Space))
                    f.write('\n')
            else:
                f.write(f'data modify storage {Ta} Space append value ')
                if len(Texts[i-1]) <= DefShort and IsShortSentenceRapid == True:
                    f.write(str(SpaceShort))
                else:
                    f.write(str(SpaceLong))
                if GenerateSkip == True: f.write(f'\nfunction chat:{FilePlace}skip/store')
                f.write('\n')

        f.write(f'data modify storage {Ta} Text append value \'(END.)\'')
        f.close
    return Events

def space(FilePlace,File_space,Ta,GenerateSkip,Mode,VisiblePlayer,Sound,Events,i,Sign_Pos):
    with open(File_space,'w+',encoding='utf-8') as f:
        f.write(f"## {Ta}\n")
        f.write(f"# 文字\n")
        f.write(f"scoreboard players add #len({Ta}) text_space 1\n")
        if GenerateSkip == True: f.write(f"execute store result score #len({Ta}_space) text_space run data get storage {Ta} Skip[0]\n")
        f.write(f"data modify block {Sign_Pos} Text1 set from storage {Ta} Text[0]\n")
        f.write(f"\n")
        f.write(f"# ----- 取代文字/間隔 ----- #\n")
        f.write(f"execute as @e[type=#minecraft:text,tag={Ta}] run data modify entity @s ")
        if Mode == 1:f.write("text")
        else: f.write("CustomName")
        f.write(f" set from block {Sign_Pos} Text1\n")
        f.write(f"execute as @e[type=#minecraft:text,tag={Ta}] store result score @s text_space run data get storage {Ta} Space[0]\n")
        if Mode == 2: f.write(f"title {VisiblePlayer} actionbar [{{\"selector\":\"@e[type=#minecraft:text,tag={Ta}]\"}}]\n")
        f.write(f"\n")
        f.write(f"# ----- 刪除文字/間隔 ----- #\n")
        f.write(f"data remove storage {Ta} Text[0]\n")
        f.write(f"data remove storage {Ta} Space[0]\n")
        if GenerateSkip == True: 
            f.write(f"execute if score #len({Ta}) text_space = #len({Ta}_space) text_space run data remove storage {Ta} Skip[0]\n")
            f.write(f"execute if score #len({Ta}) text_space = #len({Ta}_space) text_space run scoreboard players set @e[type=#minecraft:text,tag={Ta}] skip_cd 0\n")
        f.write("\n")
        f.write("# ----- 結束 ----- #\n")
        f.write(f"execute unless data storage {Ta} Text[0] run function chat:{FilePlace}-end\n")
        f.write("\n")
        f.write("# ----- 音效 ----- #\n")
        if Sound != '':
            if Mode != 2:f.write(f"execute as @e[type=#minecraft:text,tag={Ta}] at @s if data storage {Ta} Text[0] run {Sound}\n")
            else        :f.write(f"execute as {VisiblePlayer} at @s if data storage {Ta} Text[0] run {Sound}\n")
        f.write("\n")
        f.write("# ----- 指令擴充 ----- #\n")
        if len(Events) > 0:
            for i in Events:
                f.write(f"execute if score #len({Ta}) text_space matches {i} run say [cmd triggered.]\n")
        f.close

def end(File_end,Ta,FilePlace):
    with open(File_end,'w+',encoding='utf-8') as f:
        f.write(f"## {Ta}\n")
        f.write("# 刪除\n")
        f.write(f"execute as @e[type=#minecraft:text,tag={Ta}] run function chat:void\n")
        f.write("\n")
        f.write("# ----- 指令擴充 ----- #\n")
        f.close

def clear(File_clear,Ta):
    with open(File_clear,'w+',encoding='utf-8') as f:
        f.write(f"## {Ta}\n")
        f.write(f"data remove storage {Ta} Text\n")
        f.write(f"data remove storage {Ta} Space\n")
        f.write(f"data remove storage {Ta} Skip\n")
        f.write(f"data remove storage {Ta} tempskip\n")
        f.close

def skip(File_skip,File_skipl,File_skips,Ta,SkipCoolDown,FilePlace):
    with open(File_skip,'w+',encoding='utf-8') as f:
        f.write(f"## {Ta}\n")
        f.write("# ----- 間距計算 ----- #\n")
        f.write(f"execute store result score #skip text_space run data get storage {Ta} Skip[0]\n")
        f.write(f"scoreboard players operation #skip text_space -= #len({Ta}) text_space\n")
        f.write(f"scoreboard players remove #skip text_space 1\n")
        f.write(f"scoreboard players operation #len({Ta}) text_space += #skip text_space\n")
        f.write("\n")
        f.write("# ----- 刪除文字 ----- #\n")
        f.write(f"data remove storage {Ta} Skip[0]\n")
        f.write(f"execute if score @e[type=#minecraft:text,tag={Ta},tag=master,limit=1] skip_cd matches {SkipCoolDown}.. if score #skip text_space matches 1.. run function chat:{FilePlace}skip/loop\n")
        f.write("\n")
        f.write("# ----- 下一段開始 ----- #\n")
        f.write(f"execute as @e[type=#minecraft:text,tag={Ta},tag=master,limit=1] if score @s skip_cd matches {SkipCoolDown}.. run function chat:{FilePlace}basic/space_loop\n")
        f.write(f"scoreboard players set @e[type=#minecraft:text,tag={Ta},scores={{skip_cd={str(SkipCoolDown)}..}}] skip_cd 0\n")
        f.close
    with open(File_skipl,'w+',encoding='utf-8') as f:
        f.write(f"## {Ta}\n")
        f.write("# ----- 刪除 ----- #\n")
        f.write(f"data remove storage {Ta} Text[0]\n")
        f.write(f"data remove storage {Ta} Space[0]\n")
        f.write("\n")
        f.write("# ----- 循環 ----- #\n")
        f.write("scoreboard players remove #skip text_space 1\n")
        f.write("\n")
        f.write(f"execute if score #skip text_space matches 1.. run function chat:{FilePlace}skip/loop\n")
        f.close
    with open(File_skips,'w+',encoding='utf-8') as f:
        f.write(f"## {Ta}\n")
        f.write("# ----- 存入Skip分數 ----- #\n")
        f.write(f"execute store result score Skip text_space run data get storage {Ta} Space\n")
        f.write("scoreboard players add Skip text_space 1\n")
        f.write(f"execute store result storage {Ta} tempskip int 1 run scoreboard players get Skip text_space\n")
        f.write(f"data modify storage {Ta} Skip append from storage {Ta} tempskip\n")

def tick(File_tick,Ta,FilePlace):
    with open(File_tick,'r',encoding='utf-8') as f:
        temp = []
        if not f"execute if entity @s[tag={Ta}] run function chat:{FilePlace}basic/space_loop" in f.read():
            with open(File_tick,'a+',encoding='utf-8') as f:
                f.write(f"\nexecute if entity @s[tag={Ta}] run function chat:{FilePlace}basic/space_loop")
                f.close()
    with open(File_tick,'r',encoding='utf-8') as f:
        for i in f.readlines():
            if   i == "\n" or i[0] == "#": temp.append(i)
            elif not os.path.isfile(__file__.replace("\\", "/").replace("chat/ctgnrt/main.py", "")+i[i.find("function ")+9:].replace(":","/functions/").replace("\n","")+".mcfunction"): break
            else:temp.append(i)
        with open(File_tick, "w+", encoding="utf-8") as f2:
            for i in temp: f2.write(i)
            f2.close()