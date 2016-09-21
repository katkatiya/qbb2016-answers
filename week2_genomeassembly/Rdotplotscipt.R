velvetlow=read.table("/Users/cmdb/qbb2016-answers/week2_genomeassembly/velveth/velvetlow", header=T)
plot.default(velvetlow)

velvethigh=read.table("/Users/cmdb/qbb2016-answers/week2_genomeassembly/velveth/velvethigh", header=T)
plot.default(velvethigh)

spadeslow=read.table("/Users/cmdb/qbb2016-answers/week2_genomeassembly/spades/spadeslow", header=T)
plot.default(spadeslow)

spadeshigh=read.table("/Users/cmdb/qbb2016-answers/week2_genomeassembly/spades/spadeshigh", header=T)
plot.default(spadeshigh)