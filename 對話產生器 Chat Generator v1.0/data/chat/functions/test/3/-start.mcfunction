# ----- tatest.3 ----- #
# 位置
kill @e[type=#minecraft:text,tag=tatest.3]
execute rotated ~ 0 positioned ^ ^1 ^2 run summon area_effect_cloud ~ ~ ~ {Tags:[chat,master,tatest.3],CustomNameVisible:1b,CustomName:'{"text":""}',Duration:1000000000}

# 文字設定
function chat:test/3/basic/setup

# 聊天循環
scoreboard players set #len(tatest.3) text_space 0
function chat:test/3/basic/space_loop

# ----- 指令擴充 ----- #
