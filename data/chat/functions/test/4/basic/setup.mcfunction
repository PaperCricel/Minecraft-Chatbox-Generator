#String   (1)

function chat:test/4/basic/clear

data modify storage tatest.4 Text append value '["",{"text":" "}]'
data modify storage tatest.4 Space append value 20
data modify storage tatest.4 Text append value '(END.)'