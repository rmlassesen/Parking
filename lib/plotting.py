from lib.helpers import _alfa_order_by_key as alfa
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# Bar-stack plot showing the distribution between public and private parking spaces per area
def public_private_distro(self):
    pass

# Plot of the amount of private and electric parking spaces per average income
def private_electric_income(self):
    try:
        self.pspa
    except:
        self.analyze()

    pspa = alfa(self.pspa)
    espa = alfa(self.espa)
    indi = alfa(self.income_dist_dict)
    indi = sorted(indi)

    plt.cla()

    plot_title = "Spaces per net income"

    b_patch = mpatches.Patch(color='blue', label='Private Spaces')
    o_patch = mpatches.Patch(color='orange', label='Electric Spaces')

    plt.plot(indi, pspa)
    plt.plot(indi, espa)

    plt.title(plot_title)
    plt.legend(handles=[b_patch, o_patch], loc='upper center', prop={'size': 10})

    plt.show()

    return "Plot opened - " + plot_title