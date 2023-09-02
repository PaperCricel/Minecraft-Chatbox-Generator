# ----- tatest.4 ----- #
# 位置
kill @e[type=#minecraft:text,tag=tatest.4]
execute positioned ~ ~ ~ run summon text_display ~ ~ ~ {Tags:[chat,master,tatest.4],CustomNameVisible:0b,text:'{"text":""}',billboard:"center",alignment:"center",background:0,text_opacity:0}

# 文字設定
function chat:test/4/basic/setup

# 聊天循環
scoreboard players set #len(tatest.4) text_space 0
function chat:test/4/basic/space_loop

# ----- 指令擴充 ----- #
