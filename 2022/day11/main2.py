#!/usr/bin/python3

import math

class Monkey:
	index = 0
	items = []
	operation = ''
	test = 0
	test_true = 0
	test_false = 0
	inspect_amount = 0
	def __init__(self, index):
		self.index = int(index)
	def set_item(self, items):
		self.items = items
	def set_operation(self, op):
		self.operation = op
	def set_test(self, test):
		self.test = int(test)
	def set_test_true(self, test):
		self.test_true = int(test)
	def set_test_false(self, test):
		self.test_false = int(test)
	def execute(self, index, prod_diviser):
		self.inspect_amount += 1
		old = self.items[index]
		new = eval(self.operation)
		new %= prod_divisor
		if new % self.test == 0:
			self.items.pop(index)
			return new, self.test_true
		else:
			self.items.pop(index)
			return new, self.test_false
	def add_item(self, value):
		self.items.append(int(value))
	def get_item_amount(self):
		return len(self.items)
	def print_items(self):
		print(self.index, self.items)
	def get_inspect_amount(self):
		return self.inspect_amount

monkeys = []

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		if line.startswith('Monkey'):
			monkeys.append(Monkey(line.split()[-1][:-1]))
		if line.startswith('Starting items: '):
			monkeys[-1].set_item([int(i) for i in line.replace('Starting items: ', '').split(', ')])
		if line.startswith('Operation: '):
			monkeys[-1].set_operation(line.replace('Operation: new = ', ''))
		if line.startswith('Test: '):
			monkeys[-1].set_test(line.replace('Test: divisible by ', ''))
		if line.startswith('If true: '):
			monkeys[-1].set_test_true(line.replace('If true: throw to monkey ', ''))
		if line.startswith('If false: '):
			monkeys[-1].set_test_false(line.replace('If false: throw to monkey ', ''))

prod_divisor = math.prod([monkey.test for monkey in monkeys])

for _ in range(10000):
	for count,monkey in enumerate(monkeys):
		for _ in range(monkey.get_item_amount()):
			value,idx = monkey.execute(0, prod_divisor)
			monkeys[idx].add_item(value)

total = []
for monkey in monkeys:
	total.append(monkey.get_inspect_amount())
total.sort()
print(total[-1] * total[-2])
