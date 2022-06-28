# Add the Pandas dependency.
import pandas as pd
import os
# Files to load
school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")
# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df
School ID	school_name	type	size	budget
0	0	Huang High School	District	2917	1910635
1	1	Figueroa High School	District	2949	1884411
2	2	Shelton High School	Charter	1761	1056600
3	3	Hernandez High School	District	4635	3022020
4	4	Griffin High School	Charter	1468	917500
5	5	Wilson High School	Charter	2283	1319574
6	6	Cabrera High School	Charter	1858	1081356
7	7	Bailey High School	District	4976	3124928
8	8	Holden High School	Charter	427	248087
9	9	Pena High School	Charter	962	585858
10	10	Wright High School	Charter	1800	1049400
11	11	Rodriguez High School	District	3999	2547363
12	12	Johnson High School	District	4761	3094650
13	13	Ford High School	District	2739	1763916
14	14	Thomas High School	Charter	1635	1043130
school_data_df.head(10)
School ID	school_name	type	size	budget
0	0	Huang High School	District	2917	1910635
1	1	Figueroa High School	District	2949	1884411
2	2	Shelton High School	Charter	1761	1056600
3	3	Hernandez High School	District	4635	3022020
4	4	Griffin High School	Charter	1468	917500
5	5	Wilson High School	Charter	2283	1319574
6	6	Cabrera High School	Charter	1858	1081356
7	7	Bailey High School	District	4976	3124928
8	8	Holden High School	Charter	427	248087
9	9	Pena High School	Charter	962	585858
school_data_df.tail(10)
School ID	school_name	type	size	budget
5	5	Wilson High School	Charter	2283	1319574
6	6	Cabrera High School	Charter	1858	1081356
7	7	Bailey High School	District	4976	3124928
8	8	Holden High School	Charter	427	248087
9	9	Pena High School	Charter	962	585858
10	10	Wright High School	Charter	1800	1049400
11	11	Rodriguez High School	District	3999	2547363
12	12	Johnson High School	District	4761	3094650
13	13	Ford High School	District	2739	1763916
14	14	Thomas High School	Charter	1635	1043130
# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()
Student ID	student_name	gender	grade	school_name	reading_score	math_score
0	0	Paul Bradley	M	9th	Huang High School	66	79
1	1	Victor Smith	M	12th	Huang High School	94	61
2	2	Kevin Rodriguez	M	12th	Huang High School	90	60
3	3	Dr. Richard Scott	M	12th	Huang High School	67	58
4	4	Bonnie Ray	F	9th	Huang High School	97	84
# Determine if there are any missing values in the school data.
school_data_df.count()
School ID      15
school_name    15
type           15
size           15
budget         15
dtype: int64
# Determin any missing values in the student data 
student_data_df.count()
Student ID       39170
student_name     39170
gender           39170
grade            39170
school_name      39170
reading_score    39170
math_score       39170
dtype: int64
# Determine if there are any missing values in the school data.
school_data_df.isnull()
School ID	school_name	type	size	budget
0	False	False	False	False	False
1	False	False	False	False	False
2	False	False	False	False	False
3	False	False	False	False	False
4	False	False	False	False	False
5	False	False	False	False	False
6	False	False	False	False	False
7	False	False	False	False	False
8	False	False	False	False	False
9	False	False	False	False	False
10	False	False	False	False	False
11	False	False	False	False	False
12	False	False	False	False	False
13	False	False	False	False	False
14	False	False	False	False	False
# Determine if there are any missing values in the school data.
student_data_df.isnull()
Student ID	student_name	gender	grade	school_name	reading_score	math_score
0	False	False	False	False	False	False	False
1	False	False	False	False	False	False	False
2	False	False	False	False	False	False	False
3	False	False	False	False	False	False	False
4	False	False	False	False	False	False	False
...	...	...	...	...	...	...	...
39165	False	False	False	False	False	False	False
39166	False	False	False	False	False	False	False
39167	False	False	False	False	False	False	False
39168	False	False	False	False	False	False	False
39169	False	False	False	False	False	False	False
39170 rows × 7 columns

# Determine if there are any missing values in the school data.
student_data_df.isnull().sum()
Student ID       0
student_name     0
gender           0
grade            0
school_name      0
reading_score    0
math_score       0
dtype: int64
student_data_df.notnull().sum()
Student ID       39170
student_name     39170
gender           39170
grade            39170
school_name      39170
reading_score    39170
math_score       39170
dtype: int64
# Determine data types for the school DataFrame.
school_data_df.dtypes
School ID       int64
school_name    object
type           object
size            int64
budget          int64
dtype: object
school_data_df.budget.dtype
dtype('int64')
school_data_df["budget"].dtype
dtype('int64')
school_data_df["budget"].dtype
dtype('int64')
# Determine data types for the student DataFrame.
student_data_df.dtypes
Student ID        int64
student_name     object
gender           object
grade            object
school_name      object
reading_score     int64
math_score        int64
dtype: object
student_data_df.dtypes
Student ID        int64
student_name     object
gender           object
grade            object
school_name      object
reading_score     int64
math_score        int64
dtype: object
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ","Mr. ", "Ms. ", "Mrs. ","Miss ", " MD", " DDS", " DVM", " PhD"]

# iterate through the prefixes and suffixes and replace it with empty striing on studenta_data_df 
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"") 
student_data_df.head(10)
C:\Users\raney\AppData\Local\Temp/ipykernel_23600/2965979375.py:6: FutureWarning: The default value of regex will change from True to False in a future version.
  student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
Student ID	student_name	gender	grade	school_name	reading_score	math_score
0	0	Paul Bradley	M	9th	Huang High School	66	79
1	1	Victor Smith	M	12th	Huang High School	94	61
2	2	Kevin Rodriguez	M	12th	Huang High School	90	60
3	3	Richard Scott	M	12th	Huang High School	67	58
4	4	Bonnie Ray	F	9th	Huang High School	97	84
5	5	Bryan Miranda	M	9th	Huang High School	94	94
6	6	Sheena Carter	F	11th	Huang High School	82	80
7	7	Nicole Baker	F	12th	Huang High School	96	69
8	8	Michael Roth	M	10th	Huang High School	95	87
9	9	Matthew Greene	M	10th	Huang High School	96	84
school_data_complete_df = pd.merge(school_data_df,student_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()
School ID	school_name	type	size	budget	Student ID	student_name	gender	grade	reading_score	math_score
0	0	Huang High School	District	2917	1910635	0	Paul Bradley	M	9th	66	79
1	0	Huang High School	District	2917	1910635	1	Victor Smith	M	12th	94	61
2	0	Huang High School	District	2917	1910635	2	Kevin Rodriguez	M	12th	90	60
3	0	Huang High School	District	2917	1910635	3	Richard Scott	M	12th	67	58
4	0	Huang High School	District	2917	1910635	4	Bonnie Ray	F	9th	97	84
school_data_complete_df = pd.merge(student_data_df,school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
0	0	Paul Bradley	M	9th	Huang High School	66	79	0	District	2917	1910635
1	1	Victor Smith	M	12th	Huang High School	94	61	0	District	2917	1910635
2	2	Kevin Rodriguez	M	12th	Huang High School	90	60	0	District	2917	1910635
3	3	Richard Scott	M	12th	Huang High School	67	58	0	District	2917	1910635
4	4	Bonnie Ray	F	9th	Huang High School	97	84	0	District	2917	1910635
# Get the total number of students.
student_count = school_data_complete_df.count()
student_count
Student ID       39170
student_name     39170
gender           39170
grade            39170
school_name      39170
reading_score    39170
math_score       39170
School ID        39170
type             39170
size             39170
budget           39170
dtype: int64
school_data_complete_df["Student ID"].count()
39170
student_count = school_data_complete_df["Student ID"].count()
student_count
39170
# Calculate the total number of schools.
school_count = school_data_df["school_name"].count()
school_count
15
# Calculate the total number of schools
school_count2 = len(school_data_complete_df["school_name"].unique())
school_count2
15
# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget
24649428
# Calculate the average reading score
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score
81.87784018381414
# Calculate the average math score
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score
78.98537145774827
passing_math = school_data_complete_df["math_score"] >= 70
passing_math
0         True
1        False
2        False
3        False
4         True
         ...  
39165     True
39166     True
39167     True
39168     True
39169     True
Name: math_score, Length: 39170, dtype: bool
passing_reading = school_data_complete_df["reading_score"] >= 70
passing_reading
0        False
1         True
2         True
3        False
4         True
         ...  
39165     True
39166     True
39167     True
39168     True
39169     True
Name: reading_score, Length: 39170, dtype: bool
# get all student who passed math in a new data frame
passing_math_df = school_data_complete_df[school_data_complete_df["math_score"] >=70 ]
passing_math_df.head()
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
0	0	Paul Bradley	M	9th	Huang High School	66	79	0	District	2917	1910635
4	4	Bonnie Ray	F	9th	Huang High School	97	84	0	District	2917	1910635
5	5	Bryan Miranda	M	9th	Huang High School	94	94	0	District	2917	1910635
6	6	Sheena Carter	F	11th	Huang High School	82	80	0	District	2917	1910635
8	8	Michael Roth	M	10th	Huang High School	95	87	0	District	2917	1910635
# get all student who passed reading in a new data frame
passing_reading_df = school_data_complete_df[school_data_complete_df["reading_score"] >=70 ]
passing_reading_df.head()
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
1	1	Victor Smith	M	12th	Huang High School	94	61	0	District	2917	1910635
2	2	Kevin Rodriguez	M	12th	Huang High School	90	60	0	District	2917	1910635
4	4	Bonnie Ray	F	9th	Huang High School	97	84	0	District	2917	1910635
5	5	Bryan Miranda	M	9th	Huang High School	94	94	0	District	2917	1910635
6	6	Sheena Carter	F	11th	Huang High School	82	80	0	District	2917	1910635
# Calculate the number of students passing math.
passing_math_count = passing_math_df["student_name"].count()

# Calculate the number of students passing reading.
passing_reading_count = passing_reading_df["student_name"].count()

print(passing_math_count)
print(passing_reading_count)
29370
33610
#Total student count
student_count = school_data_complete_df["Student ID"].count()

# Calculate the percentage that passed the  math
passing_math_percentage = passing_math_count/float(student_count) * 100

# Calculate the percentage that passed the reading
passing_reading_percentage = passing_reading_count/float(student_count) * 100

print(passing_math_percentage)
print(passing_reading_percentage)
74.9808526933878
85.80546336482001
# Calculate the students who passed both math and reading.

passing_math_reading_df = school_data_complete_df[(school_data_complete_df["math_score"] >=70)  & (school_data_complete_df["reading_score"] >=70)] 

passing_math_reading_df
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
4	4	Bonnie Ray	F	9th	Huang High School	97	84	0	District	2917	1910635
5	5	Bryan Miranda	M	9th	Huang High School	94	94	0	District	2917	1910635
6	6	Sheena Carter	F	11th	Huang High School	82	80	0	District	2917	1910635
8	8	Michael Roth	M	10th	Huang High School	95	87	0	District	2917	1910635
9	9	Matthew Greene	M	10th	Huang High School	96	84	0	District	2917	1910635
...	...	...	...	...	...	...	...	...	...	...	...
39165	39165	Donna Howard	F	12th	Thomas High School	99	90	14	Charter	1635	1043130
39166	39166	Dawn Bell	F	10th	Thomas High School	95	70	14	Charter	1635	1043130
39167	39167	Rebecca Tanner	F	9th	Thomas High School	73	84	14	Charter	1635	1043130
39168	39168	Desiree Kidd	F	10th	Thomas High School	99	90	14	Charter	1635	1043130
39169	39169	Carolyn Jackson	F	11th	Thomas High School	95	75	14	Charter	1635	1043130
25528 rows × 11 columns

#calculate the count of students wh passed both math and reading

overall_passing_count = passing_math_reading_df["Student ID"].count()

#Calculate the Percentage of students wh passed both math and reading

overall_passing_percentage = overall_passing_count/float(student_count) * 100

overall_passing_percentage
65.17232575950983
# Adding a list of values with keys to create a new DataFrame.

district_summary_df = pd.DataFrame([{"Total Schools" : school_count, 
                                     "Total Students" : student_count,
                                     "Total Budget" : total_budget,                            
                                     "Average Reading Score" : average_reading_score, 
                                     "Average Math Score" : average_math_score,
                                     "% Passing Reading" : passing_reading_percentage,
                                     "% Passing Math" : passing_math_percentage,                                     
                                     "Overall Passing" : overall_passing_percentage
                                     
                                    }])

district_summary_df
Total Schools	Total Students	Total Budget	Average Reading Score	Average Math Score	% Passing Reading	% Passing Math	Overall Passing
0	15	39170	24649428	81.87784	78.985371	85.805463	74.980853	65.172326
# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}" .format)
district_summary_df["Total Students"]
0    39,170
Name: Total Students, dtype: object
# Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".

district_summary_df["Total Budget"]  = district_summary_df["Total Budget"].map("${:,.2f}".format)
district_summary_df["Total Budget"] 
0    $24,649,428.00
Name: Total Budget, dtype: object
district_summary_df["Average Reading Score"]  = district_summary_df["Average Reading Score"].map("{:.1f}".format)
district_summary_df["Average Math Score"]  = district_summary_df["Average Math Score"].map("{:.1f}".format)
district_summary_df["% Passing Reading"]  = district_summary_df["% Passing Reading"].map("{:.1f}".format)
district_summary_df["% Passing Math"]  = district_summary_df["% Passing Math"].map("{:.1f}".format)
district_summary_df["Overall Passing"]  = district_summary_df["Overall Passing"].map("{:.1f}".format)

district_summary_df
Total Schools	Total Students	Total Budget	Average Reading Score	Average Math Score	% Passing Reading	% Passing Math	Overall Passing
0	15	39,170	$24,649,428.00	81.9	79.0	85.8	75.0	65.2
# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students","Total Budget" ,
                    "Average Math Score", "Average Reading Score", 
                    "% Passing Math","% Passing Reading" , 
                   "Overall Passing"]
# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df
Total Schools	Total Students	Total Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	Overall Passing
0	15	39,170	$24,649,428.00	79.0	81.9	75.0	85.8	65.2
# The value_counts method counts unique values in a column
count = school_data_complete_df["school_name"].value_counts()
count
Bailey High School       4976
Johnson High School      4761
Hernandez High School    4635
Rodriguez High School    3999
Figueroa High School     2949
Huang High School        2917
Ford High School         2739
Wilson High School       2283
Cabrera High School      1858
Wright High School       1800
Shelton High School      1761
Thomas High School       1635
Griffin High School      1468
Pena High School          962
Holden High School        427
Name: school_name, dtype: int64
# Determine the school type
per_school_types_series = school_data_df.set_index(["school_name"])["type"]
per_school_types_series
school_name
Huang High School        District
Figueroa High School     District
Shelton High School       Charter
Hernandez High School    District
Griffin High School       Charter
Wilson High School        Charter
Cabrera High School       Charter
Bailey High School       District
Holden High School        Charter
Pena High School          Charter
Wright High School        Charter
Rodriguez High School    District
Johnson High School      District
Ford High School         District
Thomas High School        Charter
Name: type, dtype: object
# Add the per_school_types into a DataFrame for testing.
df = pd.DataFrame(per_school_types_series)
df
type
school_name	
Huang High School	District
Figueroa High School	District
Shelton High School	Charter
Hernandez High School	District
Griffin High School	Charter
Wilson High School	Charter
Cabrera High School	Charter
Bailey High School	District
Holden High School	Charter
Pena High School	Charter
Wright High School	Charter
Rodriguez High School	District
Johnson High School	District
Ford High School	District
Thomas High School	Charter
per_school_counts  = student_data_df["school_name"].value_counts()
per_school_counts 
Bailey High School       4976
Johnson High School      4761
Hernandez High School    4635
Rodriguez High School    3999
Figueroa High School     2949
Huang High School        2917
Ford High School         2739
Wilson High School       2283
Cabrera High School      1858
Wright High School       1800
Shelton High School      1761
Thomas High School       1635
Griffin High School      1468
Pena High School          962
Holden High School        427
Name: school_name, dtype: int64
# Calculate the total student count.
per_school_counts_series = school_data_df.set_index(["school_name"])["size"]
per_school_counts_series
school_name
Huang High School        2917
Figueroa High School     2949
Shelton High School      1761
Hernandez High School    4635
Griffin High School      1468
Wilson High School       2283
Cabrera High School      1858
Bailey High School       4976
Holden High School        427
Pena High School          962
Wright High School       1800
Rodriguez High School    3999
Johnson High School      4761
Ford High School         2739
Thomas High School       1635
Name: size, dtype: int64
# Calculate the total school budget.
per_school_budget_series = school_data_df.set_index(["school_name"])["budget"]
per_school_budget_series 
school_name
Huang High School        1910635
Figueroa High School     1884411
Shelton High School      1056600
Hernandez High School    3022020
Griffin High School       917500
Wilson High School       1319574
Cabrera High School      1081356
Bailey High School       3124928
Holden High School        248087
Pena High School          585858
Wright High School       1049400
Rodriguez High School    2547363
Johnson High School      3094650
Ford High School         1763916
Thomas High School       1043130
Name: budget, dtype: int64
# Calculate the per capita spending.
per_school_capita_series = per_school_budget_series/per_school_counts_series
per_school_capita_series
school_name
Huang High School        655.0
Figueroa High School     639.0
Shelton High School      600.0
Hernandez High School    652.0
Griffin High School      625.0
Wilson High School       578.0
Cabrera High School      582.0
Bailey High School       628.0
Holden High School       581.0
Pena High School         609.0
Wright High School       583.0
Rodriguez High School    637.0
Johnson High School      650.0
Ford High School         644.0
Thomas High School       638.0
dtype: float64
# Calculate the math scores.
student_school_math = student_data_df.set_index(["school_name"])["math_score"]
student_school_math
school_name
Huang High School     79
Huang High School     61
Huang High School     60
Huang High School     58
Huang High School     84
                      ..
Thomas High School    90
Thomas High School    70
Thomas High School    84
Thomas High School    90
Thomas High School    75
Name: math_score, Length: 39170, dtype: int64
#Calculate the average values for all numeric columns
per_school_averages_df = school_data_complete_df.groupby(["school_name"]).mean()
per_school_averages_df
Student ID	reading_score	math_score	School ID	size	budget
school_name						
Bailey High School	20358.5	81.033963	77.048432	7.0	4976.0	3124928.0
Cabrera High School	16941.5	83.975780	83.061895	6.0	1858.0	1081356.0
Figueroa High School	4391.0	81.158020	76.711767	1.0	2949.0	1884411.0
Ford High School	36165.0	80.746258	77.102592	13.0	2739.0	1763916.0
Griffin High School	12995.5	83.816757	83.351499	4.0	1468.0	917500.0
Hernandez High School	9944.0	80.934412	77.289752	3.0	4635.0	3022020.0
Holden High School	23060.0	83.814988	83.803279	8.0	427.0	248087.0
Huang High School	1458.0	81.182722	76.629414	0.0	2917.0	1910635.0
Johnson High School	32415.0	80.966394	77.072464	12.0	4761.0	3094650.0
Pena High School	23754.5	84.044699	83.839917	9.0	962.0	585858.0
Rodriguez High School	28035.0	80.744686	76.842711	11.0	3999.0	2547363.0
Shelton High School	6746.0	83.725724	83.359455	2.0	1761.0	1056600.0
Thomas High School	38352.0	83.848930	83.418349	14.0	1635.0	1043130.0
Wilson High School	14871.0	83.989488	83.274201	5.0	2283.0	1319574.0
Wright High School	25135.5	83.955000	83.682222	10.0	1800.0	1049400.0
#Calculate the average math score
per_school_math_averages_series = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
per_school_math_averages_series
school_name
Bailey High School       77.048432
Cabrera High School      83.061895
Figueroa High School     76.711767
Ford High School         77.102592
Griffin High School      83.351499
Hernandez High School    77.289752
Holden High School       83.803279
Huang High School        76.629414
Johnson High School      77.072464
Pena High School         83.839917
Rodriguez High School    76.842711
Shelton High School      83.359455
Thomas High School       83.418349
Wilson High School       83.274201
Wright High School       83.682222
Name: math_score, dtype: float64
#Calculate the average reading score
per_school_reading_averages_series = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]
per_school_reading_averages_series
school_name
Bailey High School       81.033963
Cabrera High School      83.975780
Figueroa High School     81.158020
Ford High School         80.746258
Griffin High School      83.816757
Hernandez High School    80.934412
Holden High School       83.814988
Huang High School        81.182722
Johnson High School      80.966394
Pena High School         84.044699
Rodriguez High School    80.744686
Shelton High School      83.725724
Thomas High School       83.848930
Wilson High School       83.989488
Wright High School       83.955000
Name: reading_score, dtype: float64
# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math_df = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_math_df
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
0	0	Paul Bradley	M	9th	Huang High School	66	79	0	District	2917	1910635
4	4	Bonnie Ray	F	9th	Huang High School	97	84	0	District	2917	1910635
5	5	Bryan Miranda	M	9th	Huang High School	94	94	0	District	2917	1910635
6	6	Sheena Carter	F	11th	Huang High School	82	80	0	District	2917	1910635
8	8	Michael Roth	M	10th	Huang High School	95	87	0	District	2917	1910635
...	...	...	...	...	...	...	...	...	...	...	...
39165	39165	Donna Howard	F	12th	Thomas High School	99	90	14	Charter	1635	1043130
39166	39166	Dawn Bell	F	10th	Thomas High School	95	70	14	Charter	1635	1043130
39167	39167	Rebecca Tanner	F	9th	Thomas High School	73	84	14	Charter	1635	1043130
39168	39168	Desiree Kidd	F	10th	Thomas High School	99	90	14	Charter	1635	1043130
39169	39169	Carolyn Jackson	F	11th	Thomas High School	95	75	14	Charter	1635	1043130
29370 rows × 11 columns

per_school_passing_reading_df = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
per_school_passing_reading_df
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
1	1	Victor Smith	M	12th	Huang High School	94	61	0	District	2917	1910635
2	2	Kevin Rodriguez	M	12th	Huang High School	90	60	0	District	2917	1910635
4	4	Bonnie Ray	F	9th	Huang High School	97	84	0	District	2917	1910635
5	5	Bryan Miranda	M	9th	Huang High School	94	94	0	District	2917	1910635
6	6	Sheena Carter	F	11th	Huang High School	82	80	0	District	2917	1910635
...	...	...	...	...	...	...	...	...	...	...	...
39165	39165	Donna Howard	F	12th	Thomas High School	99	90	14	Charter	1635	1043130
39166	39166	Dawn Bell	F	10th	Thomas High School	95	70	14	Charter	1635	1043130
39167	39167	Rebecca Tanner	F	9th	Thomas High School	73	84	14	Charter	1635	1043130
39168	39168	Desiree Kidd	F	10th	Thomas High School	99	90	14	Charter	1635	1043130
39169	39169	Carolyn Jackson	F	11th	Thomas High School	95	75	14	Charter	1635	1043130
33610 rows × 11 columns

per_school_passing_math_average_series  = per_school_passing_math_df.groupby(["school_name"]).mean()["math_score"]
per_school_passing_math_average_series
school_name
Bailey High School       84.505124
Cabrera High School      83.972556
Figueroa High School     84.310894
Ford High School         84.165687
Griffin High School      84.394602
Hernandez High School    84.936975
Holden High School       85.040506
Huang High School        84.240084
Johnson High School      84.742448
Pena High School         84.719780
Rodriguez High School    84.339111
Shelton High School      84.326679
Thomas High School       84.497705
Wilson High School       84.244050
Wright High School       84.758929
Name: math_score, dtype: float64
per_school_passing_reading_average_series  = per_school_passing_reading_df.groupby(["school_name"]).mean()["reading_score"]
per_school_passing_reading_average_series
school_name
Bailey High School       84.362521
Cabrera High School      84.432612
Figueroa High School     84.767745
Ford High School         84.612799
Griffin High School      84.253156
Hernandez High School    84.483725
Holden High School       84.391727
Huang High School        84.691400
Johnson High School      84.430566
Pena High School         84.680390
Rodriguez High School    84.374377
Shelton High School      84.362559
Thomas High School       84.259585
Wilson High School       84.526770
Wright High School       84.479586
Name: reading_score, dtype: float64
per_school_passing_math_count_series  = per_school_passing_math_df.groupby(["school_name"]).count()["student_name"]
per_school_passing_math_count_series
school_name
Bailey High School       3318
Cabrera High School      1749
Figueroa High School     1946
Ford High School         1871
Griffin High School      1371
Hernandez High School    3094
Holden High School        395
Huang High School        1916
Johnson High School      3145
Pena High School          910
Rodriguez High School    2654
Shelton High School      1653
Thomas High School       1525
Wilson High School       2143
Wright High School       1680
Name: student_name, dtype: int64
per_school_passing_reading_count_series  = per_school_passing_reading_df.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading_count_series
school_name
Bailey High School       4077
Cabrera High School      1803
Figueroa High School     2381
Ford High School         2172
Griffin High School      1426
Hernandez High School    3748
Holden High School        411
Huang High School        2372
Johnson High School      3867
Pena High School          923
Rodriguez High School    3208
Shelton High School      1688
Thomas High School       1591
Wilson High School       2204
Wright High School       1739
Name: student_name, dtype: int64
# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math_percentage_series = per_school_passing_math_count_series/per_school_counts_series * 100
per_school_passing_math_percentage_series
school_name
Bailey High School       66.680064
Cabrera High School      94.133477
Figueroa High School     65.988471
Ford High School         68.309602
Griffin High School      93.392371
Hernandez High School    66.752967
Holden High School       92.505855
Huang High School        65.683922
Johnson High School      66.057551
Pena High School         94.594595
Rodriguez High School    66.366592
Shelton High School      93.867121
Thomas High School       93.272171
Wilson High School       93.867718
Wright High School       93.333333
dtype: float64
per_school_passing_reading_percentage_series = per_school_passing_reading_count_series/per_school_counts_series * 100
per_school_passing_reading_percentage_series
school_name
Bailey High School       81.933280
Cabrera High School      97.039828
Figueroa High School     80.739234
Ford High School         79.299014
Griffin High School      97.138965
Hernandez High School    80.862999
Holden High School       96.252927
Huang High School        81.316421
Johnson High School      81.222432
Pena High School         95.945946
Rodriguez High School    80.220055
Shelton High School      95.854628
Thomas High School       97.308869
Wilson High School       96.539641
Wright High School       96.611111
dtype: float64
per_school_passing_math_reading_df = school_data_complete_df[(school_data_complete_df["math_score"] >=70)  & (school_data_complete_df["reading_score"] >=70)] 
per_school_passing_math_reading_df
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
4	4	Bonnie Ray	F	9th	Huang High School	97	84	0	District	2917	1910635
5	5	Bryan Miranda	M	9th	Huang High School	94	94	0	District	2917	1910635
6	6	Sheena Carter	F	11th	Huang High School	82	80	0	District	2917	1910635
8	8	Michael Roth	M	10th	Huang High School	95	87	0	District	2917	1910635
9	9	Matthew Greene	M	10th	Huang High School	96	84	0	District	2917	1910635
...	...	...	...	...	...	...	...	...	...	...	...
39165	39165	Donna Howard	F	12th	Thomas High School	99	90	14	Charter	1635	1043130
39166	39166	Dawn Bell	F	10th	Thomas High School	95	70	14	Charter	1635	1043130
39167	39167	Rebecca Tanner	F	9th	Thomas High School	73	84	14	Charter	1635	1043130
39168	39168	Desiree Kidd	F	10th	Thomas High School	99	90	14	Charter	1635	1043130
39169	39169	Carolyn Jackson	F	11th	Thomas High School	95	75	14	Charter	1635	1043130
25528 rows × 11 columns

per_school_passing_math_reading_series = per_school_passing_math_reading_df.groupby(["school_name"]).count()["student_name"]
per_school_passing_math_reading_series
school_name
Bailey High School       2719
Cabrera High School      1697
Figueroa High School     1569
Ford High School         1487
Griffin High School      1330
Hernandez High School    2481
Holden High School        381
Huang High School        1561
Johnson High School      2549
Pena High School          871
Rodriguez High School    2119
Shelton High School      1583
Thomas High School       1487
Wilson High School       2068
Wright High School       1626
Name: student_name, dtype: int64
per_school_overall_passing_percentage_series = per_school_passing_math_reading_series/per_school_counts_series * 100
per_school_overall_passing_percentage_series
school_name
Bailey High School       54.642283
Cabrera High School      91.334769
Figueroa High School     53.204476
Ford High School         54.289887
Griffin High School      90.599455
Hernandez High School    53.527508
Holden High School       89.227166
Huang High School        53.513884
Johnson High School      53.539172
Pena High School         90.540541
Rodriguez High School    52.988247
Shelton High School      89.892107
Thomas High School       90.948012
Wilson High School       90.582567
Wright High School       90.333333
dtype: float64
# Adding a list of values with keys to create a new DataFrame.
per_school_summary_df  = pd.DataFrame({
                        "School Type" : per_school_types_series,
                        "Total Students" : per_school_counts_series,
                        "Total School Budget" : per_school_budget_series,
                        "Per Student Budget" : per_school_capita_series,
                        "Average Math Score" : per_school_math_averages_series,
                        "Average Reading Score" : per_school_reading_averages_series,
                        "% Passing Math" : per_school_passing_math_percentage_series,
                        "% Passing Reading" : per_school_passing_reading_percentage_series,
                        "% Overall Passing" : per_school_overall_passing_percentage_series })
per_school_summary_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
school_name									
Bailey High School	District	4976	3124928	628.0	77.048432	81.033963	66.680064	81.933280	54.642283
Cabrera High School	Charter	1858	1081356	582.0	83.061895	83.975780	94.133477	97.039828	91.334769
Figueroa High School	District	2949	1884411	639.0	76.711767	81.158020	65.988471	80.739234	53.204476
Ford High School	District	2739	1763916	644.0	77.102592	80.746258	68.309602	79.299014	54.289887
Griffin High School	Charter	1468	917500	625.0	83.351499	83.816757	93.392371	97.138965	90.599455
Hernandez High School	District	4635	3022020	652.0	77.289752	80.934412	66.752967	80.862999	53.527508
Holden High School	Charter	427	248087	581.0	83.803279	83.814988	92.505855	96.252927	89.227166
Huang High School	District	2917	1910635	655.0	76.629414	81.182722	65.683922	81.316421	53.513884
Johnson High School	District	4761	3094650	650.0	77.072464	80.966394	66.057551	81.222432	53.539172
Pena High School	Charter	962	585858	609.0	83.839917	84.044699	94.594595	95.945946	90.540541
Rodriguez High School	District	3999	2547363	637.0	76.842711	80.744686	66.366592	80.220055	52.988247
Shelton High School	Charter	1761	1056600	600.0	83.359455	83.725724	93.867121	95.854628	89.892107
Thomas High School	Charter	1635	1043130	638.0	83.418349	83.848930	93.272171	97.308869	90.948012
Wilson High School	Charter	2283	1319574	578.0	83.274201	83.989488	93.867718	96.539641	90.582567
Wright High School	Charter	1800	1049400	583.0	83.682222	83.955000	93.333333	96.611111	90.333333
# Format the Total School Budget and the Per Student Budget columns.
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)
per_school_summary_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
school_name									
Bailey High School	District	4976	$3,124,928.00	$628.00	77.048432	81.033963	66.680064	81.933280	54.642283
Cabrera High School	Charter	1858	$1,081,356.00	$582.00	83.061895	83.975780	94.133477	97.039828	91.334769
Figueroa High School	District	2949	$1,884,411.00	$639.00	76.711767	81.158020	65.988471	80.739234	53.204476
Ford High School	District	2739	$1,763,916.00	$644.00	77.102592	80.746258	68.309602	79.299014	54.289887
Griffin High School	Charter	1468	$917,500.00	$625.00	83.351499	83.816757	93.392371	97.138965	90.599455
Hernandez High School	District	4635	$3,022,020.00	$652.00	77.289752	80.934412	66.752967	80.862999	53.527508
Holden High School	Charter	427	$248,087.00	$581.00	83.803279	83.814988	92.505855	96.252927	89.227166
Huang High School	District	2917	$1,910,635.00	$655.00	76.629414	81.182722	65.683922	81.316421	53.513884
Johnson High School	District	4761	$3,094,650.00	$650.00	77.072464	80.966394	66.057551	81.222432	53.539172
Pena High School	Charter	962	$585,858.00	$609.00	83.839917	84.044699	94.594595	95.945946	90.540541
Rodriguez High School	District	3999	$2,547,363.00	$637.00	76.842711	80.744686	66.366592	80.220055	52.988247
Shelton High School	Charter	1761	$1,056,600.00	$600.00	83.359455	83.725724	93.867121	95.854628	89.892107
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.418349	83.848930	93.272171	97.308869	90.948012
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333
# Sort and show top five schools.
top_schools_df = per_school_summary_df.sort_values(["% Overall Passing"], ascending = False)
top_schools_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
school_name									
Cabrera High School	Charter	1858	$1,081,356.00	$582.00	83.061895	83.975780	94.133477	97.039828	91.334769
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.418349	83.848930	93.272171	97.308869	90.948012
Griffin High School	Charter	1468	$917,500.00	$625.00	83.351499	83.816757	93.392371	97.138965	90.599455
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567
Pena High School	Charter	962	$585,858.00	$609.00	83.839917	84.044699	94.594595	95.945946	90.540541
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333
Shelton High School	Charter	1761	$1,056,600.00	$600.00	83.359455	83.725724	93.867121	95.854628	89.892107
Holden High School	Charter	427	$248,087.00	$581.00	83.803279	83.814988	92.505855	96.252927	89.227166
Bailey High School	District	4976	$3,124,928.00	$628.00	77.048432	81.033963	66.680064	81.933280	54.642283
Ford High School	District	2739	$1,763,916.00	$644.00	77.102592	80.746258	68.309602	79.299014	54.289887
Johnson High School	District	4761	$3,094,650.00	$650.00	77.072464	80.966394	66.057551	81.222432	53.539172
Hernandez High School	District	4635	$3,022,020.00	$652.00	77.289752	80.934412	66.752967	80.862999	53.527508
Huang High School	District	2917	$1,910,635.00	$655.00	76.629414	81.182722	65.683922	81.316421	53.513884
Figueroa High School	District	2949	$1,884,411.00	$639.00	76.711767	81.158020	65.988471	80.739234	53.204476
Rodriguez High School	District	3999	$2,547,363.00	$637.00	76.842711	80.744686	66.366592	80.220055	52.988247
# Sort and show bottom five schools.
bottom_schools_df = per_school_summary_df.sort_values(["% Overall Passing"], ascending = True)
bottom_schools_df.head()
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
school_name									
Rodriguez High School	District	3999	$2,547,363.00	$637.00	76.842711	80.744686	66.366592	80.220055	52.988247
Figueroa High School	District	2949	$1,884,411.00	$639.00	76.711767	81.158020	65.988471	80.739234	53.204476
Huang High School	District	2917	$1,910,635.00	$655.00	76.629414	81.182722	65.683922	81.316421	53.513884
Hernandez High School	District	4635	$3,022,020.00	$652.00	77.289752	80.934412	66.752967	80.862999	53.527508
Johnson High School	District	4761	$3,094,650.00	$650.00	77.072464	80.966394	66.057551	81.222432	53.539172
ninth_grades_df = school_data_complete_df[(school_data_complete_df["grade"] == "9th")]
tenth_grades_df = school_data_complete_df[(school_data_complete_df["grade"] == "10th")]
eleventh_grades_df = school_data_complete_df[(school_data_complete_df["grade"] == "11th")]
twelfth_grades_df = school_data_complete_df[(school_data_complete_df["grade"] == "12th")]
    ninth_grade_math_scores_series = ninth_grades_df.groupby(["school_name"]).mean() ["math_score"]
tenth_grade_math_scores_series = tenth_grades_df.groupby(["school_name"]).mean() ["math_score"]
eleventh_grade_math_scores_series = eleventh_grades_df.groupby(["school_name"]).mean() ["math_score"]
twelfth_grade_math_scores_series = twelfth_grades_df.groupby(["school_name"]).mean() ["math_score"]
eleventh_grade_math_scores_series
school_name
Bailey High School       77.515588
Cabrera High School      82.765560
Figueroa High School     76.884344
Ford High School         76.918058
Griffin High School      83.842105
Hernandez High School    77.136029
Holden High School       85.000000
Huang High School        76.446602
Johnson High School      77.491653
Pena High School         84.328125
Rodriguez High School    76.395626
Shelton High School      83.383495
Thomas High School       83.498795
Wilson High School       83.195326
Wright High School       83.836782
Name: math_score, dtype: float64
ninth_grade_reading_scores_series = ninth_grades_df.groupby(["school_name"]).mean() ["reading_score"]
tenth_grade_reading_scores_series = tenth_grades_df.groupby(["school_name"]).mean() ["reading_score"]
eleventh_grade_reading_scores_series = eleventh_grades_df.groupby(["school_name"]).mean() ["reading_score"]
twelfth_grade_reading_scores_series = twelfth_grades_df.groupby(["school_name"]).mean() ["reading_score"]
twelfth_grade_reading_scores_series
school_name
Bailey High School       80.912451
Cabrera High School      84.287958
Figueroa High School     81.384863
Ford High School         80.662338
Griffin High School      84.013699
Hernandez High School    80.857143
Holden High School       84.698795
Huang High School        80.305983
Johnson High School      81.227564
Pena High School         84.591160
Rodriguez High School    80.376426
Shelton High School      82.781671
Thomas High School       83.831361
Wilson High School       84.317673
Wright High School       84.073171
Name: reading_score, dtype: float64
# Combine each grade level Series for average math scores by school into a single DataFrame.
math_scores_by_grade_df = pd.DataFrame({
    "9th" : ninth_grade_math_scores_series,
     "10th" : tenth_grade_math_scores_series,
     "11th" : eleventh_grade_math_scores_series,
     "12th" : twelfth_grade_math_scores_series
})
math_scores_by_grade_df
9th	10th	11th	12th
school_name				
Bailey High School	77.083676	76.996772	77.515588	76.492218
Cabrera High School	83.094697	83.154506	82.765560	83.277487
Figueroa High School	76.403037	76.539974	76.884344	77.151369
Ford High School	77.361345	77.672316	76.918058	76.179963
Griffin High School	82.044010	84.229064	83.842105	83.356164
Hernandez High School	77.438495	77.337408	77.136029	77.186567
Holden High School	83.787402	83.429825	85.000000	82.855422
Huang High School	77.027251	75.908735	76.446602	77.225641
Johnson High School	77.187857	76.691117	77.491653	76.863248
Pena High School	83.625455	83.372000	84.328125	84.121547
Rodriguez High School	76.859966	76.612500	76.395626	77.690748
Shelton High School	83.420755	82.917411	83.383495	83.778976
Thomas High School	83.590022	83.087886	83.498795	83.497041
Wilson High School	83.085578	83.724422	83.195326	83.035794
Wright High School	83.264706	84.010288	83.836782	83.644986
# Combine each grade level Series for average reading scores by school into a single DataFrame.
reading_scores_by_grade_df = pd.DataFrame({
    "9th" : ninth_grade_reading_scores_series,
     "10th" : tenth_grade_reading_scores_series,
     "11th" : eleventh_grade_reading_scores_series,
     "12th" : twelfth_grade_reading_scores_series
})
reading_scores_by_grade_df
9th	10th	11th	12th
school_name				
Bailey High School	81.303155	80.907183	80.945643	80.912451
Cabrera High School	83.676136	84.253219	83.788382	84.287958
Figueroa High School	81.198598	81.408912	80.640339	81.384863
Ford High School	80.632653	81.262712	80.403642	80.662338
Griffin High School	83.369193	83.706897	84.288089	84.013699
Hernandez High School	80.866860	80.660147	81.396140	80.857143
Holden High School	83.677165	83.324561	83.815534	84.698795
Huang High School	81.290284	81.512386	81.417476	80.305983
Johnson High School	81.260714	80.773431	80.616027	81.227564
Pena High School	83.807273	83.612000	84.335938	84.591160
Rodriguez High School	80.993127	80.629808	80.864811	80.376426
Shelton High School	84.122642	83.441964	84.373786	82.781671
Thomas High School	83.728850	84.254157	83.585542	83.831361
Wilson High School	83.939778	84.021452	83.764608	84.317673
Wright High School	83.833333	83.812757	84.156322	84.073171
math_scores_by_grade_df["9th"] = math_scores_by_grade_df["9th"].map("{:.1f}".format)
math_scores_by_grade_df["10th"] = math_scores_by_grade_df["10th"].map("{:.1f}".format)
math_scores_by_grade_df["11th"] = math_scores_by_grade_df["11th"].map("{:.1f}".format)
math_scores_by_grade_df["12th"] = math_scores_by_grade_df["12th"].map("{:.1f}".format)
math_scores_by_grade_df
9th	10th	11th	12th
school_name				
Bailey High School	77.1	77.0	77.5	76.5
Cabrera High School	83.1	83.2	82.8	83.3
Figueroa High School	76.4	76.5	76.9	77.2
Ford High School	77.4	77.7	76.9	76.2
Griffin High School	82.0	84.2	83.8	83.4
Hernandez High School	77.4	77.3	77.1	77.2
Holden High School	83.8	83.4	85.0	82.9
Huang High School	77.0	75.9	76.4	77.2
Johnson High School	77.2	76.7	77.5	76.9
Pena High School	83.6	83.4	84.3	84.1
Rodriguez High School	76.9	76.6	76.4	77.7
Shelton High School	83.4	82.9	83.4	83.8
Thomas High School	83.6	83.1	83.5	83.5
Wilson High School	83.1	83.7	83.2	83.0
Wright High School	83.3	84.0	83.8	83.6
reading_scores_by_grade_df["9th"] = reading_scores_by_grade_df["9th"].map("{:.1f}".format)
reading_scores_by_grade_df["10th"] = reading_scores_by_grade_df["10th"].map("{:.1f}".format)
reading_scores_by_grade_df["11th"] = reading_scores_by_grade_df["11th"].map("{:.1f}".format)
reading_scores_by_grade_df["12th"] = reading_scores_by_grade_df["12th"].map("{:.1f}".format)
reading_scores_by_grade_df
9th	10th	11th	12th
school_name				
Bailey High School	81.3	80.9	80.9	80.9
Cabrera High School	83.7	84.3	83.8	84.3
Figueroa High School	81.2	81.4	80.6	81.4
Ford High School	80.6	81.3	80.4	80.7
Griffin High School	83.4	83.7	84.3	84.0
Hernandez High School	80.9	80.7	81.4	80.9
Holden High School	83.7	83.3	83.8	84.7
Huang High School	81.3	81.5	81.4	80.3
Johnson High School	81.3	80.8	80.6	81.2
Pena High School	83.8	83.6	84.3	84.6
Rodriguez High School	81.0	80.6	80.9	80.4
Shelton High School	84.1	83.4	84.4	82.8
Thomas High School	83.7	84.3	83.6	83.8
Wilson High School	83.9	84.0	83.8	84.3
Wright High School	83.8	83.8	84.2	84.1
# Remove the index name.
math_scores_by_grade_df.index.name = None
# Display the DataFrame.
math_scores_by_grade_df.head()
9th	10th	11th	12th
Bailey High School	77.1	77.0	77.5	76.5
Cabrera High School	83.1	83.2	82.8	83.3
Figueroa High School	76.4	76.5	76.9	77.2
Ford High School	77.4	77.7	76.9	76.2
Griffin High School	82.0	84.2	83.8	83.4
# Remove the index name.
reading_scores_by_grade_df.index.name = None
# Display the DataFrame.
reading_scores_by_grade_df.head()
9th	10th	11th	12th
Bailey High School	81.3	80.9	80.9	80.9
Cabrera High School	83.7	84.3	83.8	84.3
Figueroa High School	81.2	81.4	80.6	81.4
Ford High School	80.6	81.3	80.4	80.7
Griffin High School	83.4	83.7	84.3	84.0
# Get the descriptive statistics for the per_school_capita.
per_school_capita_series.describe()
count     15.000000
mean     620.066667
std       28.544368
min      578.000000
25%      591.500000
50%      628.000000
75%      641.500000
max      655.000000
dtype: float64
# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 615, 645, 675]
pd.cut(per_school_capita_series, spending_bins)
school_name
Huang High School        (645, 675]
Figueroa High School     (615, 645]
Shelton High School      (585, 615]
Hernandez High School    (645, 675]
Griffin High School      (615, 645]
Wilson High School         (0, 585]
Cabrera High School        (0, 585]
Bailey High School       (615, 645]
Holden High School         (0, 585]
Pena High School         (585, 615]
Wright High School         (0, 585]
Rodriguez High School    (615, 645]
Johnson High School      (645, 675]
Ford High School         (615, 645]
Thomas High School       (615, 645]
dtype: category
Categories (4, interval[int64, right]): [(0, 585] < (585, 615] < (615, 645] < (645, 675]]
# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 615, 645, 675]
per_school_capita_series.groupby(pd.cut(per_school_capita_series, spending_bins)).count()
(0, 585]      4
(585, 615]    2
(615, 645]    6
(645, 675]    3
dtype: int64
# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 630, 645, 675]
per_school_capita_series.groupby(pd.cut(per_school_capita_series, spending_bins)).count()
(0, 585]      4
(585, 630]    4
(630, 645]    4
(645, 675]    3
dtype: int64
# Establish the spending bins and group names.
spending_bins = [0, 585, 630, 645, 675]
group_names = ["<$584", "$585-629", "$630-644", "$645-675"]
# Categorize spending based on the bins.
per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita_series, spending_bins, labels=group_names)
per_school_summary_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing	Spending Ranges (Per Student)
school_name										
Bailey High School	District	4976	$3,124,928.00	$628.00	77.048432	81.033963	66.680064	81.933280	54.642283	$585-629
Cabrera High School	Charter	1858	$1,081,356.00	$582.00	83.061895	83.975780	94.133477	97.039828	91.334769	<$584
Figueroa High School	District	2949	$1,884,411.00	$639.00	76.711767	81.158020	65.988471	80.739234	53.204476	$630-644
Ford High School	District	2739	$1,763,916.00	$644.00	77.102592	80.746258	68.309602	79.299014	54.289887	$630-644
Griffin High School	Charter	1468	$917,500.00	$625.00	83.351499	83.816757	93.392371	97.138965	90.599455	$585-629
Hernandez High School	District	4635	$3,022,020.00	$652.00	77.289752	80.934412	66.752967	80.862999	53.527508	$645-675
Holden High School	Charter	427	$248,087.00	$581.00	83.803279	83.814988	92.505855	96.252927	89.227166	<$584
Huang High School	District	2917	$1,910,635.00	$655.00	76.629414	81.182722	65.683922	81.316421	53.513884	$645-675
Johnson High School	District	4761	$3,094,650.00	$650.00	77.072464	80.966394	66.057551	81.222432	53.539172	$645-675
Pena High School	Charter	962	$585,858.00	$609.00	83.839917	84.044699	94.594595	95.945946	90.540541	$585-629
Rodriguez High School	District	3999	$2,547,363.00	$637.00	76.842711	80.744686	66.366592	80.220055	52.988247	$630-644
Shelton High School	Charter	1761	$1,056,600.00	$600.00	83.359455	83.725724	93.867121	95.854628	89.892107	$585-629
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.418349	83.848930	93.272171	97.308869	90.948012	$630-644
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567	<$584
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333	<$584
# Calculate averages for the desired columns.
spending_math_average_scores_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["Average Math Score"]
spending_reading_average_scores_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["Average Reading Score"]
spending_passing_math_percentage_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["% Passing Math"]
spending_passing_reading_percentage_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["% Passing Reading"]
spending_overall_passing_percentage_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["% Overall Passing"]

spending_overall_passing_percentage_series
Spending Ranges (Per Student)
<$584       90.369459
$585-629    81.418596
$630-644    62.857656
$645-675    53.526855
Name: % Overall Passing, dtype: float64
spending_summary_df = pd.DataFrame({
    "Average Math Score" : spending_math_average_scores_series,
    "Average Reading Score" : spending_reading_average_scores_series,
    "% Passing Math" : spending_passing_math_percentage_series,
    "% Passing Reading" : spending_passing_reading_percentage_series,
    "% Overall Passing" : spending_overall_passing_percentage_series,
    
})
spending_summary_df
Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
Spending Ranges (Per Student)					
<$584	83.455399	83.933814	93.460096	96.610877	90.369459
$585-629	81.899826	83.155286	87.133538	92.718205	81.418596
$630-644	78.518855	81.624473	73.484209	84.391793	62.857656
$645-675	76.997210	81.027843	66.164813	81.133951	53.526855
spending_summary_df["Average Math Score"] = spending_summary_df["Average Math Score"].map("{:.1f}".format)
spending_summary_df["Average Reading Score"] = spending_summary_df["Average Reading Score"].map("{:.1f}".format)
spending_summary_df["% Passing Math"] = spending_summary_df["% Passing Math"].map("{:.0f}".format)
spending_summary_df["% Passing Reading"] = spending_summary_df["% Passing Reading"].map("{:.0f}".format)
spending_summary_df["% Overall Passing"] = spending_summary_df["% Overall Passing"].map("{:.0f}".format)
spending_summary_df
Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
Spending Ranges (Per Student)					
<$584	83.5	83.9	93	97	90
$585-629	81.9	83.2	87	93	81
$630-644	78.5	81.6	73	84	63
$645-675	77.0	81.0	66	81	54
# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

per_school_summary_df["School Size"] = pd.cut(per_school_counts_series, size_bins, labels=group_names)
per_school_summary_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing	Spending Ranges (Per Student)	School Size
school_name											
Bailey High School	District	4976	$3,124,928.00	$628.00	77.048432	81.033963	66.680064	81.933280	54.642283	$585-629	Large (2000-5000)
Cabrera High School	Charter	1858	$1,081,356.00	$582.00	83.061895	83.975780	94.133477	97.039828	91.334769	<$584	Medium (1000-2000)
Figueroa High School	District	2949	$1,884,411.00	$639.00	76.711767	81.158020	65.988471	80.739234	53.204476	$630-644	Large (2000-5000)
Ford High School	District	2739	$1,763,916.00	$644.00	77.102592	80.746258	68.309602	79.299014	54.289887	$630-644	Large (2000-5000)
Griffin High School	Charter	1468	$917,500.00	$625.00	83.351499	83.816757	93.392371	97.138965	90.599455	$585-629	Medium (1000-2000)
Hernandez High School	District	4635	$3,022,020.00	$652.00	77.289752	80.934412	66.752967	80.862999	53.527508	$645-675	Large (2000-5000)
Holden High School	Charter	427	$248,087.00	$581.00	83.803279	83.814988	92.505855	96.252927	89.227166	<$584	Small (<1000)
Huang High School	District	2917	$1,910,635.00	$655.00	76.629414	81.182722	65.683922	81.316421	53.513884	$645-675	Large (2000-5000)
Johnson High School	District	4761	$3,094,650.00	$650.00	77.072464	80.966394	66.057551	81.222432	53.539172	$645-675	Large (2000-5000)
Pena High School	Charter	962	$585,858.00	$609.00	83.839917	84.044699	94.594595	95.945946	90.540541	$585-629	Small (<1000)
Rodriguez High School	District	3999	$2,547,363.00	$637.00	76.842711	80.744686	66.366592	80.220055	52.988247	$630-644	Large (2000-5000)
Shelton High School	Charter	1761	$1,056,600.00	$600.00	83.359455	83.725724	93.867121	95.854628	89.892107	$585-629	Medium (1000-2000)
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.418349	83.848930	93.272171	97.308869	90.948012	$630-644	Medium (1000-2000)
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567	<$584	Large (2000-5000)
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333	<$584	Medium (1000-2000)
size_math_average_scores_series = per_school_summary_df.groupby("School Size").mean()["Average Math Score"]
size_reading_average_scores_series = per_school_summary_df.groupby("School Size").mean()["Average Reading Score"]
size_passing_math_percentage_series = per_school_summary_df.groupby("School Size").mean()["% Passing Math"]
size_passing_reading_percentage_series = per_school_summary_df.groupby("School Size").mean()["% Passing Reading"]
size_overall_passing_percentage_series = per_school_summary_df.groupby("School Size").mean()["% Overall Passing"]

size_overall_passing_percentage_series
School Size
Small (<1000)         89.883853
Medium (1000-2000)    90.621535
Large (2000-5000)     58.286003
Name: % Overall Passing, dtype: float64
size_summary_df = pd.DataFrame({
    "Average Math Score" : size_math_average_scores_series,
    "Average Reading Score" : size_reading_average_scores_series,
    "% Passing Math" : size_passing_math_percentage_series,
    "% Passing Reading" : size_passing_reading_percentage_series,
    "% Overall Passing" : size_overall_passing_percentage_series,
    
})
size_summary_df
Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
School Size					
Small (<1000)	83.821598	83.929843	93.550225	96.099437	89.883853
Medium (1000-2000)	83.374684	83.864438	93.599695	96.790680	90.621535
Large (2000-5000)	77.746417	81.344493	69.963361	82.766634	58.286003
size_summary_df["Average Math Score"] = size_summary_df["Average Math Score"].map("{:.1f}".format)
size_summary_df["Average Reading Score"] = size_summary_df["Average Reading Score"].map("{:.1f}".format)
size_summary_df["% Passing Math"] = size_summary_df["% Passing Math"].map("{:.0f}".format)
size_summary_df["% Passing Reading"] = size_summary_df["% Passing Reading"].map("{:.0f}".format)
size_summary_df["% Overall Passing"] = size_summary_df["% Overall Passing"].map("{:.0f}".format)
size_summary_df
Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
School Size					
Small (<1000)	83.8	83.9	94	96	90
Medium (1000-2000)	83.4	83.9	94	97	91
Large (2000-5000)	77.7	81.3	70	83	58
type_math_average_scores_series = per_school_summary_df.groupby("School Type").mean()["Average Math Score"]
type_reading_average_scores_series = per_school_summary_df.groupby("School Type").mean()["Average Reading Score"]
type_passing_math_percentage_series = per_school_summary_df.groupby("School Type").mean()["% Passing Math"]
type_passing_reading_percentage_series = per_school_summary_df.groupby("School Type").mean()["% Passing Reading"]
type_overall_passing_percentage_series = per_school_summary_df.groupby("School Type").mean()["% Overall Passing"]
type_overall_passing_percentage_series
School Type
Charter     90.432244
District    53.672208
Name: % Overall Passing, dtype: float64
type_summary_df = pd.DataFrame({
    "Average Math Score" : type_math_average_scores_series,
    "Average Reading Score" : type_reading_average_scores_series,
    "% Passing Math" : type_passing_math_percentage_series,
    "% Passing Reading" : type_passing_reading_percentage_series,
    "% Overall Passing" : type_overall_passing_percentage_series,
    
})
type_summary_df
Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
School Type					
Charter	83.473852	83.896421	93.620830	96.586489	90.432244
District	76.956733	80.966636	66.548453	80.799062	53.672208
type_summary_df["Average Math Score"] = type_summary_df["Average Math Score"].map("{:.1f}".format)
type_summary_df["Average Reading Score"] = type_summary_df["Average Reading Score"].map("{:.1f}".format)
type_summary_df["% Passing Math"] = type_summary_df["% Passing Math"].map("{:.0f}".format)
type_summary_df["% Passing Reading"] = type_summary_df["% Passing Reading"].map("{:.0f}".format)
type_summary_df["% Overall Passing"] = type_summary_df["% Overall Passing"].map("{:.0f}".format)
type_summary_df
Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
School Type					
Charter	83.5	83.9	94	97	90
District	77.0	81.0	67	81	54