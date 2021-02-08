import random

class DNA:
	def __init__(self, gene, chromosome):
	    self.gene = gene
	    self.chromosome = chromosome

	def Gene(self, gene):
		gene = [0, 1]
		return random.randint(0, 1)

	def Chromosome(self, chromosome):
		chromosome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		return random.randint(0, 9)

	def D_N_A(self, chromosome):
		chromosome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		return random.randint(0, 9)

gene1 = DNA("Blond", "Y")
print(gene1.Gene(0))

chromo1 = DNA("Brown", "X")
print(gene1.Chromosome(1))

dna1 = DNA("Red-Hair", "XY")
print(dna1.D_N_A(2))


class Organism(DNA):
	def __init__(self, gene, chromosome):
		super().__init__(gene, chromosome)
	    self.environment = environment

	def Environment(self, environment):




