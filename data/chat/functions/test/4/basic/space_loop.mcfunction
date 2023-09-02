## tatest.4
# 文字
scoreboard players add #len(tatest.4) text_space 1
data modify block 0 0 0 Text1 set from storage tatest.4 Text[0]

# ----- 取代文字/間隔 ----- #
execute as @e[type=#minecraft:text,tag=tatest.4] run data modify entity @s text set from block 0 0 0 Text1
execute as @e[type=#minecraft:text,tag=tatest.4] store result score @s text_space run data get storage tatest.4 Space[0]

# ----- 刪除文字/間隔 ----- #
data remove storage tatest.4 Text[0]
data remove storage tatest.4 Space[0]

# ----- 結束 ----- #
execute unless data storage tatest.4 Text[0] run function chat:test/4/-end

# ----- 音效 ----- #

# ----- 指令擴充 ----- #
