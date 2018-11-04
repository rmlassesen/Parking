from lib import *
from inspect import getmembers, isfunction

class Parking:
    def __init__(self, p_info_url, soceco_url):
        self.electric_spaces_per_area = {}
        self.private_spaces_per_area = {}
        self.area_const_dict = {}
        self.income_dist_dict = {}

        self.set_vars(p_info_url, soceco_url)
        self.get_areas()


    def set_vars(self, p_info_url, soceco_url):
        df_p_info = datahandler.get_dataframe(p_info_url)
        df_soceco = datahandler.get_dataframe(soceco_url)

        df_p_info['antal_pladser'] = df_p_info['antal_pladser'].apply(int)
        df_soceco['HUSTANDE'] = df_soceco['HUSTANDE'].apply(int)

        df_soceco = df_soceco[(df_soceco.AAR == '2014') & (df_soceco.DISTRIKTSNAVN != 'Uden for inddeling')]
        df_soceco['DISTRIKTSNAVN'] = df_soceco['DISTRIKTSNAVN'].apply(helpers._normalize_area)

        self.spaces_by_type = df_p_info.groupby(['bydel', 'p_ordning'])['antal_pladser'].sum()
        self.spaces_by_status = df_p_info.groupby(['bydel', 'vejstatus'])['antal_pladser'].sum()

        spaces_by_area = df_p_info.groupby(['bydel'])['antal_pladser'].sum()
        self.spaces_by_area = spaces_by_area.sort_values(ascending=False)

        self.incomes = df_soceco.groupby(['DISTRIKTSNAVN', 'INDKOMSTKATEGORI'])['HUSTANDE'].sum()
        self.constellations = df_soceco.groupby(['DISTRIKTSNAVN', 'FAMILIEGRUPPE'])['HUSTANDE'].sum()

        self.df_soc = df_soceco
        self.df_pni = df_p_info

    def get_areas(self):
        areas = self.df_soc.groupby(['DISTRIKTSNAVN']).groups
        self.areas = list(areas.keys())

    def analyze(self):
        self.featured_spaces()
        self.fam_const()
        self.best_parking()
        self.income_by_area()



for func in getmembers(analyze, isfunction):
    setattr(Parking,func[0], func[1])

for func in getmembers(plotting, isfunction):
    setattr(Parking,func[0], func[1])

for func in getmembers(mapping, isfunction):
    setattr(Parking,func[0], func[1])