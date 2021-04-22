

class Node:
    def __init__(self):
        self.m_children_nodes={}
        self.m_total_word_so_far = ''
        self.m_current_letter = ''
        self.m_word = ''
        self.m_curr_index=0
        

    def add_word(self, word, word_so_far = '', curr_index= -1 ):
        self.m_word = word
        self.m_curr_index = curr_index
        if self.m_curr_index >= 0:
            self.m_curr_letter = self.m_word[self.m_curr_index]
            self.m_total_word_so_far = word_so_far + self.m_word[self.m_curr_index]
        if self.m_curr_index + 1 < len(self.m_word):   # next up letter is within word
            if self.m_word[self.m_curr_index+1] not in self.m_children_nodes:
                self.m_children_nodes[self.m_word[self.m_curr_index+1]]=Node()
                self.m_children_nodes[self.m_word[self.m_curr_index+1]].add_word( \
                    self.m_word, self.m_total_word_so_far, self.m_curr_index + 1)
            else:
                self.m_children_nodes[self.m_word[self.m_curr_index+1]].add_word( \
                    self.m_word, self.m_total_word_so_far, self.m_curr_index + 1)                      
                                      
                      
    def auto_complete_word(self, str):
        if len(str)> 0 and str[0] in self.m_children_nodes:
            self.m_children_nodes[str[0]].auto_complete_word(str[1:])
        if len(str) == 0:
            print("auto complete :")
            self.print_tree()

    def print_tree(self):
        if self:
            if len(self.m_children_nodes)==0:
                    print('word : ', self.m_total_word_so_far)
            else:
                for i in self.m_children_nodes:
                    self.m_children_nodes[i].print_tree()


#client code

words = ['den', 'dear', 'do', 'disco']

root= Node()
for word in words:
    root.add_word(word)

root.print_tree()

print('de :')
root.auto_complete_word('de')

for i in range(5):
    mystr = input('enter letters to autocomplete : ')
    root.auto_complete_word(mystr)


