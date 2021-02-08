import random

class DNA:
	def __init__(self, gene, chromosome):
	    self.gene = gene
	    self.chromosome = chromosome
	    self.chromosome_list = []
	    self.dna_list = []

	def Gene(self, gene):
		self.gene = random.randint(0, 1)
		return self.gene

	def Chromosome(self, chromosome):
		for x in range(0, 10):
		    self.chromosome_list.append(self.gene)
		return self.chromosome_list

	def D_N_A(self, chromosome):
		for x in range(0, 10):
		    self.dna_list.append(self.chromosome_list)
		return self.dna_list


gene1 = DNA("Blond", "Y")
print(gene1.Gene(0))

chromo1 = DNA("Brown", "X")
print(gene1.Chromosome(0))

dna1 = DNA("Red-Hair", "XY")
print(dna1.D_N_A(0))


import random

class Gene:
    def __init__(self, gene):
        self.gene = gene

    def mutation(self):
        self.gene = random.randint(0, 1)
        return self.gene


class Chromsome(Gene):
    def __init__(self, gene):
        super().__init__(gene)
        self.chromsome_list = []

    def chromsome_series(self):
        for x in range(10):
            self.mutate()
            self.chromsome_list.append(self.gene)
        return self.chromsome_list

class DNA(Chromsome):
    def __init__(self, gene):
        super().__init__(gene)
        self.dna_list = []

    def dna_series(self):
        for i in range(10):
            self.chromsome_series()
            self.dna_list.append(self.chromsome_list)
    
            
        print(self.dna_list)


class Organism(DNA):
	def __init__(self, gene, chromosome):
		super().__init__(gene, chromosome)
	    self.environment = environment

	def Environment(self, environment):

