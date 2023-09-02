# ----- tatest.2 ----- #
# 位置
kill @e[type=#minecraft:text,tag=tatest.2]
execute rotated ~ 0 positioned ^ ^1 ^2 run summon text_display ~ ~ ~ {Tags:[chat,master,tatest.2],CustomNameVisible:0b,text:'{"text":""}',billboard:"center",alignment:"center",line_width:0,text_opacity:0}

# 文字設定
function chat:test/2/basic/setup
schedule function chat:test/2/basic/transformation 1t

# 聊天循環
scoreboard players set #len(tatest.2) text_space 0
function chat:test/2/basic/space_loop

# ----- 指令擴充 ----- #
