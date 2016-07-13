#palette corresponds to number of piano keys
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotting as p

numcolors = 12
chromatic = { 'C': 0, 'C#': 1,
              'Db': 1, 'D': 2, 'D#': 3,
              'Eb': 3, 'E': 4, 'E#': 5,
              'Fb': 4, 'F': 5, 'F#': 6,
              'Gb': 6, 'G': 7, 'G#': 8,
              'Ab': 8, 'A': 9, 'A#': 10,
              'Bb': 10, 'B': 11, 'B#': 0,
              'Cb': 11,
              }
palette = sns.color_palette('husl',numcolors)

def readNotes(fname):
    notes = []
    with open(fname) as f:
        for line in f.readlines():
            notes.append(line.strip().split(' '))
    return notes


def randomNotes():
    num_lines = 30
    notes = []
    for _ in xrange(num_lines):
        num_notes = 30 * np.random.uniform(0,1)
        notes.append(np.random.choice(chromatic.keys(), num_notes))
    return notes


def main():
    fig = plt.figure(figsize=(10,10), facecolor='black')
    p.remove_axes()
    notes = readNotes('mary.txt')
    #notes = randomNotes()
    num_lines = len(notes)
    spacing = np.linspace(0, 1, num_lines+1)
    line_heights = (spacing[:-1] + spacing[1:])/2
    delta_heights = np.linspace(-.5/num_lines, .5/num_lines, numcolors)
    all_x = []
    all_y = []

    for h, line in zip(line_heights, notes):
        x_vals = np.linspace(0,1,len(line)+1) # in the future handle timing
        x =( x_vals[:-1] + x_vals[1:])/2
        numbers = [chromatic[note] for note in line]
        colors = [palette[num] for num in numbers]
        note_heights = [h + delta_heights[num] for num in numbers]
        plt.scatter(x, note_heights, c=colors, s=40, alpha=0.7)
        all_x = np.concatenate([all_x, x])
        all_y = np.concatenate([all_y, note_heights])

    #sel = np.where(np.random.uniform(0,1,len(all_x)) > .5)[0]
    N = len(all_x)
    sel = np.random.permutation(N)
    line_col = sns.xkcd_rgb['neon blue']
    plt.plot(all_x[sel], all_y[sel], line_col, alpha=0.15)

    for lh in spacing:
        plt.axhline(lh, color='white', alpha=0.1)

    #plt.savefig('music_random.png', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.show()

if __name__ == '__main__':
    main()




