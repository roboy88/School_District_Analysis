# Dependencies and Setup
import pandas as pd

# File to Load (Remember to change the path if needed.)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read the School Data and Student Data and store into a Pandas DataFrame
school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)

# Cleaning Student Names and Replacing Substrings in a Python String
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

# Check names.
student_data_df.head(10)
C:\Users\roman\AppData\Local\Temp/ipykernel_25376/3904321406.py:18: FutureWarning: The default value of regex will change from True to False in a future version.
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
Deliverable 1: Replace the reading and math scores.
Replace the 9th grade reading and math scores at Thomas High School with NaN.
# Install numpy using conda install numpy or pip install numpy. 
# Step 1. Import numpy as np.
import numpy as np
# Step 2. Use the loc method on the student_data_df to select all the reading scores from the 9th grade at Thomas High School and replace them with NaN.
student_data_df.loc[(student_data_df["grade"] == "9th") & (student_data_df["school_name"] == "Thomas High School"),["reading_score"]] = np.nan
#  Step 3. Refactor the code in Step 2 to replace the math scores with NaN.
student_data_df.loc[(student_data_df["grade"] == "9th") & (student_data_df["school_name"] == "Thomas High School"),["math_score"]] = np.nan
#  Step 4. Check the student data for NaN's. 
student_data_df.tail(10)
Student ID	student_name	gender	grade	school_name	reading_score	math_score
39160	39160	Katie Weaver	F	11th	Thomas High School	89.0	86.0
39161	39161	April Reyes	F	10th	Thomas High School	70.0	84.0
39162	39162	Derek Weeks	M	12th	Thomas High School	94.0	77.0
39163	39163	John Reese	M	11th	Thomas High School	90.0	75.0
39164	39164	Joseph Anthony	M	9th	Thomas High School	NaN	NaN
39165	39165	Donna Howard	F	12th	Thomas High School	99.0	90.0
39166	39166	Dawn Bell	F	10th	Thomas High School	95.0	70.0
39167	39167	Rebecca Tanner	F	9th	Thomas High School	NaN	NaN
39168	39168	Desiree Kidd	F	10th	Thomas High School	99.0	90.0
39169	39169	Carolyn Jackson	F	11th	Thomas High School	95.0	75.0
Deliverable 2 : Repeat the school district analysis
District Summary
# Combine the data into a single dataset
school_data_complete_df = pd.merge(student_data_df, school_data_df, how="left", on=["school_name", "school_name"])
school_data_complete_df.head()
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
0	0	Paul Bradley	M	9th	Huang High School	66.0	79.0	0	District	2917	1910635
1	1	Victor Smith	M	12th	Huang High School	94.0	61.0	0	District	2917	1910635
2	2	Kevin Rodriguez	M	12th	Huang High School	90.0	60.0	0	District	2917	1910635
3	3	Richard Scott	M	12th	Huang High School	67.0	58.0	0	District	2917	1910635
4	4	Bonnie Ray	F	9th	Huang High School	97.0	84.0	0	District	2917	1910635
# Calculate the Totals (Schools and Students)
school_count = len(school_data_complete_df["school_name"].unique())
student_count = school_data_complete_df["Student ID"].count()

# Calculate the Total Budget
total_budget = school_data_df["budget"].sum()
# Calculate the Average Scores using the "clean_student_data".
average_reading_score = school_data_complete_df["reading_score"].mean()
average_math_score = school_data_complete_df["math_score"].mean()
# Step 1. Get the number of students that are in ninth grade at Thomas High School.
# These students have no grades. 
stu_9th_thomas_count = student_data_df.loc[(student_data_df["grade"] == "9th") & (student_data_df["school_name"] == "Thomas High School")].count()["Student ID"]

# Get the total student count 
student_count = school_data_complete_df["Student ID"].count()

# Step 2. Subtract the number of students that are in ninth grade at 
# Thomas High School from the total student count to get the new total student count.
new_student_count = student_count - stu_9th_thomas_count
new_student_count
38709
# Calculate the passing rates using the "clean_student_data".
passing_math_count = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)].count()["student_name"]
passing_reading_count = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)].count()["student_name"]
# Step 3. Calculate the passing percentages with the new total student count.
passing_math_percentage =  passing_math_count/new_student_count * 100
passing_reading_percentage =  passing_reading_count/new_student_count * 100
# Calculate the students who passed both reading and math.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)
                                               & (school_data_complete_df["reading_score"] >= 70)]

# Calculate the number of students that passed both reading and math.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()


# Step 4.Calculate the overall passing percentage with new total student count.
overall_passing_percentage = overall_passing_math_reading_count/new_student_count * 100
# Create a DataFrame
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count, 
          "Total Students": student_count, 
          "Total Budget": total_budget,
          "Average Math Score": average_math_score, 
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])



# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
# Format the "Total Budget" to have the comma for a thousands separator, a decimal separator and a "$".
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)
district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)
district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.1f}".format)
district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.1f}".format)
district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.1f}".format)

# Display the data frame
district_summary_df
Total Schools	Total Students	Total Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
0	15	39,170	$24,649,428.00	78.9	81.9	74.8	85.7	64.9
School Summary
# Determine the School Type
per_school_types = school_data_df.set_index(["school_name"])["type"]

# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()

# Calculate the total school budget and per capita spending
per_school_budget = school_data_complete_df.groupby(["school_name"]).mean()["budget"]
# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts

# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]

# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]

# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]

# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100

# Calculate the students who passed both reading and math.
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)
                                               & (school_data_complete_df["math_score"] >= 70)]

# Calculate the number of students passing math and passing reading by school.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]

# Calculate the percentage of passing math and reading scores per school.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100
# Create the DataFrame
per_school_summary_df = pd.DataFrame({
    "School Type": per_school_types,
    "Total Students": per_school_counts,
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math,
    "Average Reading Score": per_school_reading,
    "% Passing Math": per_school_passing_math,
    "% Passing Reading": per_school_passing_reading,
    "% Overall Passing": per_overall_passing_percentage})


#per_school_summary_df
# Format the Total School Budget and the Per Student Budget
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)

# Display the data frame
per_school_summary_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
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
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.350937	83.896082	66.911315	69.663609	65.076453
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333
# Step 5.  Get the number of 10th-12th graders from Thomas High School (THS).
student_ths_101112_count = school_data_complete_df.loc[(school_data_complete_df["grade"] != "9th") & (school_data_complete_df["school_name"] == "Thomas High School")].count()["Student ID"]
# Step 6. Get all the students passing math from THS
ths_passing_math_df = school_data_complete_df.loc[(school_data_complete_df["school_name"] == "Thomas High School") & (school_data_complete_df["math_score"] >= 70)]
ths_passing_math_df
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
37535	37535	Norma Mata	F	10th	Thomas High School	76.0	76.0	14	Charter	1635	1043130
37536	37536	Cody Miller	M	11th	Thomas High School	84.0	82.0	14	Charter	1635	1043130
37541	37541	Eric Stevens	M	10th	Thomas High School	80.0	76.0	14	Charter	1635	1043130
37542	37542	Elizabeth Bennett	F	11th	Thomas High School	91.0	94.0	14	Charter	1635	1043130
37544	37544	Jacqueline Harris	F	10th	Thomas High School	71.0	92.0	14	Charter	1635	1043130
...	...	...	...	...	...	...	...	...	...	...	...
39163	39163	John Reese	M	11th	Thomas High School	90.0	75.0	14	Charter	1635	1043130
39165	39165	Donna Howard	F	12th	Thomas High School	99.0	90.0	14	Charter	1635	1043130
39166	39166	Dawn Bell	F	10th	Thomas High School	95.0	70.0	14	Charter	1635	1043130
39168	39168	Desiree Kidd	F	10th	Thomas High School	99.0	90.0	14	Charter	1635	1043130
39169	39169	Carolyn Jackson	F	11th	Thomas High School	95.0	75.0	14	Charter	1635	1043130
1094 rows ?? 11 columns

# Step 7. Get all the students passing reading from THS
ths_passing_reading_df = school_data_complete_df.loc[(school_data_complete_df["school_name"] == "Thomas High School") & (school_data_complete_df["reading_score"] >= 70)]
ths_passing_reading_df
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
37535	37535	Norma Mata	F	10th	Thomas High School	76.0	76.0	14	Charter	1635	1043130
37536	37536	Cody Miller	M	11th	Thomas High School	84.0	82.0	14	Charter	1635	1043130
37541	37541	Eric Stevens	M	10th	Thomas High School	80.0	76.0	14	Charter	1635	1043130
37542	37542	Elizabeth Bennett	F	11th	Thomas High School	91.0	94.0	14	Charter	1635	1043130
37544	37544	Jacqueline Harris	F	10th	Thomas High School	71.0	92.0	14	Charter	1635	1043130
...	...	...	...	...	...	...	...	...	...	...	...
39163	39163	John Reese	M	11th	Thomas High School	90.0	75.0	14	Charter	1635	1043130
39165	39165	Donna Howard	F	12th	Thomas High School	99.0	90.0	14	Charter	1635	1043130
39166	39166	Dawn Bell	F	10th	Thomas High School	95.0	70.0	14	Charter	1635	1043130
39168	39168	Desiree Kidd	F	10th	Thomas High School	99.0	90.0	14	Charter	1635	1043130
39169	39169	Carolyn Jackson	F	11th	Thomas High School	95.0	75.0	14	Charter	1635	1043130
1139 rows ?? 11 columns

# Step 8. Get all the students passing math and reading from THS

ths_passing_math_reading_df =  school_data_complete_df.loc[(school_data_complete_df["school_name"] == "Thomas High School") & (school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
ths_passing_math_reading_df
Student ID	student_name	gender	grade	school_name	reading_score	math_score	School ID	type	size	budget
37535	37535	Norma Mata	F	10th	Thomas High School	76.0	76.0	14	Charter	1635	1043130
37536	37536	Cody Miller	M	11th	Thomas High School	84.0	82.0	14	Charter	1635	1043130
37541	37541	Eric Stevens	M	10th	Thomas High School	80.0	76.0	14	Charter	1635	1043130
37542	37542	Elizabeth Bennett	F	11th	Thomas High School	91.0	94.0	14	Charter	1635	1043130
37544	37544	Jacqueline Harris	F	10th	Thomas High School	71.0	92.0	14	Charter	1635	1043130
...	...	...	...	...	...	...	...	...	...	...	...
39163	39163	John Reese	M	11th	Thomas High School	90.0	75.0	14	Charter	1635	1043130
39165	39165	Donna Howard	F	12th	Thomas High School	99.0	90.0	14	Charter	1635	1043130
39166	39166	Dawn Bell	F	10th	Thomas High School	95.0	70.0	14	Charter	1635	1043130
39168	39168	Desiree Kidd	F	10th	Thomas High School	99.0	90.0	14	Charter	1635	1043130
39169	39169	Carolyn Jackson	F	11th	Thomas High School	95.0	75.0	14	Charter	1635	1043130
1064 rows ?? 11 columns

# Step 9. Calculate the percentage of 10th-12th grade students passing math from Thomas High School. 
ths_passing_math_count = ths_passing_math_df["Student ID"].count()
ths_passing_math_percentage = ths_passing_math_count /student_ths_101112_count * 100
# Step 10. Calculate the percentage of 10th-12th grade students passing reading from Thomas High School.
ths_passing_reading_count = ths_passing_reading_df["Student ID"].count()
ths_passing_reading_percentage = ths_passing_reading_count /student_ths_101112_count * 100
# Step 11. Calculate the overall passing percentage of 10th-12th grade from Thomas High School. 
ths_overall_passing_count = ths_passing_math_reading_df["Student ID"].count()
ths_overall_passing_percentage = ths_overall_passing_count /student_ths_101112_count * 100
# Step 12. Replace the passing math percent for Thomas High School in the per_school_summary_df.
per_school_summary_df.loc["Thomas High School","% Passing Math"]= ths_passing_math_percentage
# Step 13. Replace the passing reading percentage for Thomas High School in the per_school_summary_df.
per_school_summary_df.loc["Thomas High School","% Passing Reading"]= ths_passing_reading_percentage
# Step 14. Replace the overall passing percentage for Thomas High School in the per_school_summary_df.
per_school_summary_df.loc["Thomas High School","% Overall Passing"]= ths_overall_passing_percentage
per_school_summary_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
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
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.350937	83.896082	93.185690	97.018739	90.630324
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333
High and Low Performing Schools
# Sort and show top five schools.
per_school_summary_df.sort_values(["% Overall Passing"], ascending = False)
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
Cabrera High School	Charter	1858	$1,081,356.00	$582.00	83.061895	83.975780	94.133477	97.039828	91.334769
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.350937	83.896082	93.185690	97.018739	90.630324
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
# Sort and show top five schools.
per_school_summary_df.sort_values(["% Overall Passing"], ascending = True)
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing
Rodriguez High School	District	3999	$2,547,363.00	$637.00	76.842711	80.744686	66.366592	80.220055	52.988247
Figueroa High School	District	2949	$1,884,411.00	$639.00	76.711767	81.158020	65.988471	80.739234	53.204476
Huang High School	District	2917	$1,910,635.00	$655.00	76.629414	81.182722	65.683922	81.316421	53.513884
Hernandez High School	District	4635	$3,022,020.00	$652.00	77.289752	80.934412	66.752967	80.862999	53.527508
Johnson High School	District	4761	$3,094,650.00	$650.00	77.072464	80.966394	66.057551	81.222432	53.539172
Ford High School	District	2739	$1,763,916.00	$644.00	77.102592	80.746258	68.309602	79.299014	54.289887
Bailey High School	District	4976	$3,124,928.00	$628.00	77.048432	81.033963	66.680064	81.933280	54.642283
Holden High School	Charter	427	$248,087.00	$581.00	83.803279	83.814988	92.505855	96.252927	89.227166
Shelton High School	Charter	1761	$1,056,600.00	$600.00	83.359455	83.725724	93.867121	95.854628	89.892107
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333
Pena High School	Charter	962	$585,858.00	$609.00	83.839917	84.044699	94.594595	95.945946	90.540541
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567
Griffin High School	Charter	1468	$917,500.00	$625.00	83.351499	83.816757	93.392371	97.138965	90.599455
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.350937	83.896082	93.185690	97.018739	90.630324
Cabrera High School	Charter	1858	$1,081,356.00	$582.00	83.061895	83.975780	94.133477	97.039828	91.334769
Math and Reading Scores by Grade
# Create a Series of scores by grade levels using conditionals.
# Group each school Series by the school name for the average math score.

ninth_grade_average_math_scores_series = school_data_complete_df.loc[(school_data_complete_df["grade"] == "9th")].groupby(["school_name"]).mean() ["math_score"]
tenth_grade_average_math_scores_series = school_data_complete_df.loc[(school_data_complete_df["grade"] == "10th")].groupby(["school_name"]).mean() ["math_score"]
eleventh_grade_average_math_scores_series = school_data_complete_df.loc[(school_data_complete_df["grade"] == "11th")].groupby(["school_name"]).mean() ["math_score"]
twelfth_grade_average_math_scores_series = school_data_complete_df.loc[(school_data_complete_df["grade"] == "12th")].groupby(["school_name"]).mean() ["math_score"]

# Group each school Series by the school name for the average reading score.
ninth_grade_average_reading_scores_series = school_data_complete_df.loc[(school_data_complete_df["grade"] == "9th")].groupby(["school_name"]).mean() ["reading_score"]
tenth_grade_average_reading_scores_series = school_data_complete_df.loc[(school_data_complete_df["grade"] == "10th")].groupby(["school_name"]).mean() ["reading_score"]
eleventh_grade_average_reading_scores_series = school_data_complete_df.loc[(school_data_complete_df["grade"] == "11th")].groupby(["school_name"]).mean() ["reading_score"]
twelfth_grade_average_reading_scores_series = school_data_complete_df.loc[(school_data_complete_df["grade"] == "12th")].groupby(["school_name"]).mean() ["reading_score"]
# Combine each Series for average math scores by school into single data frame.
average_math_scores_by_grade_df = pd.DataFrame({
    "9th" : ninth_grade_average_math_scores_series,
     "10th" : tenth_grade_average_math_scores_series,
     "11th" : eleventh_grade_average_math_scores_series,
     "12th" : twelfth_grade_average_math_scores_series
})
# Combine each Series for average reading scores by school into single data frame.
average_reading_scores_by_grade_df = pd.DataFrame({
    "9th" : ninth_grade_average_reading_scores_series,
     "10th" : tenth_grade_average_reading_scores_series,
     "11th" : eleventh_grade_average_reading_scores_series,
     "12th" : twelfth_grade_average_reading_scores_series
})
# Format each grade column.
average_math_scores_by_grade_df["9th"] = average_math_scores_by_grade_df["9th"].map("{:.1f}".format)
average_math_scores_by_grade_df["10th"] = average_math_scores_by_grade_df["10th"].map("{:.1f}".format)
average_math_scores_by_grade_df["11th"] = average_math_scores_by_grade_df["11th"].map("{:.1f}".format)
average_math_scores_by_grade_df["12th"] = average_math_scores_by_grade_df["12th"].map("{:.1f}".format)

average_reading_scores_by_grade_df["9th"] = average_reading_scores_by_grade_df["9th"].map("{:.1f}".format)
average_reading_scores_by_grade_df["10th"] = average_reading_scores_by_grade_df["10th"].map("{:.1f}".format)
average_reading_scores_by_grade_df["11th"] = average_reading_scores_by_grade_df["11th"].map("{:.1f}".format)
average_reading_scores_by_grade_df["12th"] = average_reading_scores_by_grade_df["12th"].map("{:.1f}".format)
# Remove the index.
average_math_scores_by_grade_df.reset_index(inplace=True)

# Display the data frame
average_math_scores_by_grade_df
school_name	9th	10th	11th	12th
0	Bailey High School	77.1	77.0	77.5	76.5
1	Cabrera High School	83.1	83.2	82.8	83.3
2	Figueroa High School	76.4	76.5	76.9	77.2
3	Ford High School	77.4	77.7	76.9	76.2
4	Griffin High School	82.0	84.2	83.8	83.4
5	Hernandez High School	77.4	77.3	77.1	77.2
6	Holden High School	83.8	83.4	85.0	82.9
7	Huang High School	77.0	75.9	76.4	77.2
8	Johnson High School	77.2	76.7	77.5	76.9
9	Pena High School	83.6	83.4	84.3	84.1
10	Rodriguez High School	76.9	76.6	76.4	77.7
11	Shelton High School	83.4	82.9	83.4	83.8
12	Thomas High School	nan	83.1	83.5	83.5
13	Wilson High School	83.1	83.7	83.2	83.0
14	Wright High School	83.3	84.0	83.8	83.6
## Remove the index.
average_reading_scores_by_grade_df.reset_index(inplace=True)
# Display the data frame
average_reading_scores_by_grade_df
school_name	9th	10th	11th	12th
0	Bailey High School	81.3	80.9	80.9	80.9
1	Cabrera High School	83.7	84.3	83.8	84.3
2	Figueroa High School	81.2	81.4	80.6	81.4
3	Ford High School	80.6	81.3	80.4	80.7
4	Griffin High School	83.4	83.7	84.3	84.0
5	Hernandez High School	80.9	80.7	81.4	80.9
6	Holden High School	83.7	83.3	83.8	84.7
7	Huang High School	81.3	81.5	81.4	80.3
8	Johnson High School	81.3	80.8	80.6	81.2
9	Pena High School	83.8	83.6	84.3	84.6
10	Rodriguez High School	81.0	80.6	80.9	80.4
11	Shelton High School	84.1	83.4	84.4	82.8
12	Thomas High School	nan	84.3	83.6	83.8
13	Wilson High School	83.9	84.0	83.8	84.3
14	Wright High School	83.8	83.8	84.2	84.1
Scores by School Spending
# Establish the spending bins and group names.
spending_bins = [0, 585, 630, 645, 675]
group_names = ["<$584", "$585-629", "$630-644", "$645-675"]

# Categorize spending based on the bins.
per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels=group_names)
per_school_summary_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing	Spending Ranges (Per Student)
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
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.350937	83.896082	93.185690	97.018739	90.630324	$630-644
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567	<$584
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333	<$584
# Calculate averages for the desired columns. 
spending_math_average_scores_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["Average Math Score"]
spending_reading_average_scores_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["Average Reading Score"]
spending_passing_math_percentage_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["% Passing Math"]
spending_passing_reading_percentage_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["% Passing Reading"]
spending_overall_passing_percentage_series = per_school_summary_df.groupby("Spending Ranges (Per Student)").mean()["% Overall Passing"]
# Create the DataFrame
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
$630-644	78.502002	81.636261	73.462589	84.319261	62.778233
$645-675	76.997210	81.027843	66.164813	81.133951	53.526855
# Format the DataFrame 
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
Scores by School Size
# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
# Categorize spending based on the bins.
per_school_summary_df["School Size"] = pd.cut(per_school_counts, size_bins, labels=group_names)

per_school_summary_df
School Type	Total Students	Total School Budget	Per Student Budget	Average Math Score	Average Reading Score	% Passing Math	% Passing Reading	% Overall Passing	Spending Ranges (Per Student)	School Size
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
Thomas High School	Charter	1635	$1,043,130.00	$638.00	83.350937	83.896082	93.185690	97.018739	90.630324	$630-644	Medium (1000-2000)
Wilson High School	Charter	2283	$1,319,574.00	$578.00	83.274201	83.989488	93.867718	96.539641	90.582567	<$584	Large (2000-5000)
Wright High School	Charter	1800	$1,049,400.00	$583.00	83.682222	83.955000	93.333333	96.611111	90.333333	<$584	Medium (1000-2000)
# Calculate averages for the desired columns. 
size_math_average_scores_series = per_school_summary_df.groupby("School Size").mean()["Average Math Score"]
size_reading_average_scores_series = per_school_summary_df.groupby("School Size").mean()["Average Reading Score"]
size_passing_math_percentage_series = per_school_summary_df.groupby("School Size").mean()["% Passing Math"]
size_passing_reading_percentage_series = per_school_summary_df.groupby("School Size").mean()["% Passing Reading"]
size_overall_passing_percentage_series = per_school_summary_df.groupby("School Size").mean()["% Overall Passing"]
# Assemble into DataFrame. 
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
Medium (1000-2000)	83.361201	83.873869	93.582398	96.732654	90.557997
Large (2000-5000)	77.746417	81.344493	69.963361	82.766634	58.286003
# Format the DataFrame  
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
Scores by School Type
# Calculate averages for the desired columns. 
type_math_average_scores_series = per_school_summary_df.groupby("School Type").mean()["Average Math Score"]
type_reading_average_scores_series = per_school_summary_df.groupby("School Type").mean()["Average Reading Score"]
type_passing_math_percentage_series = per_school_summary_df.groupby("School Type").mean()["% Passing Math"]
type_passing_reading_percentage_series = per_school_summary_df.groupby("School Type").mean()["% Passing Reading"]
type_overall_passing_percentage_series = per_school_summary_df.groupby("School Type").mean()["% Overall Passing"]
# Assemble into DataFrame. 
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
Charter	83.465425	83.902315	93.610020	96.550223	90.392533
District	76.956733	80.966636	66.548453	80.799062	53.672208
# # Format the DataFrame 
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