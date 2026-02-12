import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('NutritionStudy.csv', index_col='ID')

#findings
#females have lower average alchohol consumption (excluding greg)
#note: 42 males vs 273 females
#makes sense because of what they are testing, also causes increse at ~35 age (for females)

#overall not much correlation between smoaking status and alchohol consumption
#found that current smoakers have (slightly) less acholhol consumption and average a lower age
#never and former smoakers have similar stats

