# mapping = {native_key : normal_key}
mapping = {
    'ENERC_KCAL': 'ENERC_KCAL',
    'ENERC_KJ': 'ENERC',
    'WATER': 'WATER',
    'PROCNT': 'PROCNT',
    'PROTA': 'PROTA',
    'NT': 'NT',  # no nitrogen equivalent (nitrogen factor?)
    'FAT': 'FAT',
    'ASH': 'ASH',
    'FIBTG': 'FIBTG',
    'ALC': 'ALC',
    'FRUS': 'FRUS',
    'GLUS': 'GLUS',
    'SUCS': 'SUCS',
    'MALS': 'MALS',
    'LACS': 'LACS',
    'GALS': 'GALS',
    # 'MALT3' : 'MALTRS',

    'SUGAR': 'SUGAR',
    'STARCH': 'STARCH',

    'DEXTN': 'DEXTN',
    'GLYR': 'GLYRL',
    'GLYC': 'GLYC',
    'INULN': 'INULN',
    'MANTL': 'MANTL',
    'MALTDEX': 'MALTDEX',
    'OLSAC': 'OLSAC',
    'RAFS': 'RAFS',
    'STAS': 'STAS',
    'SORTL': 'SORTL',
    'CHOAVL': 'CHOAVL',
    # 'AVAILCHOCNS' : 'AVAILCHOCNS',
    'CHOCDF': 'CHOCDF',
    'ACEAC': 'ACEAC',
    'CITAC': 'CITAC',
    'FUMAC': 'FUMAC',
    'LACAC': 'LACAC',
    'MALAC': 'MALAC',
    'OXALAC': 'OXALAC',
    'PROPAC': 'PROPAC',
    'QUINAC': 'QUINAC',
    'SHIKAC': 'SHIKAC',
    'SUCAC': 'SUCAC',
    'TARAC': 'TARAC',
    'AL': 'AL',  # not in USDA
    'SB': 'SB',
    'AS': 'AS',
    'CD': 'CD',
    'CR': 'CR',
    'CO': 'CO',
    'CA': 'CA',
    'CU': 'CU',
    'F': 'FD',
    'FD': 'FD',
    'FLD': 'FD',
    'I': 'ID',
    'PB': 'PB',
    'FE': 'FE',
    'MG': 'MG',
    'MN': 'MN',
    'HG': 'HG',
    'MO': 'MO',
    'NI': 'NI',
    'P': 'P',
    'K': 'K',
    'SE': 'SE',
    'NA': 'NA',
    'S': 'S',  # not found
    'SN': 'SN',
    'ZN': 'ZN',
    'BETN': 'BETN',
    'HYP': 'HYP',
    'HISTN_G': 'HIS',
    'THEBRN': 'THEBRN',
    'CHOLN': 'CHOLN',
    'THIA': 'THIA',  # THIAMIN (THIA)
    'RIBF': 'RIBF',  # RIBOFLAVIN (RIBF)
    'NIA': 'NIA',  # NIACIN (NIA)
    'NIAEQ': 'NIAEQ',  # NIACIN EQUIVALENTS?
    'PANTAC': 'PANTAC',
    'VITB6A': 'VITB6A',
    'MK4': 'MK4',  # menaquinone-4 (VIT K)
    'BIOT': 'BIOT',  # not available in USDA
    'VITB12': 'VITB12',
    'FOL': 'FOL',  # folate total
    'FOLAC': 'FOLAC',
    'FOLFD': 'FOLFD',
    'FOLDFE': 'FOLDFE',

    'CARTA': 'CARTA',
    'CARTB': 'CARTB',
    'CRYPX': 'CRYPX',
    'CARTBEQ': 'CARTBEQ',
    'LUT+ZEA': 'LUT+ZEA',
    'LYCPN': 'LYCPN',
    # 'XANTHOPHYL' : 'XANTHOPHYL',
    'VITE': 'VITE',
    'V1TB12': 'V1TB12',
    'VITK1': 'VITK',
    'VITK': 'VITK',
    'VITK1D': 'VITK1D',
    'RETOL': 'RETOL',
    'VITA_IU': 'VITA_IU',
    'VITA_RAE': 'VITA',
    'VITC': 'VITC',
    'VITA': 'VITA',
    # vitd file
    'CHOCAL': 'CHOCAL',
    'ERGCAL': 'ERGCAL',
    '25HCHOOL': 'CHOCALOH',
    '25HERGCAL': 'ERGCALOH',
    'VITAMIND3EQ': 'VITDEQ',
    'VITD': 'VITD',

    # sterols
    'PHYSTR': 'PHYSTR',
    'STID7': 'STID7',
    'CAMD5': 'CAMD5',
    'SITSTR': 'SITSTR',

    'TOCPHA': 'TOCPHA',  # VIT E
    'TOCTRA': 'TOCTRA',
    'TOCPHB': 'TOCPHB',
    'TOCTRB': 'TOCTRB',
    'TOCPHD': 'TOCPHD',
    'TOCTRD': 'TOCTRD',
    'TOCPHG': 'TOCPHG',
    'TOCTRG': 'TOCTRG',
    'F4D0': 'F4D0',
    'F6D0': 'F6D0',
    'F8D0': 'F8D0',
    'F10D0': 'F10D0',
    'F12D0': 'F12D0',
    'F13D0': 'F13D0',
    'F14D0': 'F14D0',
    'F15D0': 'F15D0',
    'F16D0': 'F16D0',  ### revie
    'F17D0': 'F17D0',
    'F18D0': 'F18D0',
    'F19D0': 'F19D0',  # (mg)
    'F20D0': 'F20D0',
    'F21D0': 'F21D0',
    'F22D0': 'F22D0',
    'F23D0': 'F23D0',
    'F24D0': 'F24D0',

    # saturated FAT
    'FASAT': 'FASAT',
    'F10D1': 'F10D1',
    'F14D1': 'F14D1',
    'F15D1': 'F15D1',
    'F16D1': 'F16D1',
    'F16D1T': 'F16D1T',
    'F16D1C': 'F16D1C',
    'F17D1': 'F17D1',
    'F18D1': 'F18D1',
    'F18D1C': 'F18D1C',
    'F18D2': 'F18D2',
    'F18D2TT': 'F18D2TT',
    'F18D2I': 'F18D2I',
    'F18D3': 'F18D3',
    'F18D3T': 'F18D3T',
    'F18D3I': 'F18D3I',
    'F18D4': 'F18D4',
    'F18D1TN7': 'F18D1N7',  # USDA USES A TOTAL
    'F18D1N7': 'F18D1N7',
    'F20D1': 'F20D1',
    'F20D1N11': 'F20D1N11F',  # NA
    'F21D5': 'F21D5',
    'F22D1': 'F22D1',
    'F22D1T': 'F22D1T',
    'F24D1': 'F24D1',
    'F24D1C': 'F24D1C',

    # monosaturated FAT in g
    'FAMS': 'FAMS',
    'FAMSF': 'FAMSF',
    'P182W6': 'F18D2CN6',
    'F18D3CN6': 'F18D3N6',
    'F18D2CN6': 'F18D2CN6',
    'F18D4CN3': 'F18D4N3',
    'F20D2CN6': 'F20D2N6',
    'P204W3': 'F20D4N3',  # not in USDA but in NUTTAB 20:4 n-3
    'F20D4': 'F20D4',
    'F22D1C': 'F22D1C',
    'F22D6': 'F22DN3',
    'F22D4': 'F22D6',

    'P182W6FD': 'F18D2N6',
    'F18D2N6': 'F18D2N6',
    'F18D2N6F': 'F18D2N6F',
    'P183W3FD': 'F18D3N3',
    'F18D3N3': 'F18D3N3',
    'F18D3N3F': 'F18D3N3F',
    'P183W6FD': 'F18D3N6',
    'F18D3N6': 'F18D3N6',
    'F18D3N6F': 'F18D3N6F',
    'P184W3FD': 'F18D4N3',
    'F18D4N3': 'F18D4N3',
    'F18D4N3F': 'F18D4N3F',
    'P202W6FD': 'F20D2N6',
    'F20D2N6': 'F20D2N6',
    'F20D2N6F': 'F20D2N6F',
    'P203W3FD': 'F20D3N3',
    'F20D3N3': 'F20D3N3',
    'F20D3N3F': 'F20D3N3F',
    'P203W6FD': 'F20D3N6',
    'F20D3N6': 'F20D3N6',
    'F20D3N6F': 'F20D3N6F',
    'P204W3FD': 'F20D4N3',
    'F20D4N3': 'F20D4N3',
    'F20D4N3F': 'F20D4N3F',
    'P204W6FD': 'F20D4N6',
    'F20D4N6': 'F20D4N6',
    'F20D4N6F': 'F20D4N6F',
    'P205W3FD': 'F20D5N3',
    'F20D5N3': 'F20D5N3',
    'F20D5N3F': 'F20D5N3F',
    'P222W6FD': 'F22N2D6',
    'F22N2D6': 'F22N2D6',
    'F22N2D6F': 'F22N2D6F',
    'P224W6FD': 'F22D4N6',
    'F22D4N6': 'F22D4N6',
    'F22D4N6F': 'F22D4N6F',
    'P225W3FD': 'F22D5N3',
    'F22D5N3': 'F22D5N3',
    'P224W6': 'F22D4N6F',
    'P225W3': 'F22D5N3F',
    'F22D5N3F': 'F22D5N3F',
    'P226W3FD': 'F22D6N3',
    'F22D6N3': 'F22D6N3',
    'F22D6N3F': 'F22D6N3F',
    'FAPU': 'FAPU',
    'LCW3TOTAL': 'LCW3TOTAL',
    'S4FD': 'F4D0',
    'S6FD': 'F6D0',
    'S8FD': 'F8D0',
    'S10FD': 'F10D0',
    'S11D': 'F11D0',
    'S12FD': 'F12D0',
    'S13FD': 'F13D0',
    'S14FD': 'F14D0',
    'S16FD': 'F16D0',
    'S18FD': 'F18D0',
    'S19FD': 'F19D0',
    'S20FD': 'F20D0',
    'S21FD': 'F21D0',
    'S22FD': 'F22D0',
    'S23FD': 'F23D0',

    # monosaturated fats:
    'TOTAL MONOUNSATURATED FAT (FD)': 'FAMS',
    # 'FAMSF': 'FAMSF',
    'F18D3CN3': 'F18D3CN3',  # ALA
    'F22D5': 'F22D5N3',  # DPA
    'F20D3': 'F20D3',  # undifferentiated
    'F20D5': 'F20D5',

    'TOTAL POLYUNSATURATED FAT (FD)': 'FAPU',
    'FAPUF': 'FAPUF',
    'LCW3TOTALFD': 'LCW3TOTALFD',
    'FAUNDIFF': 'FAUNDIFF',
    'FAUNDIFFFD': 'FAUN',
    'FAUN': 'FAUN',

    # transfatty acid File
    'FATRN': 'FATRN',
    'M161T6': 'F16D1TF',
    'F16D1TF': 'F16D1TF',
    'M18T': 'F18D1TF',
    'F18D1TF': 'F18D1TF',
    'M181T9': 'F18D1TN9F',
    'F18D1TN9F': 'F18D1TN9F',
    'M181TW7': 'F18D1TN7F',
    'TOTAL_TRANSMONO (%)': 'FATRNMF',
    'FATRNMF': 'FATRNMF',
    'F18D2T': 'F18D2TF',
    'F18D2CLA': 'F18D2CLA',
    'F18D2CLAFD': 'F18D2CLAFD',
    'F182T9T12': 'F18D2T9T12',
    'F18D2T9T12FD': 'F18D2T9T12',
    'F18D2T9T12F': 'F18D2T9T12F',
    'F18D2T9T12': 'F18D2T9T12',
    'F182TW6': 'F18D2TN6F',
    'F183T9T12T15': 'F183T9T12T15',
    'TOTAL_TRANSPOLY (%)': 'FATRNPF',
    'FATRNPF': 'FATRNPF',
    'M161T6FD': 'F16D1T',
    'F18D1T': 'F18D1T',
    'F181T9FD': 'F18D1TN9',
    'F18D1TN9': 'F18D1TN9',
    'F181TW7FD': 'F18D1TN7',
    'F18D1TN7F': 'F18D1TN7F',
    'TOTAL_TRANSMONO (FD)': 'FATRNM',
    'F182TFD': 'F18D2T',
    'F182CLAFD': 'F182CLAFD',
    'F18D2CLAF': 'F18D2CLAF',
    'F182T9T12FD': 'F182T9T12FD',
    'F182TW6FD': 'F18D2TN6',
    'F18D2TN6': 'F18D2TN6',
    'F18D3TFD': 'F18D3T',
    'F18D3T9T12T15FD': 'F18D3T9T12T15FD',
    'F18D3T9T12T15F': 'F18D3T9T12T15F',
    'FATRNP': 'FATRNP',
    'TOTAL_TRANSFA': 'FATRNF',
    'FATRNF': 'FATRNF',
    'TOTAL_TRANSFAFD': 'FATRN',
    'FATRNM': 'FATRNM',

    # Amino Acid File
    'TRP_G': 'TRP',
    'ALA_G': 'ALA',
    'ARG_G': 'ARG',
    'ASP_G': 'ASP',
    'CYS_G': 'CYS',
    'CYS': 'CYS',
    'GLU_G': 'GLU',
    'GLY_G': 'GLY',
    'HIS_G': 'HIS',
    'ILE_G': 'ILE',
    'ILE': 'ILE',
    'LEU_G': 'LEU',
    'LYS_G': 'LYS',
    'MET_G': 'MET',
    'PHE_G': 'PHE',
    'PRO_G': 'PRO',
    'SER_G': 'SER',
    'THR_G': 'THR',
    'TYR_G': 'TYR',
    'VAL_G': 'VAL',

    # main File
    'CAFFN': 'CAFFN',
    'ENERGY-04DF': 'ENERC',
    'MOIS': 'WATER',
    'PROT': 'PROCNT',
    'NIT': 'NT',  # no nitrogen equivalent (nitrogen factor?)
    'AOACDFTOTW': 'FIBTG',
    'ETOHM': 'ALC',
    'FRU': 'FRUS',
    'GLUC': 'GLUS',
    'SUC': 'SUCS',
    'MALT': 'MALS',
    'LACT': 'LACS',
    'GAL': 'GALS',
    'MALT3': 'MALTRS',
    'MALTRS': 'MALTRS',

    'TOTALSUGARS': 'SUGAR',
    'DEXTRIN': 'DEXTN',
    'GLYCEROL': 'GLYRL',
    'GLYRL': 'GLYRL',
    'GLYCOGEN': 'GLYC',
    'INULIN': 'INULN',
    'MANNITOL': 'MANTL',
    'MALTODEXTRIN': 'MALTDEX',
    'OLIGOSACCH': 'OLSAC',
    'RAFFINOSE': 'RAFS',
    'STACHYOSE': 'STAS',
    'SORB': 'SORTL',
    'AVAILCHO': 'CHOAVL',
    'AVAILCHOCNS': 'AVAILCHOCNS',
    'CHODIFF': 'CHOCDF',
    'ACETIC': 'ACEAC',
    'CITRIC': 'CITAC',
    'FUMARIC': 'FUMAC',
    'LACTIC': 'LACAC',
    'MALIC': 'MALAC',
    'OXALIC': 'OXALAC',
    'PROPIONIC': 'PROPAC',
    'QUINIC': 'QUINAC',
    'SHIKIMIC': 'SHIKAC',
    'SUCCINIC': 'SUCAC',
    'TARTARIC': 'TARAC',
    'IODINE': 'ID',
    'B1': 'THIA',  # THIAMIN (THIA)
    'B2': 'RIBF',  # RIBOFLAVIN (RIBF)
    'B3': 'NIA',  # NIACIN (NIA)
    'NIACIN EQUIVALENTS': 'NIAEQ',  # NIACIN EQUIVALENTS?
    'PANT': 'PANTAC',
    'B6': 'VITB6A',
    'BIOTIN': 'BIOT',  # not available in USDA
    'B12': 'VITB12',
    'FOLATETOT': 'FOL',
    'FOLDFE-04': 'FOLDFE',

    'ACAR': 'CARTA',
    'BCAR': 'CARTB',
    'CRYP': 'CRYPX',
    'BCAREQ-04': 'CARTBEQ',
    'LUTIEN': 'LUTN',
    'LYCO': 'LYCPN',
    'XANTHOPHYL': 'XANTHOPHYL',
    'RET': 'RETOL',
    'RETEQ-05': 'VITA',
    # vitd file
    'CHOOL': 'CHOCAL',

    'ATOC': 'TOCPHA',
    'ATOCOL': 'TOCTRA',
    'BTOC': 'TOCPHB',
    'BTOCOL': 'TOCTRB',
    'DTOC': 'TOCPHD',
    'DTOCOL': 'TOCTRD',
    'GTOC': 'TOCPHG',
    'GTOCOL': 'TOCTRG',
    'S4': 'F4D0F',  # convert all of these to mg/100g (multiple by 100) essentially
    'F4D0F': 'F4D0F',
    'S6': 'F6D0F',
    'F6D0F': 'F6D0F',
    'S8': 'F8D0F',
    'F8D0F': 'F8D0F',
    'S11': 'F11D0F',
    'F11D0F': 'F11D0F',
    'F11D0': 'F11D0',
    'S10': 'F10D0F',
    'F10D0F': 'F10D0F',
    'S12': 'F12D0F',
    'F12D0F': 'F12D0F',
    'S13': 'F13D0F',
    'F13D0F': 'F13D0F',
    'S14': 'F14D0F',
    'F14D0F': 'F14D0F',
    'S15': 'F15D0F',
    'F15D0F': 'F15D0F',
    'S16': 'F16D0F',  ### review
    'F16D0F': 'F16D0F',  ### review
    'S17': 'F17D0F',
    'F17D0F': 'F17D0F',
    'S18': 'F18D0F',
    'F18D0F': 'F18D0F',
    'S19': 'F19D0F',
    'F19D0F': 'F19D0F',
    'S20': 'F20D0F',
    'F20D0F': 'F20D0F',
    'S21': 'F21D0F',
    'F21D0F': 'F21D0F',
    'S22': 'F22D0F',
    'F22D0F': 'F22D0F',
    'S23': 'F23D0F',
    'F23D0F': 'F23D0F',
    'S24': 'F24D0F',
    'F24D0F': 'F24D0F',

    # saturated FAT
    'TOTAL_SATURAT-04': 'FATSAT',
    'FATSAT': 'FATSAT',
    'M10': 'F10D1F',
    'F10D1F': 'F10D1F',
    'M14': 'F14D1F',
    'F14D1F': 'F14D1F',
    'M15': 'F15D1F',
    'F15D1F': 'F15D1F',
    'M16': 'F16D1F',
    'F16D1F': 'F16D1F',
    'M17': 'F17D1F',
    'F17D1F': 'F17D1F',
    'M18': 'F18D1F',
    'F18D1F': 'F18D1F',
    'M18W7': 'F18D1N7F',
    'M181W7': 'F18D1N7F',
    'F18D1N7F': 'F18D1N7F',
    'M20': 'F20D1F',
    'F20D1F': 'F20D1F',
    'M201W11': 'F20D1N11F',
    'F20D1N11F': 'F20D1N11F',
    'M22': 'F22D1F',
    'F22D1F': 'F22D1F',
    'M24': 'F24D1F',
    'F24D1F': 'F24D1F',

    # monosaturated FAT
    'TOTAL MONOUNSATURATED FAT (%)': 'FAMSF',
    'P183W3': 'F18D3N3',
    'P183W6': 'F18D3N6',
    'P184W3': 'F18D4N3',
    'P202W6': 'F20D2N6',
    'P203W3': 'F20D3N3',
    'P203W6': 'F20D3N6',
    'P204W6': 'F20D4N6',
    'P205W3': 'F20D5N3',
    'P222W6': 'P222W6',
    'P226W3': 'F22D6N3',

    'TOTAL POLYUNSATURATED FAT (%)': 'FAPUF',
    'S11FD': 'F11D0',
    'S15FD': 'F15D0',
    'S17FD': 'F17D0',
    'S24FD': 'F24D0',

    # sat FAT
    'TOTALSATURATFD-04': 'FASAT',
    'M10FD': 'F10D1',
    'M14FD': 'F14D1',
    'M15FD': 'F15D1',
    'M16FD': 'F16D1',
    'M17FD': 'F17D1',
    'M18FD': 'F18D1',
    'M18W7FD': 'F18D1N7',
    'M181W7FD': 'F18D1N7',
    'M20FD': 'F20D1',
    'M201W11FD': 'F20D1N11',
    'M22FD': 'F22D1',
    'M24FD': 'F24D1',

    # monosaturated fats:
    # transfatty acid File
    'P182T': 'F18D2TF',
    'F18D2TF': 'F18D2TF',
    'P182CLA': 'P182CLA',
    'P182T9T12': 'P182T9T12',
    'P182TW6': 'F18D2TN6F',
    'F18D2TN6F': 'F18D2TN6F',
    'P183T': 'P183T',
    'P183T9T12T15': 'P183T9T12T15',
    'M181TFD': 'F18D1T',
    'M181T9FD': 'F18D1TN9',
    'M181TW7FD': 'F18D1TN7',
    'P182TFD': 'F18D2T',
    'P182CLAFD': 'P182CLAFD',
    'P182T9T12FD': 'P182T9T12FD',
    'P182TW6FD': 'F18D2TN6',
    'P183TFD': 'P183TFD',
    'P183T9T12T15FD': 'P183T9T12T15FD',
    'TOTAL_TRANSPOLY (FD)': 'FATRNP',

    # Amino Acid File - *** need to convert to not being percentage of nitrogen
    'TRYP': 'TRPN',
    'TRPN': 'TRPN',
    'TRYPFD': 'TRP',
    'TRP': 'TRP',
    'ALA': 'ALAN',
    'ARG': 'ARGN',
    'ASP': 'ASPN',
    'CSY': 'CSYN',
    'GLU': 'GLUN',
    'GLY': 'GLYN',
    'HIS': 'HISN',
    'ILEU': 'ILEN',
    'LEU': 'LEUN',
    'LUTEIN': 'LUTN',
    'LUTN': 'LUTN',
    'LYS': 'LYSN',
    'MET': 'METN',
    'PHE': 'PHEN',
    'PRO': 'PRON',
    'SER': 'SERN',
    'THR': 'THRN',
    'TYR': 'TYRN',
    'VAL': 'VALN',

    # main File
    'CAFFEINE': 'CAFFN',
    'CHOL': 'CHOLE',
    'CHOLE': 'CHOLE',
    'ENERC': 'ENERC',
    'ENERC1': 'ENERC',
    'ID': 'ID',
}