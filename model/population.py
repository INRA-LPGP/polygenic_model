import random
from .individual import Individual
from .definitions import genotypes
import sys


class Population():

    def __init__(self):

        self.size = 0
        self.generations = 0
        self.individuals = []
        self.genotypes_count = {genotype: 0 for genotype in genotypes}

    def add_individual(self, individual):

        self.individuals.append(individual)
        self.size += 1

    def kill(self):

        self.size = 0
        self.individuals = []

    def output(self, file_path=None):

        if file_path:
            file = open(file_path, 'a')
            for individual in self.individuals:
                file.write(str(individual.id_n) + '\t' +
                           individual.sex + '\t' +
                           individual.locus_1.output() + '\t' +
                           individual.locus_2.output() + '\n')
        else:
            for individual in self.individuals:
                print(str(individual.id_n) + '\t' +
                      individual.sex + '\t' +
                      individual.locus_1.output() + '\t' +
                      individual.locus_2.output())
            print('\n')

    def output_stats(self, file_path=None):

        for genotype in self.genotypes_count.keys():
            self.genotypes_count[genotype] = 0

        for individual in self.individuals:
            self.genotypes_count[individual.genotype()] += 1

        # if file_path:
        #     file = open(file_path, 'a')
        #     file.write(str(self.generations) + '\t')
        #     for i, (genotype, value) in enumerate(self.genotypes_count.items()):
        #         file.write(str(value))
        #         if i < len(self.genotypes_count.items()) - 1:
        #             file.write('\t')
        #     file.write('\n')
        # else:
        #     print(str(self.generations) + '\t')
        #     for genotype, value in self.genotypes_count.items():
        #         print('/'.join(g for g in genotype) + ' : ' + str(value) + '\t')
        #     print('\n')

    def update(self):

        newborns = []

        males = [individual for individual in self.individuals if
                 individual.sex == 'M']
        females = [individual for individual in self.individuals if
                   individual.sex == 'F']

        if len(males) == 0:
            print('The population died: no more males')
            sys.exit()
        if len(males) == 1:
            print('The population died: no more females')
            sys.exit()

        random.shuffle(males)
        random.shuffle(females)

        Individual.count = 0

        for i in range(self.size):
            father = random.choice(males)
            mother = random.choice(females)
            newborns.append(Individual(parents=[father, mother]))

        self.generations += 1
        self.individuals = newborns
