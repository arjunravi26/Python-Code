import pandas

student_dict = {'names': ['Arjun', 'Althaf', 'Jishnu', 'Sijo'], 'score': [50, 100, 29, 30]}
df = pandas.DataFrame(student_dict)
# print(df)

# Loop through a df

for (index, row) in df.iterrows():
    print(row)
