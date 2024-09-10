from matplotlib import pyplot as plt
from matplotlib_venn import venn3_circles
from matplotlib_venn import venn3
import os

def generate_ikigai_diagram(data, upload_folder):
    plt.figure(figsize=(10,10))

    # Create the Venn diagram
    venn = venn3(subsets=(set(data['what_you_love']),
                          set(data['what_the_world_needs']),
                          set(data['what_you_can_be_paid_for'])),
                 set_labels=('What You Love', 'What the World Needs', 'What You Can Be Paid For'))

    venn_circles = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

    # Set positions for "Passion", "Mission", "Profession", "Vocation"
    plt.text(-0.7, 0.7, 'Passion', size=16, horizontalalignment='center')
    plt.text(0.7, 0.7, 'Mission', size=16, horizontalalignment='center')
    plt.text(-0.7, -0.7, 'Profession', size=16, horizontalalignment='center')
    plt.text(0.7, -0.7, 'Vocation', size=16, horizontalalignment='center')

    # Ikigai should be at the center
    plt.text(0, 0, 'Ikigai', size=20, weight='bold', horizontalalignment='center')

    # Save the figure
    image_path = os.path.join(upload_folder, 'ikigai_diagram.png')
    plt.savefig(image_path, bbox_inches='tight')
    plt.close()

    return image_path
