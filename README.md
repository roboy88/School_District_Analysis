# School_District_Analysis
Using jupyter notebook within anaconda and python package I am analyzing standardized test scores in Marias school District.
The school board has notified Maria and her supervisor that the students_complete.csv file shows evidence of academic dishonesty; specifically, reading and math grades for Thomas High School ninth graders appear to have been altered. Although the school board does not know the full extent of the academic dishonesty, they want to uphold state-testing standards and have turned to Maria for help. She has asked you to replace the math and reading scores for Thomas High School with NaNs while keeping the rest of the data intact. Once you’ve replaced the math and reading scores, Maria would like you to repeat the school district analysis that you did in this module and write up a report to describe how these changes affected the overall analysis.
For this part of the Challenge, write a report that summarizes your updated analysis and compares it with the results from the module.

The analysis should contain the following:

Overview of the school district analysis: Explain the purpose of this analysis.
The purpose of this analysis was to help Maria seperate the wheat from the chaff regarding test scores and academic dishonesty specifically raing and math grades from Thoman High school ningth graders whose test scores appear to have been hack and altered much like the film war games staring Mathew Broderick. Once i went in a refactored code and replaced the math and reading scores Maria wanted me to report how these changes affected the overall analysis & I found that:
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

the average reading scores were good for a "B" average 90>="A", 80>="B",70>="C"

I also found that the average Math scores were good for "B" & "C" average with Thomas High school scoring; 83.1, 83.7, 83.1 and 83.0 respectivley. 
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
Results: Using bulleted lists and images of DataFrames as support, address the following questions.

How is the district summary affected?
How is the school summary affected?
How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools?
How does replacing the ninth-grade scores affect the following:
Math and reading scores by grade
Scores by school spending
Scores by school size
Scores by school type
Summary: Summarize four changes in the updated school district analysis after reading and math scores for the ninth grade at Thomas High School have been replaced with NaNs.
