# 7.3 Install necessary packages 
install.packages("car")
install.packages("QuantPsyc")

# 7.3 Load necessary packages 
library(car)
library(QuantPsyc)

# 7.4.2 Read data from the 'Album Sales 1.dat' file
album1 <- read.delim("Album Sales 1.dat", header = TRUE)

# 7.4.2 Perform linear regression with 'sales' as response and 'adverts' as predictor
albumSales.lm <- lm(sales ~ adverts, data = album1)

# 7.5 Display the summary of the regression model
summary(albumSales.lm)

# 7.5 Print the Pearson correlation coefficient 
print(sqrt(summary(albumSales.lm)$r.squared))
