
# cooldown
scoreboard players remove @s[tag=!chat.stop,scores={text_space=1..}] text_space 1
scoreboard players add @s[tag=!chat.stop] skip_cd 1

# text updating
execute if entity @s[tag=master,scores={text_space=0}] run function chat:space

# ----- 特定字串執行 ----- #

execute if entity @s[tag=ta1] at @p rotated 180 0 run tp @s ^ ^1 ^2