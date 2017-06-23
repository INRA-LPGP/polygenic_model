import parameters
from . import definitions
from .individual import Individual
from .population import Population


def initialize(ini_file_path):

    global_parameters = parameters.load(ini_file_path)

    population = Population()
    genotypes_fraction = int(global_parameters['population_size'] /
                             len(definitions.genotypes))

    output_file = open(global_parameters['output_file'], 'w')
    output_file.write('Generation\t')
    for i, genotype in enumerate(definitions.genotypes):
        output_file.write('/'.join(g for g in genotype))
        if i < len(definitions.genotypes) - 1:
            output_file.write('\t')
        else:
            output_file.write('\n')

    for i in range(global_parameters['population_size']):
        genotype = definitions.genotypes[int(i / genotypes_fraction)
                                         % len(definitions.genotypes)]
        population.add_individual(Individual(genotype))

    return population, global_parameters
