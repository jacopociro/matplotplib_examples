import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

fig = plt.figure(figsize=(5, 1.5))
text = fig.text(0.5, 0.5, 'hello path effect world!\n this is the normal path effect\n pretty dull uh?', ha='center', va='center', size=20)
text.set_path_effects([path_effects.Normal()])

fig = plt.figure()
text = fig.text(0.5, 0.5, 'hello path effect world!', path_effects=[path_effects.withSimplePatchShadow()])

plt.plot([0, 3, 2, 5], linewidth=5, color='blue', path_effects=[path_effects.SimpleLineShadow(), path_effects.Normal()])

# making an artist stand out
fig = plt.figure(figsize=(7, 1))
text = fig.text(0.5, 0.5, 'this text stands out beacuse of \n''its black border', color='white', ha='center', va='center', size=30)
text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='black'), path_effects.Normal()])

# greater control
fig = plt.figure(figsize=(8.5, 1))
t = fig.text(0.02, 0.5, 'Hatch shadow', fontsize=75, weight=1000, va='center')
t.set_path_effects([path_effects.PathPatchEffect(offset=(4, -4), hatch='xxxx', facecolor='gray'), path_effects.PathPatchEffect(edgecolor='white', linewidth=1.1, facecolor='black')])
plt.show()