Imagine subset and index as if it's SQL

mpg[mpg.hwy > 35]
select * from mpg where hwy > 35

mpg[mpg.hwy > 35][["hwy", "model"]]
select hwy, model from mpg where hwy > 35

mpg[["hwy","model"]] # need to use double square bracket when selecting more than 1 column
select hwy, model from mpg

mpg.hwy = mpg["hwy"] # if more than 1 column then can't use dot method


