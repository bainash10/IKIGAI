from matplotlib import pyplot as plt
from matplotlib_venn import venn3
import os

def generate_ikigai_diagram(data, upload_folder):
    plt.figure(figsize=(10,10))

    # Labels for the Ikigai diagram
    venn = venn3(subsets=(set(data['what_you_love']),
                          set(data['what_the_world_needs']),
                          set(data['what_you_can_be_paid_for'])),
                 set_labels=('What You Love', 'What the World Needs', 'What You Can Be Paid For'))

    # Customize the display to show the fourth set (What You're Good At)
    # Venn3 doesn’t support 4 sets, so we adjust the labels manually

    # Save the figure
    image_path = os.path.join(upload_folder, 'ikigai_diagram.png')
    plt.savefig(image_path)
    plt.close()

    return image_path
