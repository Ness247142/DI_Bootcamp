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


class Organism(DNA):
	def __init__(self, gene, chromosome):
		super().__init__(gene, chromosome)
	    self.environment = environment

	def Environment(self, environment):


