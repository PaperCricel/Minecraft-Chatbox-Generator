## tatest.2
# ----- 刪除 ----- #
data remove storage tatest.2 Text[0]
data remove storage tatest.2 Space[0]

# ----- 循環 ----- #
scoreboard players remove #skip text_space 1

execute if score #skip text_space matches 1.. run function chat:test/2/skip/loop
