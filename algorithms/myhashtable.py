class HashTable:
	'''
	HashTable with linked-list implementation
	of collision handling. Expands by powers of 2.
	'''
	def __init__(self):
		self.table_log_size = 0
		self.table = [[]]
	
	def put(self, obj):
		index = HashTable.hash(obj)
		
		# Expand table if needed
		total_size = 2 ** self.table_log_size
		while(total_size <= index):
			self.table_log_size += 1
			total_size = 2 ** self.table_log_size
		
		for i in range(0, total_size - len(self.table)):
			self.table.append([])
		
		self.table[index].append(obj)
		
		
	def hash(obj):
		''' 
		Returns an integer indicating the object's
		index in the table
		'''
		hashcode = HashTable.chksum(obj)
		return hashcode
	
	def chksum(obj):
		s = str(obj)
		chksum = 0
		for char in s:
			chksum += ord(char)
			chksum = chksum % 256
		return chksum
		
ht = HashTable()
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put(HashTable())
ht.put("meme")
print(ht.table)

