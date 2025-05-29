# 10.6.1 - Installing necessary packages for one-way ANOVA
install.packages("compute.es")
install.packages("car")
install.packages("ggplot2")
install.packages("multcomp")
install.packages("pastecs")

# 10.6.1 - Loading installed packages
library(car)
library(ggplot2)
library(multcomp)
library(pastecs)

# 10.6.3 - Entering the data for analysis 
libido <- c(3, 2, 1, 1, 4, 5, 2, 4, 5, 3, 6, 4, 5, 3, 6) # vector containing libido scores
dose <- gl(3, 5, labels = c("Placebo", "Low Dose", "High Dose")) # factor variable for dose groups 
viagraData <- data.frame(dose, libido) # combine vectors into a data frame

# 10.6.6.1 - Conduct the main analysis 
viagraModel <- lm(libido ~ dose, data = viagraData) # linear model with libido
summary(viagraModel) # summary statistics of the model, including coefficients and significance
plot(viagraModel) # plot for linear model that checks for assumptions and outliers
