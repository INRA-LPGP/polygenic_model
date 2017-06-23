

class Locus:

    def __init__(self, allele_1, allele_2):

        self.allele_1 = allele_1
        self.allele_2 = allele_2

    def output(self):

        return self.allele_1 + self.allele_2

    def gametes(self):

        return [self.allele_1, self.allele_2]
