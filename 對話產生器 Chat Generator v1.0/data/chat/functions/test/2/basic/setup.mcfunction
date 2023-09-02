#String
#早安阿早安:D (7)
#這是測試用文字.. (16)
#應該... (21)
#沒有問題 (25)


function chat:test/2/basic/clear

data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"早"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"早安"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"早安阿"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"早安阿早"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"早安阿早安"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"早安阿早安:"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"早安阿早安:D"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 20
function chat:test/2/skip/store
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這是"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這是"},{"color":"yellow","text":"測"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這是"},{"color":"yellow","text":"測試"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這是"},{"color":"yellow","text":"測試"},{"color":"white","text":"用"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這是"},{"color":"yellow","text":"測試"},{"color":"white","text":"用文"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這是"},{"color":"yellow","text":"測試"},{"color":"white","text":"用文字"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這是"},{"color":"yellow","text":"測試"},{"color":"white","text":"用文字."},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 5
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"這是"},{"color":"yellow","text":"測試"},{"color":"white","text":"用文字.."},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 20
function chat:test/2/skip/store
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"應"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"應該"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"應該."},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 5
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"應該.."},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 5
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"應該..."},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 20
function chat:test/2/skip/store
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"沒"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"沒有"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"沒有問"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 2
data modify storage tatest.2 Text append value '["",{"text":"⨇","color":"gray"},{"text":"沒有問題"},{"text":"⨈","color":"gray"}]'
data modify storage tatest.2 Space append value 15
function chat:test/2/skip/store
data modify storage tatest.2 Text append value '(END.)'