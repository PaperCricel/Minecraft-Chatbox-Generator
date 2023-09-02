## tatest.3
# ----- 存入Skip分數 ----- #
execute store result score Skip text_space run data get storage tatest.3 Space
scoreboard players add Skip text_space 1
execute store result storage tatest.3 tempskip int 1 run scoreboard players get Skip text_space
data modify storage tatest.3 Skip append from storage tatest.3 tempskip
