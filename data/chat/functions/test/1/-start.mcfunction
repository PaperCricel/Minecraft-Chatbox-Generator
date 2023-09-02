# ----- tatest.1 ----- #
# 位置
kill @e[type=#minecraft:text,tag=tatest.1]
execute rotated ~ 0 positioned ^ ^1 ^2 run summon area_effect_cloud ~ ~ ~ {Tags:[chat,master,tatest.1],CustomNameVisible:1b,CustomName:'{"text":""}',Duration:1000000000}

# 文字設定
function chat:test/1/basic/setup

# 聊天循環
scoreboard players set #len(tatest.1) text_space 0
function chat:test/1/basic/space_loop

# ----- 指令擴充 ----- #
