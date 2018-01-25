import pandas as pd

# 2005
tax_05 = pd.read_csv('2005.csv',
                     usecols=['state', 'zipcode', 'agi_class', 'n1', 'a00100',
                              'a00200', 'a01000', 'a09200', 'PREP'])
tax_05.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_05['year'] = 2005
tax_05['state'] = tax_05['state'].str.upper()

# 2006
tax_06 = pd.read_csv('2006.csv',
                     usecols=['state', 'zipcode', 'agi_class', 'n1', 'a00100',
                              'a00200', 'a23900', 'a09200', 'prep'])
tax_06.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_06['year'] = 2006
tax_06['state'] = tax_06['state'].str.upper()

# 2007
tax_07 = pd.read_csv('2007.csv',
                     usecols=['state', 'ZIPCODE', 'agi_class', 'n1', 'a00100',
                              'a00200', 'a23900', 'a06500', 'prep'])
tax_07.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_07['year'] = 2007
tax_07['state'] = tax_07['state'].str.upper()

# 2008
tax_08 = pd.read_csv('2008.csv',
                     usecols=['state', 'ZIPCODE', 'agi_class', 'n1', 'a00100',
                              'a00200', 'a23900', 'a06500', 'prep'])
tax_08.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_08['year'] = 2008
tax_08['state'] = tax_08['state'].str.upper()

# 2009
tax_09 = pd.read_csv('2009.csv',
                     usecols=['STATE', 'ZIPCODE', 'AGI_STUB', 'N1', 'A00100',
                              'A00200', 'A01000', 'A06500', 'PREP'])

tax_09.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_09['year'] = 2009
tax_09['state'].str.upper()
tax_09['state'] = tax_09['state'].str.upper()

# 2010
tax_10 = pd.read_csv('2010.csv',
                     usecols=['STATE', 'zipcode', 'agi_stub', 'N1', 'A00100',
                              'A00200', 'A01000', 'A06500', 'PREP'])

tax_10.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_10['year'] = 2010
tax_10['state'].str.upper()
tax_10['state'] = tax_10['state'].str.upper()

# 2011
tax_11 = pd.read_csv('2011.csv',
                     usecols=['STATE', 'ZIPCODE', 'agi_stub', 'N1', 'A00100',
                              'A00200', 'A01000', 'A06500', 'PREP'])

tax_11.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_11['year'] = 2011
tax_11['state'].str.upper()
tax_11['state'] = tax_11['state'].str.upper()

# 2012
tax_12 = pd.read_csv('2012.csv',
                     usecols=['STATE', 'zipcode', 'AGI_STUB', 'N1', 'A00100',
                              'A00200', 'A01000', 'A06500', 'PREP'])

tax_12.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_12['year'] = 2012
tax_12['state'].str.upper()
tax_12['state'] = tax_12['state'].str.upper()

# 2013
tax_13 = pd.read_csv('2013.csv',
                     usecols=['STATE', 'zipcode', 'agi_stub', 'N1', 'A00100',
                              'A00200', 'A01000', 'A06500', 'PREP'])

tax_13.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_13['year'] = 2013
tax_13['state'].str.upper()
tax_13['state'] = tax_13['state'].str.upper()

# 2014
tax_14 = pd.read_csv('2014.csv',
                     usecols=['state', 'zipcode', 'agi_stub', 'n1', 'a00100',
                              'a00200', 'a01000', 'a06500', 'prep'])

tax_14.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_14['year'] = 2014
tax_14['state'].str.upper()
tax_14['state'] = tax_14['state'].str.upper()

# 2015
tax_15 = pd.read_csv('2015.csv',
                     usecols=['STATE', 'zipcode', 'agi_stub', 'N1', 'A00100',
                              'A00200', 'A01000', 'A06500', 'PREP'])

tax_15.columns = ['state', 'zipcode', 'agi_class', 'num_of_returns', 'agi',
                  'total_wages', 'total_capital_gl', 'total_tax', 'prep']
tax_15['year'] = 2015
tax_15['state'].str.upper()
tax_15['state'] = tax_15['state'].str.upper()

raw_data = pd.concat([tax_05, tax_06, tax_07, tax_08, tax_09, tax_10, tax_11,
                      tax_12, tax_13, tax_14, tax_15])
