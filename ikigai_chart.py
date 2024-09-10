from matplotlib import pyplot as plt
from matplotlib_venn import venn3
import os

def find_intersections(data):
    # Convert lists to sets for finding intersections
    love_set = set(data['what_you_love'])
    world_needs_set = set(data['what_the_world_needs'])
    paid_for_set = set(data['what_you_can_be_paid_for'])
    good_at_set = set(data['what_you_are_good_at'])

    passion = love_set & good_at_set
    mission = love_set & world_needs_set
    profession = good_at_set & paid_for_set
    vocation = world_needs_set & paid_for_set

    ikigai = love_set & world_needs_set & paid_for_set & good_at_set

    return passion, mission, profession, vocation, ikigai

def generate_ikigai_diagram(data, upload_folder):
    passion, mission, profession, vocation, ikigai = find_intersections(data)

    plt.figure(figsize=(10, 10))
    
    # Create the Venn diagram
    venn = venn3(subsets=(set(data['what_you_love']),
                          set(data['what_the_world_needs']),
                          set(data['what_you_can_be_paid_for'])),
                 set_labels=('What You Love', 'What the World Needs', 'What You Can Be Paid For'))

    # Manually add text in appropriate positions for each section
    plt.text(-0.7, 0.6, f"Passion: {', '.join(passion)}", size=10, ha='center')
    plt.text(0.7, 0.6, f"Mission: {', '.join(mission)}", size=10, ha='center')
    plt.text(-0.7, -0.6, f"Profession: {', '.join(profession)}", size=10, ha='center')
    plt.text(0.7, -0.6, f"Vocation: {', '.join(vocation)}", size=10, ha='center')
    
    # Ikigai at the center
    plt.text(0, 0, f"Ikigai: {', '.join(ikigai)}", size=14, weight='bold', ha='center')

    # Save the figure
    image_path = os.path.join(upload_folder, 'ikigai_diagram.png')
    plt.savefig(image_path, bbox_inches='tight')
    plt.close()

    return image_path
