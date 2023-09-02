## tatest.1
# 文字
scoreboard players add #len(tatest.1) text_space 1
data modify block 0 0 0 Text1 set from storage tatest.1 Text[0]

# ----- 取代文字/間隔 ----- #
execute as @e[type=#minecraft:text,tag=tatest.1] run data modify entity @s CustomName set from block 0 0 0 Text1
execute as @e[type=#minecraft:text,tag=tatest.1] store result score @s text_space run data get storage tatest.1 Space[0]

# ----- 刪除文字/間隔 ----- #
data remove storage tatest.1 Text[0]
data remove storage tatest.1 Space[0]

# ----- 結束 ----- #
execute unless data storage tatest.1 Text[0] run function chat:test/1/-end

# ----- 音效 ----- #
execute as @e[type=#minecraft:text,tag=tatest.1] at @s if data storage tatest.1 Text[0] run function chat:sounds/default

# ----- 指令擴充 ----- #
execute if score #len(tatest.1) text_space matches 19 run say [cmd triggered.]
