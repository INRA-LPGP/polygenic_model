from model.definitions import sex_from_genotype
from .locus import Locus
import random


class Individual:

    count = 0

    def __init__(self, genotype=None, parents=None):

        self.id_n = Individual.count
        if genotype:
            self.init_from_genotype(genotype)
        if parents:
            self.init_from_parents(parents)
        self.assign_sex()
        Individual.count += 1

    def assign_sex(self):

        if self.locus_1 is None or self.locus_2 is None:
            self.sex = 'N'
        elif self.locus_1.allele_1 is None:
            self.sex = 'N'
        elif self.locus_1.allele_2 is None:
            self.sex = 'N'
        elif self.locus_2.allele_1 is None:
            self.sex = 'N'
        elif self.locus_2.allele_2 is None:
            self.sex = 'N'
        else:
            self.sex = sex_from_genotype(self.genotype())

    def init_from_genotype(self, genotype):

        self.locus_1 = Locus(genotype[0][0], genotype[0][1])
        self.locus_2 = Locus(genotype[1][0], genotype[1][1])

    def init_from_parents(self, parents):

        father = parents[0]
        mother = parents[1]

        self.locus_1 = Locus(random.choice(father.locus_1.gametes()),
                             random.choice(mother.locus_1.gametes()))

        self.locus_2 = Locus(random.choice(father.locus_2.gametes()),
                             random.choice(mother.locus_2.gametes()))

        # print(mother.genotype(), father.genotype(), self.genotype())

    def genotype(self):

        genotype_1 = ''.join(sorted(self.locus_1.allele_1 +
                                    self.locus_1.allele_2))
        genotype_2 = ''.join(sorted(self.locus_2.allele_1 +
                                    self.locus_2.allele_2, reverse=True))

        return (genotype_1, genotype_2)
