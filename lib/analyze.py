import pandas as pd

# Number of parking spaces in an area.
def number_of_p_spaces(self, area = "Indre By"):
    data = self.df_pni[self.df_pni.bydel == area]
    total = data['antal_pladser'].sum()
    p_spaces_per_road = data.groupby(['vejnavn'])['antal_pladser'].sum().sort_values()

    road_with_most = p_spaces_per_road.keys()[-1]

    return str(total) + " spaces in Indre by - " + road_with_most + " has the most spaces"

# Number of parking spaces by odd and even house numbers
def p_spaces_odd_even(df):
    most_Lige = df[df.vejside == 'Lige husnr.']
    most_ulige = df[df.vejside == 'Ulige husnr.']

    return 'Lige husnr {}'.format(len(most_Lige)) , 'Ulige husnr {}'.format(len(most_ulige))


# Number of parking spaces for electric vehicles and number of private parkingspaces
def featured_spaces(self):
    electric_spaces_per_area = {}
    private_spaces_per_area = {}

    for area in self.areas:
        electric_spaces_per_area[area] = self.spaces_by_type[area]['El-Bil plads']
        private_spaces_per_area[area] = self.spaces_by_status[area]['Privat fællesvej']

        if 'Privat fællesvej §2 stk1' in self.spaces_by_status[area]:
            private_spaces_per_area[area] += self.spaces_by_status[area]['Privat fællesvej §2 stk1']

        if 'Privat fællessti' in self.spaces_by_status[area]:
            private_spaces_per_area[area] += self.spaces_by_status[area]['Privat fællessti']

    self.espa, self.pspa = electric_spaces_per_area, private_spaces_per_area



# Number of marked parking spaces in data serial
def marked_p_spaces(ds):
    pass

# Most common family constellations per area
def fam_const(self):
    for area in self.areas:
        self.area_const_dict[area] = self.constellations[area].sort_values(ascending=False).keys()[0]


# Best parking opportunities for family constellations
def best_parking(self):
    spaces_by_area = self.df_pni.groupby(['bydel'])['antal_pladser'].sum()
    spaces_by_area = spaces_by_area.sort_values(ascending=False)

    self.const_with_best_parking = self.area_const_dict[spaces_by_area.keys()[0]]


def income_by_area(self):
    for area in self.areas:
        self.income_dist_dict[area] = self.incomes[area].sort_values().keys()[-1]
