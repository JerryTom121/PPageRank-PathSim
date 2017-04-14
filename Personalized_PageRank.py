#Xinbo Wu
#Personalized PageRank

from Utility import *


class P_PageRank(object):

    def __init__(self, net_file_name, name_ID_file_name, c=0.15):
        self.net_adlist = nom_adlist(make_adlist(net_file_name))
        self.c = c
        self.name_ID_dict = make_name_ID_dict(name_ID_file_name)
        self.ID_name_dict = make_ID_name_dict(name_ID_file_name)
        
        
    def set_preference(self, p_set=[]):
        self.u = dict()
        for element in p_set:
            key = self.name_ID_dict[element]
            self.u.update({key:1})
        
        self.u = nom_vec(self.u)
        
        

    def run(self, num_iter=10):
        self.v = nom_vec(make_vec(self.net_adlist.keys()))


        #print(self.v)
        for i in xrange(num_iter):
            self.v = constant_vec_multiply(1-self.c,
                                            adlist_vec_multiply(
                                                self.net_adlist, self.v))
            self.v = vec_vec_add(self.v, constant_vec_multiply(
                self.c, self.u))
            #print(self.v)

        print "finished"



    def find_top_n(self, n):
        result = dict()
        sorted_keys = sorted(self.v, key=self.v.__getitem__)
        
        for key in sorted_keys[len(self.v) - n :len(self.v)]:
            result.update({key:self.v[key]})

        return result
    
    











        
