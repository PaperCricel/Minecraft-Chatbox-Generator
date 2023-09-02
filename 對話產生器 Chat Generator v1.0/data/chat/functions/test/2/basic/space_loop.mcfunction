## tatest.2
# 文字
scoreboard players add #len(tatest.2) text_space 1
execute store result score #len(tatest.2_space) text_space run data get storage tatest.2 Skip[0]
data modify block 0 0 0 Text1 set from storage tatest.2 Text[0]

# ----- 取代文字/間隔 ----- #
execute as @e[type=#minecraft:text,tag=tatest.2] run data modify entity @s text set from block 0 0 0 Text1
execute as @e[type=#minecraft:text,tag=tatest.2] store result score @s text_space run data get storage tatest.2 Space[0]

# ----- 刪除文字/間隔 ----- #
data remove storage tatest.2 Text[0]
data remove storage tatest.2 Space[0]
execute if score #len(tatest.2) text_space = #len(tatest.2_space) text_space run data remove storage tatest.2 Skip[0]
execute if score #len(tatest.2) text_space = #len(tatest.2_space) text_space run scoreboard players set @e[type=#minecraft:text,tag=tatest.2] skip_cd 0

# ----- 結束 ----- #
execute unless data storage tatest.2 Text[0] run function chat:test/2/-end

# ----- 音效 ----- #
execute as @e[type=#minecraft:text,tag=tatest.2] at @s if data storage tatest.2 Text[0] run function chat:sounds/default

# ----- 指令擴充 ----- #
execute if score #len(tatest.2) text_space matches 19 run say [cmd triggered.]
