# List of high schools
high_schools = ["Huang High School",  "Figueroa High School", "Shelton High School", "Hernandez High School","Griffin High School","Wilson High School", "Cabrera High School", "Bailey High School", "Holden High School", "Pena High School", "Wright High School","Rodriguez High School", "Johnson High School", "Ford High School", "Thomas High School"]
# Add the Pandas dependency.
import pandas as pd
school_series = pd.Series(high_schools)
school_series
0         Huang High School
1      Figueroa High School
2       Shelton High School
3     Hernandez High School
4       Griffin High School
5        Wilson High School
6       Cabrera High School
7        Bailey High School
8        Holden High School
9          Pena High School
10       Wright High School
11    Rodriguez High School
12      Johnson High School
13         Ford High School
14       Thomas High School
dtype: object
for school in school_series:
    print(school)
Huang High School
Figueroa High School
Shelton High School
Hernandez High School
Griffin High School
Wilson High School
Cabrera High School
Bailey High School
Holden High School
Pena High School
Wright High School
Rodriguez High School
Johnson High School
Ford High School
Thomas High School
# A dictionary of high schools
high_school_dicts = [{"School ID": 0, "school_name": "Huang High    School", "type": "District"},
                   {"School ID": 1, "school_name": "Figueroa High School", "type": "District"},
                    {"School ID": 2, "school_name":"Shelton High School", "type": "Charter"},
                    {"School ID": 3, "school_name":"Hernandez High School", "type": "District"},
                    {"School ID": 4, "school_name":"Griffin High School", "type": "Charter"}]
school_df = pd.DataFrame(high_school_dicts)
school_df
School ID	school_name	type
0	0	Huang High School	District
1	1	Figueroa High School	District
2	2	Shelton High School	Charter
3	3	Hernandez High School	District
4	4	Griffin High School	Charter
# Three separate lists of information on high schools
school_id = [0, 1, 2, 3, 4]
school_name = ["Huang High School", "Figueroa High School",
"Shelton High School", "Hernandez High School","Griffin High School"]
type_of_school = ["District", "District", "Charter", "District","Charter"]
# Initialize a new DataFrame.
schools_df = pd.DataFrame()
schools_df["School ID"] = school_id
school_df["school_name"] = school_name
school_df["type"] = type_of_school
school_df
School ID	school_name	type
0	0	Huang High School	District
1	1	Figueroa High School	District
2	2	Shelton High School	Charter
3	3	Hernandez High School	District
4	4	Griffin High School	Charter
# Create a dictionary of informaion on schools
high_school_dict = {"School ID" : school_id, "school_name" : school_name, "type" : type_of_school}
high_school_dict
{'School ID': [0, 1, 2, 3, 4],
 'school_name': ['Huang High School',
  'Figueroa High School',
  'Shelton High School',
  'Hernandez High School',
  'Griffin High School'],
 'type': ['District', 'District', 'Charter', 'District', 'Charter']}
school_df =pd.DataFrame(high_school_dict)
school_df
School ID	school_name	type
0	0	Huang High School	District
1	1	Figueroa High School	District
2	2	Shelton High School	Charter
3	3	Hernandez High School	District
4	4	Griffin High School	Charter
school_df.columns
Index(['School ID', 'school_name', 'type'], dtype='object')
school_df.index
RangeIndex(start=0, stop=5, step=1)
school_df.values
array([[0, 'Huang High School', 'District'],
       [1, 'Figueroa High School', 'District'],
       [2, 'Shelton High School', 'Charter'],
       [3, 'Hernandez High School', 'District'],
       [4, 'Griffin High School', 'Charter']], dtype=object)
school_id = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
school_name =  ["Huang High School", "Figueroa High School", "Shelton High School", "Hernandez High School", 
                "Griffin High School", "Wilson High School", "Cabrera High School", "Bailey High School",
               "Holden High School", "Pena High School", "Wright High School", "Rodriguez High School",
               "Johnson High School", "Ford High School","Thamos High School"]
type_of_school = ["District", "District", "Charter", "District",
                  "Charter","Charter","Charter","District",
                  "Charter","Charter","Charter","District",
                 "District","District","Charter"]
school_df["School ID"] = school_id
school_df["school_name"] = school_name
school_df["type"] = type_of_school
school_df
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_11116/136150032.py in <module>
----> 1 school_df["School ID"] = school_id
      2 school_df["school_name"] = school_name
      3 school_df["type"] = type_of_school
      4 school_df

~\anaconda3\envs\PythonData\lib\site-packages\pandas\core\frame.py in __setitem__(self, key, value)
   3653         else:
   3654             # set column
-> 3655             self._set_item(key, value)
   3656 
   3657     def _setitem_slice(self, key: slice, value):

~\anaconda3\envs\PythonData\lib\site-packages\pandas\core\frame.py in _set_item(self, key, value)
   3830         ensure homogeneity.
   3831         """
-> 3832         value = self._sanitize_column(value)
   3833 
   3834         if (

~\anaconda3\envs\PythonData\lib\site-packages\pandas\core\frame.py in _sanitize_column(self, value)
   4527 
   4528         if is_list_like(value):
-> 4529             com.require_length_match(value, self.index)
   4530         return sanitize_array(value, self.index, copy=True, allow_2d=True)
   4531 

~\anaconda3\envs\PythonData\lib\site-packages\pandas\core\common.py in require_length_match(data, index)
    555     """
    556     if len(data) != len(index):
--> 557         raise ValueError(
    558             "Length of values "
    559             f"({len(data)}) "

ValueError: Length of values (15) does not match length of index (5)
new_school_id = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
new_school_name =  ["Huang High School", "Figueroa High School", "Shelton High School", "Hernandez High School", 
                "Griffin High School", "Wilson High School", "Cabrera High School", "Bailey High School",
               "Holden High School", "Pena High School", "Wright High School", "Rodriguez High School",
               "Johnson High School", "Ford High School","Thamos High School"]
new_type_of_school = ["District", "District", "Charter", "District",
                  "Charter","Charter","Charter","District",
                  "Charter","Charter","Charter","District",
                 "District","District","Charter"]
school_df["School ID"] = new_school_id
school_df["school_name"] = new_school_name
school_df["type"] = new_type_of_school
school_df
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_11116/2526744413.py in <module>
----> 1 school_df["School ID"] = new_school_id
      2 school_df["school_name"] = new_school_name
      3 school_df["type"] = new_type_of_school
      4 school_df

~\anaconda3\envs\PythonData\lib\site-packages\pandas\core\frame.py in __setitem__(self, key, value)
   3653         else:
   3654             # set column
-> 3655             self._set_item(key, value)
   3656 
   3657     def _setitem_slice(self, key: slice, value):

~\anaconda3\envs\PythonData\lib\site-packages\pandas\core\frame.py in _set_item(self, key, value)
   3830         ensure homogeneity.
   3831         """
-> 3832         value = self._sanitize_column(value)
   3833 
   3834         if (

~\anaconda3\envs\PythonData\lib\site-packages\pandas\core\frame.py in _sanitize_column(self, value)
   4527 
   4528         if is_list_like(value):
-> 4529             com.require_length_match(value, self.index)
   4530         return sanitize_array(value, self.index, copy=True, allow_2d=True)
   4531 

~\anaconda3\envs\PythonData\lib\site-packages\pandas\core\common.py in require_length_match(data, index)
    555     """
    556     if len(data) != len(index):
--> 557         raise ValueError(
    558             "Length of values "
    559             f"({len(data)}) "

ValueError: Length of values (15) does not match length of index (5)
new_schools_df = pd.DataFrame()
new_schools_df["School ID"] = new_school_id
new_schools_df["school_name"] = new_school_name
new_schools_df["type"] = new_type_of_school
new_schools_df
School ID	school_name	type
0	0	Huang High School	District
1	1	Figueroa High School	District
2	2	Shelton High School	Charter
3	3	Hernandez High School	District
4	4	Griffin High School	Charter
5	5	Wilson High School	Charter
6	6	Cabrera High School	Charter
7	7	Bailey High School	District
8	8	Holden High School	Charter
9	9	Pena High School	Charter
10	10	Wright High School	Charter
11	11	Rodriguez High School	District
12	12	Johnson High School	District
13	13	Ford High School	District
14	14	Thamos High School	Charter
class Dog:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound
    
    def bark(self):
        print(f"{self.sound} {self.sound}")
        
first_dog = Dog("Blacky", "Black", "Bow")

first_dog.bark()


    
Bow Bow