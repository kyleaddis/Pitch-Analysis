import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/savant_data.csv")


pitches = data[['pitch_type', 'release_speed', 'release_pos_x', 'release_spin_rate', 'release_extension', 'spin_axis',
       'release_pos_z', 'stand', 'zone', 'description', 'balls', 'strikes', 'game_year', 'inning', 'outs_when_up',
       'pfx_x', 'pfx_z', 'plate_x', 'plate_z', 'on_3b', 'on_2b', 'on_1b', 'vx0', 'vy0', 'vz0', 'ax', 'ay', 'az',
       'pitch_number', 'pitch_name']]

#sns.scatterplot(x='release_speed', y='release_spin_rate', data=pitches, hue='pitch_name' )
sns.violinplot(x='release_speed', y='pitch_type', data=pitches)
plt.show()

fastballs = pitches[pitches['pitch_type'] == 'FF']
fb_by_year = fastballs.groupby('game_year')['release_spin_rate'].mean()
print(fb_by_year)