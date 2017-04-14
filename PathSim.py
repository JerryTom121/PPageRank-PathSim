#Xinbo Wu
#PathSim for DBLP data

from Utility import *

class PathSim(object):
    '''
        input files: 
        0: relation
        1: author
        2: venue
        3: term
    '''
    def __init__(self, file_names=[]):
        self.paper_others = file_to_dict(file_names[0])

        self.author_dict = make_ID_name_dict(file_names[1])
        self.venue_dict = make_ID_name_dict(file_names[2])
        self.term_dict = make_ID_name_dict(file_names[3])
        self.author_name_ID = make_name_ID_dict(file_names[1])
 
        self.author_venue = dict()
        self.author_term = dict()

        for key in self.paper_others.keys():
            tmp_author_list = []
            tmp_venue_list = []
            tmp_term_list = []

            for element in self.paper_others[key]:
                if self.author_dict.has_key(element):
                     tmp_author_list.append(element)
                elif self.venue_dict.has_key(element):
                     tmp_venue_list.append(element)
                elif self.term_dict.has_key(element):
                     tmp_term_list.append(element)
                     
            for author in tmp_author_list:
                for venue in tmp_venue_list:
                    if self.author_venue.has_key(author):
                        if self.author_venue[author].has_key(venue):
                            self.author_venue[author][venue] += 1
                        else:
                            self.author_venue[author].update({venue:1})
                    else:
                        self.author_venue.update({author:{venue:1}})

                for term in tmp_term_list:
                    if self.author_term.has_key(author):
                        if self.author_term[author].has_key(term):
                            self.author_term[author][term] += 1
                        else:
                            self.author_term[author].update({term:1})
                    else:
                        self.author_term.update({author:{term:1}})


    def run(self, author_name="", meta_path='data/APVPA'):
        self.target_author_name = author_name
        self.target_author_ID = self.author_name_ID[author_name]
        self.result = dict()
        
        if meta_path == 'data/APVPA':
            for author in  self.author_venue.keys():
                tmp_meta_path_count = 0
                tmp_target_self_path_count = 0
                tmp_author_self_path_count = 0
                tmp_common_venue = []
                
                for venue in  self.author_venue[self.target_author_ID].keys():
                    if  self.author_venue[author].has_key(venue):
                        tmp_common_venue.append(venue)
                        tmp_meta_path_count += float(self.author_venue[author][venue])*float(self.author_venue[self.target_author_ID][venue])                        
                        tmp_author_self_path_count +=  float((self.author_venue[author][venue]))**2
                        
                    tmp_target_self_path_count +=  float((self.author_venue[self.target_author_ID][venue]))**2

                s = 2*float(tmp_meta_path_count)/float(tmp_target_self_path_count+tmp_author_self_path_count)
                
                self.result.update({author:s})
            
        else:
            raise "Error only support two meta-path: either APVPA"
    

    def find_top_n(self, n):
        result = dict()
        sorted_keys = sorted(self.result, key=self.result.__getitem__)
        
        for key in sorted_keys[len(self.result) - n :len(self.result)]:
            result.update({key:self.result[key]})

        return result


def main():
    file_names = []
    file_names.append("data/relation.txt")
    file_names.append("data/author.txt")
    file_names.append("data/venue.txt")

    target_author_name1 = "Christos Faloutsos"
    target_author_name2 = "AnHai Doan"
    target_author_name3 = "Xifeng Yan"
    target_author_name4 = "Jamie Callan"

    pathSim = PathSim(file_names)

    '''Find top 10 similar researchers for Christos Faloutsos using APVPA'''
    print "Find top 10 similar researchers for ", target_author_name1, " using APVPA"
    pathSim.run(author_name=target_author_name1, meta_path='APVPA')

    
    result = pathSim.find_top_n(15)

    sorted_result = sorted(result, key=result.__getitem__)

    for i in xrange(len(sorted_result)):
        key = sorted_result[len(sorted_result)-1-i]
        print i+1, ". ", pathSim.author_dict[key], '%.15f' % result[key]

    print "\n"
    '''Find top 10 similar researchers for AnHai Doan using APVPA'''
    print "Find top 10 similar researchers for ", target_author_name2, " using APVPA"
    pathSim.run(author_name=target_author_name2, meta_path='APVPA')

    
    result = pathSim.find_top_n(15)

    sorted_result = sorted(result, key=result.__getitem__)

    for i in xrange(len(sorted_result)):
        key = sorted_result[len(sorted_result)-1-i]
        print i+1, ". ", pathSim.author_dict[key], '%.15f' % result[key]
    

main()   
 






















    
                
            


            
        
        
