import pandas as pd
from pydataset import data
mpg = data('mpg')
mpg

# On average, which manufacturer has the best miles per gallon?
extract = mpg.groupby(mpg.manufacturer)[['hwy']].mean().sort_values(by='hwy', ascending = False)
extract

indexNamesArr = extract.index.values # retrieve the index of manufacturer
indexNamesArr
print("The manufacturer producing the best mpg car is: {}".format(indexNamesArr[0])) 
# The manufacturer producing the best mpg car is: honda 

# How many different manufacturers are there?
print("There are {} manufacturers in the dataset".format(mpg.manufacturer.nunique()))
# There are 15 manufacturers in the dataset

# # How many different models are there?
model_count = mpg.groupby(["manufacturer","model"])["model"].count()
model_count
manufacturer  model                 
audi          a4                         7
              a4 quattro                 8
              a6 quattro                 3
chevrolet     c1500 suburban 2wd         5
              corvette                   5
              k1500 tahoe 4wd            4
              malibu                     5
dodge         caravan 2wd               11
              dakota pickup 4wd          9
              durango 4wd                7
              ram 1500 pickup 4wd       10
ford          expedition 2wd             3
              explorer 4wd               6
              f150 pickup 4wd            7
              mustang                    9
honda         civic                      9
hyundai       sonata                     7
              tiburon                    7
jeep          grand cherokee 4wd         8
land rover    range rover                4
lincoln       navigator 2wd              3
mercury       mountaineer 4wd            4
nissan        altima                     6
              maxima                     3
              pathfinder 4wd             4
pontiac       grand prix                 5
subaru        forester awd               6
              impreza awd                8
toyota        4runner 4wd                6
              camry                      7
              camry solara               7
              corolla                    5
              land cruiser wagon 4wd     2
              toyota tacoma 4wd          7
volkswagen    gti                        5
              jetta                      9
              new beetle                 6
              passat                     7
Name: model, dtype: int64

# Do automatic or manual cars have better miles per gallon?
mpg[["trans","trans_app"]] = mpg.trans.str.split("(",expand = True) # pre-process transmission data
mpg

mpg.assign(avg_hwy_mileage_by_transmission = mpg.groupby("trans").hwy.transform("mean")).sort_values(by=['model','trans'])


# The transform method can be used to produce a series with the same length of the original dataframe 
# where each value represents the aggregation from the grouped by subgroup. 
# For example, if we wanted to know the average math grade for each classroom, 
# and add this data back to our original dataframe


# Joining and Merging

# Use USER & ROLE dataframe -

# What happens if you drop the foreign keys from the dataframes and try to merge them?
# won't be able to join, because there's no reference

# What do you think a right join would look like? An outer join? 

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

0	1	bob	1.0
1	2	joe	2.0
2	3	sally	3.0
3	4	adam	3.0
4	5	jane	NaN
5	6	mike	NaN

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

0	1	admin
1	2	author
2	3	reviewer
3	4	commenter

# default = left join
norm_left = users.join(roles, lsuffix='_role_id', rsuffix='_id')
norm_left

# right join, some users without role_id info are gone
right_join = users.join(roles, how = 'right', lsuffix='_role_id', rsuffix='_id')
right_join


0	1	bob	1.0	1	admin
1	2	joe	2.0	2	author
2	3	sally	3.0	3	reviewer
3	4	adam	3.0	4	commen

# outer join, include everything, no directional relationship
outer_join = users.join(roles, how = 'outer', lsuffix='_role_id', rsuffix='_id')
outer_join