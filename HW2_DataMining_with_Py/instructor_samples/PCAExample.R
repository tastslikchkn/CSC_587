
mu = colMeans(USArrests)

USArrestspca = prcomp(USArrests)

nComp = 4
USArrestshat = USArrestspca$x[,1:nComp] %*% t(USArrestspca$rotation[,1:nComp])
USArrestshat = scale(USArrestshat, center = -mu, scale = FALSE)
