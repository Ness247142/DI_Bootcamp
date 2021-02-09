# import random

# class DNA:
# 	def __init__(self, gene, chromosome):
# 	    self.gene = gene
# 	    self.chromosome = chromosome
# 	    self.chromosome_list = []
# 	    self.dna_list = []

# class Gene:
# 	def __init__(self):
# 		self.gene = random.randint(0, 1)
# 		return self.gene

# class Chromosome:
# 	for x in range(0, 10):
# 		self.chromosome_list.append(self.gene)
# 		return self.chromosome_list

# class DNA:
# 	def __init__(self):
# 		for x in range(0, 10):
# 			self.dna_list.append(self.chromosome_list)
# 			return self.dna_list



from random import randint, random

class Gene:
	def __init__(self):
		self.value = randint(0, 1)

	def mutate(self):
		self.value == 1 if self.value == 0 else self. value == 1
		# self.value = int(not bool(self.value))

	def __repr__(self):
		return str(self.value)

class Chromosome:
	def __init__(self):
		self.value = [Gene() for i in range(10)]

	def mutate(self):
		for gene in self.value:
			if random() > 0,5:
				gene.mutate()

	def __repr__(self):
		return f"{self.value}"

class DNA:
	def __init__(self):
		self.value = [Chromosome()] for _ in range(10)

	def __repr__(self):
		return f"{self.value}"



c = Chromosome()
c.value()

c.mutate()

d = DNA()
d.value()


gene1 = Gene()
gene1.value()

chromo1 = Chromosome()
chromo1.value()

dna1 = DNA()
dna1.value()


class Organism(DNA):
	def __init__(self):
		super().__init__(self)
	    self.environment = environment
