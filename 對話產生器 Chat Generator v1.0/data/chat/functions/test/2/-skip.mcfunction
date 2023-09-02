## tatest.2
# ----- 間距計算 ----- #
execute store result score #skip text_space run data get storage tatest.2 Skip[0]
scoreboard players operation #skip text_space -= #len(tatest.2) text_space
scoreboard players remove #skip text_space 1
scoreboard players operation #len(tatest.2) text_space += #skip text_space

# ----- 刪除文字 ----- #
data remove storage tatest.2 Skip[0]
execute if score @e[type=#minecraft:text,tag=tatest.2,tag=master,limit=1] skip_cd matches 20.. if score #skip text_space matches 1.. run function chat:test/2/skip/loop

# ----- 下一段開始 ----- #
execute as @e[type=#minecraft:text,tag=tatest.2,tag=master,limit=1] if score @s skip_cd matches 20.. run function chat:test/2/basic/space_loop
scoreboard players set @e[type=#minecraft:text,tag=tatest.2,scores={skip_cd=20..}] skip_cd 0
