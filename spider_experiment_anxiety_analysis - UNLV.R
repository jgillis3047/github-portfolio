# Install Packages
install.packages("data.table")
install.packages("dplyr")
install.packages("ggplot2")
#if you got an error on ggplot, please install "cli"
install.packages("cli")

# Library Read
library(data.table)
library(dplyr)
library(ggplot2)

# 9.5.2.2. Define the groups 
Group <- gl(2, 12, labels = c("Picture", "Real Spider"))

# 9.5.2.2 Define the anxiety scores 
Anxiety <- c(30, 35, 45, 40, 50, 35, 55, 25, 30, 45, 40, 50, 40, 35, 50, 55, 65, 55, 50, 35, 30, 50, 60, 39)

# 9.5.2.2 Combine into a dataframe 
spiderLong <- data.frame(Group, Anxiety)

# 9.5.2.2 Display the dataframe 
print(spiderLong)

# 9.5.2.5 Perform an independent t-test using data in long format
ind_t_test <- t.test(Anxiety ~ Group, data = spiderLong, paired = FALSE)

# 9.5.2.5 View the results 
print(ind_t_test)

# 9.6.3.2 Create variables for the anxiety scores 
picture <- c(30, 35, 45, 40, 50, 35, 55, 25, 30, 45, 40, 50)
real <- c(40, 35, 50, 55, 65, 55, 50, 35, 30, 50, 60, 39)

# 9.6.3.2 Merge variables into a dataframe titled spiderWide 
spiderWide <- data.frame(picture, real)

# 9.6.3.2 Display the spiderWide dataframe
print(spiderWide)

# 9.6.3.5 Perform a dependent t-test comparing 'real' and 'picture' conditions 
dep_t_test <- t.test(spiderWide$real, spiderWide$picture, paired = TRUE)

# 9.6.3.5 View the results of the test 
print(dep_t_test)