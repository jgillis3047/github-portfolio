# 5.4 Install packages 
install.packages("car")
install.packages("ggplot2")
install.packages("pastecs")
install.packages("psych")

# 5.4 Load Packages 
library(car)
library(ggplot2)
library(pastecs)
library(psych)

# 5.5.1 Read the Data 
dlf <- read.delim("DownloadFestival.dat", header=TRUE)


# 5.5.1 Create Histogram with Normal Curves 
hist.day1 <- ggplot(dlf, aes(x = day1)) + geom_histogram(aes(y = ..density..), colour = "black", fill = "white") + labs(x = "Hygiene score on day 1", y = "Density") + geom_density(alpha = 0.2, fill = "#FF6666") + stat_function(fun = dnorm, args = list(mean = mean(dlf$day1, na.rm = TRUE), sd = sd(dlf$day1, na.rm = TRUE)), colour = "black", size=1)
hist.day1

# 5.5.1 Create Q-Q Plots 
qqplot.day1 <- ggplot(dlf, aes(sample = day1)) + stat_qq() + stat_qq_line() + labs(title = "Q-Q Plot for Day 1 Hygiene Scores")
qqplot.day1


# 5.6.1 The Shapiro-Wilk test
rexam <- read.delim("RExam.dat", header=TRUE)
shapiro.test(rexam$exam)
shapiro.test(rexam$numeracy)

# 5.6.1 Advanced Usage 
by(rexam$exam, rexam$uni, shapiro.test)
by(rexam$numeracy, rexam$uni, shapiro.test)
