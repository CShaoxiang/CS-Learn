# python3
# Use direct addressing to achieve O(1) time on find() and delete ()
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


# create Query objects to process
def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [None] * (10**7)


    for cur_query in queries:
        ph_number = cur_query.number 
      

        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[ph_number] = cur_query.name
        
                
        elif cur_query.type == 'del':
            contacts[ph_number] = None 
               
        else:
            response = contacts[ph_number] if contacts[ph_number] is not None else "not found"  
            result.append(response)

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

