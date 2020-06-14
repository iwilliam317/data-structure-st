from pyhash import murmur3_32, fnv1_32

class BloomFilter():
    def __init__(self):
        self.DIVISOR = 20
        self.big_vector = [0] * self.DIVISOR
        self.fnv = fnv1_32()
        self.murmur = murmur3_32()
    
    def add_value(self, value):
        fnv_value = self.fnv(value) % self.DIVISOR
        murmur_value = self.murmur(value) % self.DIVISOR

        if self.is_value_saved(fnv_value, murmur_value):
            print('%s already there!' %(value))
            return
        
        self.big_vector[fnv_value] = 1
        self.big_vector[murmur_value] = 1
        print('%s added' %(value))

    def print_big_vector(self):
        print(self.big_vector)

    def is_value_saved(self, fnv_value, murmur_value):
        return self.big_vector[fnv_value] & self.big_vector[murmur_value]
        
bloom = BloomFilter()
bloom.add_value('Table')
bloom.add_value('Cooker')
bloom.add_value('Shelf')
bloom.add_value('Cooker')
bloom.print_big_vector()