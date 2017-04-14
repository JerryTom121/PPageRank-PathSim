#Xinbo Wu
#Utility functions

def make_vec(keys):
    result = dict()
    for key in keys:
        result.update({key:1})
        
    return result


def make_adlist(file_name):
    result = dict()
    
    f = open(file_name, 'r')

    for line in f:
        splited = line.rstrip().split('\t')
        
        if result.has_key(splited[0]):
            if result[splited[0]].has_key(splited[1]):
                print "1"
                result[splited[0]][splited[1]] += 1
            else:
                result[splited[0]].update({splited[1]:1})
        else:
            result.update({splited[0]:{splited[1]:1}})

        if result.has_key(splited[1]):
            if result[splited[1]].has_key(splited[0]):
                print "1"
                result[splited[1]][splited[0]] += 1
            else:
                result[splited[1]].update({splited[0]:1})
        else:
            result.update({splited[1]:{splited[0]:1}})
        

    f.close()

    return result

def file_to_dict(file_name):
    result = dict()
    
    f = open(file_name, 'r')

    for line in f:
        splited = line.rstrip().split('\t')
        
        if result.has_key(splited[0]):
                result[splited[0]].append(splited[1])
        else:
            result.update({splited[0]:[splited[1]]})

    f.close()

    return result

def nom_adlist(adlist):
    tmp_adlist = adlist.copy()

    for key1 in tmp_adlist.keys():
        count = 0
        
        for key2 in tmp_adlist.keys():
            count += tmp_adlist[key2].has_key(key1)
            
        for key2 in tmp_adlist.keys(): 
            if tmp_adlist[key2].has_key(key1):
                tmp_adlist[key2][key1] = float(tmp_adlist[key2][key1])/count

    return tmp_adlist


def nom_vec(vec):
    tmp_vec = vec.copy()

    dom = sum(tmp_vec.values())
    
    
    for key in tmp_vec.keys():
        tmp_vec[key] = float(tmp_vec[key])/dom

    return tmp_vec
            

def adlist_vec_multiply(adlist, vec):
    result = dict()

    for key1 in adlist.keys():
        tmp1 = adlist[key1]
        tmp_sum = 0
        
        for key2 in vec.keys():
            if tmp1.has_key(key2):
                tmp_sum += tmp1[key2]*vec[key2]

        result.update({key1:tmp_sum})
    return result

def constant_vec_multiply(constant, vec):
    tmp_vec = vec.copy()
    
    for key in tmp_vec.keys():
        tmp_vec[key] = constant*tmp_vec[key]

    return tmp_vec


def vec_vec_add(vec1, vec2):
    tmp_vec1 = vec1.copy()
    tmp_vec2 = vec2.copy()
    
    for key in tmp_vec2.keys():
        if tmp_vec1.has_key(key):
            tmp_vec1[key] += tmp_vec2[key]
        else:
            tmp_vec1.update({key:tmp_vec2[key]})

    return tmp_vec1


def find_ID(file_name, name):
    result = ""
    
    f = open(file_name,'r')

    for line in f:
        splited = f.split('\t')

        if splited[1] == name:
            result = splited[0]
            break

    f.close()

    return result


def make_ID_name_dict(file_name):
    result = dict()
    
    f = open(file_name,'r')

    for line in f:
        splited = line.rstrip().split('\t')

        result.update({splited[0]:splited[1]})

    f.close()
    #print(result)
    return result

def make_name_ID_dict(file_name):
    result = dict()
    
    f = open(file_name,'r')

    for line in f:
        splited = line.rstrip().split('\t')

        result.update({splited[1]:splited[0]})
    
    f.close()
    #print(result)

    return result

        

    
    

        






























    
    
