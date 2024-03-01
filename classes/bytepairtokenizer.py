from collections import Counter

class BytePairTokenizer:
    def __init__(self):
        self.text = ""
        self.vocab_size = 0
        self.merges = {}
        self.encoded_ids = []
        self.reverse_merges = {}
        self.ids = []
        self.expanded_ids = []

    def _prepare_reverse_dict(self):
        if len(self.merges):
            for (p1,p2),token in self.merges.items():
                self.reverse_merges[token]=(p1,p2)
        else:
            self.reverse_merges= {}
    
    def _get_pair_from_token(self,token):
        try:
            return self.reverse_merges[token]
        except:
            print("Token not in Dict")
            
    def get_stats(self):
        _count = []
        for pair in zip(self.encoded_ids,self.encoded_ids[1:]):
            _count.append(pair)
        item_count = Counter(_count)
        return dict(item_count.items())
        
    def merge(self,ids,pair,new_token):
        new_encoded_text = []
        idx = 0
        while idx < len(ids):
            if idx < len(ids)-1 and ids[idx] == pair[0] and ids[idx+1] == pair[1]:
                new_encoded_text.append(new_token)
                idx += 2
            else:
                new_encoded_text.append(ids[idx])
                idx +=1
        return new_encoded_text

    def _transform_to_utf_tokens(self):
        return list(self.text.encode("utf-8"))
    
    def encode(self,text,vocab_size=276):
        self.text = text
        self.vocab_size = vocab_size
        self.encoded_ids = self._transform_to_utf_tokens()
        for i in range(self.vocab_size-256):
            stats = self.get_stats()
            max_key_pair = max(stats, key=lambda k: stats[k])
            new_token = 256 + i
            self.encoded_ids = self.merge(self.encoded_ids,max_key_pair,new_token)
            self.merges[max_key_pair] = new_token
        self._prepare_reverse_dict()
        return self.encoded_ids
    
    def __expand(self,ids):
        try:
            expanded_ids = []
            for token in ids:
                if token > 255:
                    _pair = self._get_pair_from_token(token)
                    expanded_ids.extend(_pair)
                else:
                    expanded_ids.append(token)        
            if max(expanded_ids) > 255:
                expanded_ids = self.__expand(expanded_ids)
            return expanded_ids
        except Exception as e:
            print("An unexpected error occurred:", e)
            
    def decode(self):
        return bytes(self.__expand(self.encoded_ids)).decode('utf-8',errors='replace')