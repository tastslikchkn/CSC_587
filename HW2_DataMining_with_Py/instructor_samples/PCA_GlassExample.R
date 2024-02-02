library(ggplot2)
glass = read.csv('glass.csv')
load('forensic_glass.rda')

head(glass)

data = glass[, 3:10]

data_pca = prcomp(data)

data_mapped = as.data.frame(data_pca$x)

head(data_pca)

ggplot(data=data_mapped, aes(x=PC1, y=PC2)) + geom_point(aes(color=glass$type))

ggplot(data=glass, aes(x=Na, y=Fe)) + geom_point(aes(color=type))

barplot(data_pca$sdev)
