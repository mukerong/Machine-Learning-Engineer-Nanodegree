import pandas as pd

# 2005
tax_05 = pd.read_csv('2005.csv',
                     usecols=['state', 'agi_class', 'n1', 'n2', 'n6', 'n21060',
                              'a00100', 'a00200', 'a00300', 'a00600', 'a01000',
                              'a09200', 'PREP'])
tax_05.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'net_capital_gl', 'total_tax', 'prep']
tax_05['year'] = 2005
tax_05['state'] = tax_05['state'].str.upper()

# 2006
tax_06 = pd.read_csv('2006.csv',
                     usecols=['state', 'agi_class', 'n1', 'n2', 'n6', 'n04470',
                              'a00100', 'a00200', 'a00300', 'a00600', 'a23900',
                              'a09200', 'prep'])
tax_06.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'net_capital_gl', 'total_tax', 'prep']
tax_06['year'] = 2006
tax_06['state'] = tax_06['state'].str.upper()

# 2007
tax_07 = pd.read_csv('2007.csv',
                     usecols=['state', 'agi_class', 'n1', 'n2', 'numdep',
                              'n04470', 'a00100', 'a00200', 'a00300', 'a00600',
                              'a23900', 'a18500', 'a06500', 'prep'])
tax_07.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'net_capital_gl', 'real_estate', 'total_tax', 'prep']
tax_07['year'] = 2007
tax_07['state'] = tax_07['state'].str.upper()

# 2008
tax_08 = pd.read_csv('2008.csv',
                     usecols=['state', 'agi_class', 'n1', 'n2', 'numdep',
                              'a00100', 'a00200', 'a00300', 'a00600', 'a06500',
                              'a23900', 'prep'])
tax_08.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'agi', 'total_salary',
                  'taxable_interest', 'ordinary_dividend', 'net_capital_gl',
                  'total_tax', 'prep']
tax_08['year'] = 2008
tax_08['state'] = tax_08['state'].str.upper()

# 2009
tax_09 = pd.read_csv('2009.csv',
                     usecols=['STATE', 'AGI_STUB', 'N1', 'N2', 'NUMDEP',
                              'N04470', 'A00100', 'A00200', 'A00300', 'A00600',
                              'A00650', 'A01000', 'A18500', 'A06500', 'PREP'])

tax_09.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'qualified_dividend', 'net_capital_gl', 'real_estate',
                  'total_tax', 'prep']
tax_09['year'] = 2009
tax_09['state'] = tax_09['state'].str.upper()

# 2010
tax_10 = pd.read_csv('2010.csv',
                     usecols=['STATE', 'agi_stub', 'N1', 'N2', 'NUMDEP',
                              'N04470', 'A00100', 'A00200', 'A00300', 'A00600',
                              'A00650', 'A01000', 'A18500', 'A06500', 'PREP'])

tax_10.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'qualified_dividend', 'net_capital_gl', 'real_estate',
                  'total_tax', 'prep']
tax_10['year'] = 2010
tax_10['state'] = tax_10['state'].str.upper()

# 2011
tax_11 = pd.read_csv('2011.csv',
                     usecols=['STATE', 'agi_stub', 'N1', 'N2', 'NUMDEP',
                              'N04470', 'A00100', 'A00200', 'A00300', 'A00600',
                              'A00650', 'A01000', 'A18500', 'A06500', 'PREP'])

tax_11.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'qualified_dividend', 'net_capital_gl', 'real_estate',
                  'total_tax', 'prep']
tax_11['year'] = 2011
tax_11['state'] = tax_11['state'].str.upper()

# 2012
tax_12 = pd.read_csv('2012.csv',
                     usecols=['STATE', 'AGI_STUB', 'N1', 'N2', 'NUMDEP',
                              'N04470', 'A00100', 'A00200', 'A00300', 'A00600',
                              'A00650', 'A01000', 'A18500', 'A06500', 'PREP'])

tax_12.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'qualified_dividend', 'net_capital_gl', 'real_estate',
                  'total_tax', 'prep']
tax_12['year'] = 2012
tax_12['state'] = tax_12['state'].str.upper()

# 2013
tax_13 = pd.read_csv('2013.csv',
                     usecols=['STATE', 'agi_stub', 'N1', 'N2', 'NUMDEP',
                              'N04470', 'A00100', 'A00200', 'A00300', 'A00600',
                              'A00650', 'A01000', 'A18500', 'A06500', 'PREP'])

tax_13.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'qualified_dividend', 'net_capital_gl', 'real_estate',
                  'total_tax', 'prep']
tax_13['year'] = 2013
tax_13['state'] = tax_13['state'].str.upper()

# 2014
tax_14 = pd.read_csv('2014.csv',
                     usecols=['state', 'agi_stub', 'n1', 'n2', 'numdep',
                              'n04470', 'a00100', 'a00200', 'a00300', 'a00600',
                              'a00650', 'a01000', 'a18500', 'a06500', 'prep'])

tax_14.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'qualified_dividend', 'net_capital_gl', 'real_estate',
                  'total_tax', 'prep']
tax_14['year'] = 2014
tax_14['state'] = tax_14['state'].str.upper()

# 2015
tax_15 = pd.read_csv('2015.csv',
                     usecols=['STATE', 'agi_stub', 'N1', 'N2', 'NUMDEP',
                              'N04470', 'A00100', 'A00200', 'A00300', 'A00600',
                              'A00650', 'A01000', 'A18500', 'A06500', 'PREP'])

tax_15.columns = ['state', 'agi_class', 'num_of_returns', 'num_of_exemptions',
                  'num_of_dependents', 'num_of_itemized', 'agi',
                  'total_salary', 'taxable_interest', 'ordinary_dividend',
                  'qualified_dividend', 'net_capital_gl', 'real_estate',
                  'total_tax', 'prep']
tax_15['year'] = 2015
tax_15['state'] = tax_15['state'].str.upper()

# Concat the data together
raw_data = pd.concat([tax_05, tax_06, tax_07, tax_08, tax_09, tax_10, tax_11,
                      tax_12, tax_13, tax_14, tax_15], ignore_index=True)

raw_data = raw_data[['year', 'state', 'agi_class', 'num_of_returns',
                     'num_of_exemptions', 'num_of_dependents',
                     'num_of_itemized', 'agi', 'total_salary',
                     'taxable_interest', 'ordinary_dividend',
                     'qualified_dividend', 'net_capital_gl', 'real_estate',
                     'total_tax', 'prep']]

raw_data['agi_class'] = raw_data['agi_class'].astype('int64')
raw_data[['num_of_exemptions', 'num_of_itemized', 'total_salary',
          'taxable_interest', 'ordinary_dividend', 'net_capital_gl',
          'real_estate', 'total_tax', 'prep']] = \
    raw_data[['num_of_exemptions', 'num_of_itemized', 'total_salary',
              'taxable_interest', 'ordinary_dividend', 'net_capital_gl',
              'real_estate', 'total_tax', 'prep']].apply(pd.to_numeric,
                                                         errors='coerce')
