import random, string

class random_test_case:
    def __init__(self, seed=0, fields_scheme={"name"}):
        '''
        fields_scheme(set): fields name of generated documents.
        '''
        random.seed(seed)
        self.fields_scheme = fields_scheme
    
    def random_str(self, max_str_len):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1, max_str_len)))

    def generate_random_case(self, max_str_len =5):
        random_case = {}
        print(self.fields_scheme)
        for field_name in self.fields_scheme:
            random_case.update({field_name: self.random_str(max_str_len)})
        return random_case