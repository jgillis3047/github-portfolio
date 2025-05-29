# 6.5.1: Install required packages 
install.packages("Hmisc")
install.packages("polycor")
install.packages("ggplot2")
install.packages("ggm")


# 6.5.1: Load the packages 
library(boot)
library(ggm)
library(ggplot2)
library(Hmisc)
library(polycor)

# 6.5.3: Import Data
examData <- read.delim("Exam Anxiety.dat", header = TRUE)

# 6.5.3: Prepare Data, remove fifth column
examData <- examData[, -5]

# 6.5.3: Install and load the 'dplyr' package
install.packages("dplyr")
library(dplyr)

# 6.5.3: Convert factors to numeric as necessary
examData <- examData %>% mutate(Code = as.numeric(Code))
examData <- examData %>% mutate(Revise = as.numeric(Revise))
examData <- examData %>% mutate(Exam = as.numeric(Exam))
examData <- examData %>% mutate(Anxiety = as.numeric(Anxiety))
examDataMatrix <- as.matrix(examData)

# 6.5.3: Run 'rcorr()' on Matrix
rcorrResult <- rcorr(examDataMatrix, type = "pearson")

# 6.5.3: Convert Matrix Back to Data Frame for 'cor.test()'
examData <- as.data.frame(examDataMatrix)

# 6.5.3: Run 'cor.test()'
corTestResult <- cor.test(examData$Exam, examData$Anxiety, method = "pearson")
corTestResult <- cor.test(examData$Exam, examData$Anxiety, alternative = "less", method = "pearson", conf.level = 0.99)
