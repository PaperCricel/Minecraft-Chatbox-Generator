## tatest.3
# ----- 刪除 ----- #
data remove storage tatest.3 Text[0]
data remove storage tatest.3 Space[0]

# ----- 循環 ----- #
scoreboard players remove #skip text_space 1

execute if score #skip text_space matches 1.. run function chat:test/3/skip/loop
