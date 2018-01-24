import random
import string

def random_str(max_str_len):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1, max_str_len)))

class RandomTestCase(object):
    def __init__(self, seed=0, fields_scheme=None):
        '''
        fields_scheme(set): fields name of generated documents. (Default: ["name"])
        '''
        if fields_scheme is None:
            fields_scheme = ["name"]

        random.seed(seed)
        self.fields_scheme = fields_scheme

    def generate_random_case(self, max_str_len=5):
        random_case = {}
        for field_name in self.fields_scheme:
            random_case.update({field_name: random_str(max_str_len)})
        return random_case
