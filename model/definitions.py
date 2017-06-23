
# Possible values for each locus
locus_1_values = ['X', 'Y']
locus_2_values = ['Z', 'W']

# Possible genotypes
genotypes = [('XX', 'ZZ'), ('XX', 'ZW'), ('XY', 'ZZ'),
             ('XY', 'ZW'), ('YY', 'ZZ'), ('YY', 'ZW')]

# Matrix defining sex assignment
sex_matrix = {'XX': {'ZZ': 'F', 'ZW': 'F'},
              'XY': {'ZZ': 'M', 'ZW': 'F'},
              'YY': {'ZZ': 'M', 'ZW': 'F'}}


def sex_from_genotype(genotype):

    '''
    Function defining sex assignment. Verification for loci values are done
    inside Individual class.
    '''

    return sex_matrix[genotype[0]][genotype[1]]
