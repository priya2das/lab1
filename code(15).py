import pandas as pd

file_name = "weather.csv"
df = pd.read_csv(file_name)


# Q. 1)  Find all the unique 'Wind Speed' values in the data.
unique_wind_speed = df['Wind Speed_km/h'].unique()
print(" Q. 1)",unique_wind_speed)

# Q. 2) Find the number of times when the 'Weather is exactly Clear'.
clear_weather_count = df[df['Weather'] == 'Clear'].shape[0]
print("Q. 2)", clear_weather_count)

# Q3: Find the number of times when the 'Wind Speed was exactly 4 km/h'.
wind_speed_4_count = df[df['Wind Speed_km/h'] == 4].shape[0]
print("Q. 3)", wind_speed_4_count)

# Q4: Find out all the Null Values in the data.
null_values = df.isnull().sum()
print("Q. 4)", null_values)

# # Q5: Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
df.rename(columns={'Weather': 'Weather Condition'}, inplace=True)
print("Q. 5)", df.columns) 

# Q6: What is the mean 'Visibility'?
mean_visibility = df['Visibility_km'].mean()
print("Q. 6)", mean_visibility)

# Q7: What is the Standard Deviation of 'Pressure' in this data?
pressure_std = df['Press_kPa'].std()
print("Q. 7)", pressure_std)

# Q8: What is the Variance of 'Relative Humidity' in this data?
humidity_variance = df['Rel Hum_%'].var()
print("Q. 8)", humidity_variance)

# Q9: Find all instances when 'Snow' was recorded.
snow_instances = df[df['Weather Condition'].str.contains('Snow')]
print("Q. 9)", snow_instances)

# Q10: Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.
wind_vis_instances = df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)]
print("Q. 10)", wind_vis_instances)

# Q11: What is the Mean value of each column against each 'Weather Condition'?
# mean_values = df.groupby('Weather Condition').mean()
# print(mean_values)

# Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?

min_values = df.groupby('Weather Condition').min()
max_values = df.groupby('Weather Condition').max()
print("Q. 12)")
print("Minimum values:")
print(min_values)
print("\nMaximum values:")
print(max_values)

# Q. 13) Show all the Records where Weather Condition is Fog.
fog_records = df[df['Weather Condition'] == 'Fog']
print("Q. 13)")
print(fog_records)

# Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
clear_or_high_visibility = df[(df['Weather Condition'] == 'Clear') | (df['Visibility_km'] > 40)]
print("Q. 14)")
print(clear_or_high_visibility)


# Q. 15) Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'
condition_A = (df['Weather Condition'] == 'Clear') & (df['Rel Hum_%'] > 50)
condition_B = (df['Visibility_km'] > 40)

instances = df[condition_A | condition_B]
print("Q. 15)")
print(instances)