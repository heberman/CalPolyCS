"""Class: SearchEngine
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""

from hashtable_quadratic import *
import os
import math

def main():
    path = input("Input path to directory: ")
    stop_table = HashTableQuadratic()
    stopwords = import_stopwords('stop_words.txt', stop_table)
    main_engine = SearchEngine(path, stopwords)
    query = input("Input a search query: ")
    while query != ':q':
        while query[0:2] != 's:':
            if query == ':q':
                quit()
            print("To search, prepend the query with 's:'. Otherwise, type ':q'.")
            query = input("Input a search query: ")
        query = query[2:]
        results = main_engine.search(query)
        for result in results:
            print(result[0])
        print('')
        query = input("Input a search query: ")
    quit()


class SearchEngine:
    """search engine for documents and accounts for term frequency
    Attributes:
        directory (str): name of directory
        stopwords (HashTableQuadratic): a hash table containing stopwords
        doc_length (HashTableQuadratic): a hash table containing the total number of words in each document
        term_freqs (HashTableQuadratic) : a hash table of hash tables for each term
    """
    def __init__(self, directory, stop):
        self.doc_length = HashTableQuadratic()
        self.term_freqs = HashTableQuadratic()
        self.stopwords = stop
        self.index_files(directory)

    def read_file(self, infile):
        """A helper function to read a file
        Args:
            infile (str) : the path to a file
        Returns:
            (list) : a list of str read from a file
        """
        lines = []
        with open(infile, 'r') as file:
            for line in file:
                lines.append(line)
        return lines

    def parse_words(self, lines):
        """splits strings into words by spaces.
        Args:
            lines (list) : a list of strings
        Returns:
            list : a list of words
        """
        words = []
        bad_chars = ['\n', '(', ')', '[', ']', '{', '}', '.', ',', '?', '!']
        for item in lines:
            line = item.split()
            for word in line:
                for val in bad_chars:
                    word = word.replace(val, '')
                word = word.lower()
                words.append(word)
        return self.exclude_stopwords(words)

    def exclude_stopwords(self, terms):
        """exclude stopwords from the list of terms
        Args:
            terms (list) : list of terms
        Returns:
            list : a list of str with stopwords removed
        """
        stopless = []
        for item in terms:
            if item not in self.stopwords:
                stopless.append(item)
        return stopless

    def count_words(self, file_path_name, words):
        """count words in a file and store the frequency of each
        Args:
             file_path_name (str) : the file name
             words (list) : a list of words
        Returns:
            -
        """
        for word in words:
            if word not in self.term_freqs:
                self.term_freqs[word] = HashTableQuadratic()
                self.term_freqs[word][file_path_name] = 1
            else:
                if file_path_name in self.term_freqs[word]:
                    self.term_freqs[word][file_path_name] += 1
                else:
                    self.term_freqs[word][file_path_name] = 1
        self.doc_length[file_path_name] = len(words)

    def index_files(self, directory):
        """index all text files in a given directory
        Args:
            directory (str) : the path of a directory
        Returns:
            -
        """
        files = os.listdir(directory)
        for i in range(len(files)):
            files[i] = os.path.join(directory, files[i])
        for item in files:
            if not os.path.isfile(item):
                files.remove(item)
            else:
                if os.path.splitext(item)[1] != '.txt':
                    files.remove(item)
        for item in files:
            lines = self.read_file(item)
            words = self.parse_words(lines)
            self.count_words(item, words)

    def get_wf(self, tf):
        """computes the weighted frequency
        Args:
            tf (float) : term frequency
        Returns:
            float : the weighted frequency
        """
        if tf > 0:
            wf = 1 + math.log(tf)
        else:
            wf = 0
        return wf

    def get_scores(self, terms):
        """creates a list of scores for each file in corpus
        Args:
            terms (list) : a list of str
        Returns:
            list : a list of tuples, each containing the file_path_name and its relevancy score.
        """
        scores = HashTableQuadratic()
        for item in terms:
            file_table = self.term_freqs[item]
            for file in file_table.keys():
                if file not in scores:
                    scores[file] = self.get_wf(file_table[file])
                else:
                    scores[file] += self.get_wf(file_table[file])
        for file in scores.keys():
            scores[file] /= self.doc_length[file]
            scores[file] = round(scores[file], 3)
        scores_list = []
        for key in scores.keys():
            if scores[key] > 0:
                scores_list.append((key, scores[key]))
        return scores_list

    def rank(self, scores):
        """ranks files in the descending order of relevancy
        Args:
            scores(list) : a list of tuples: (file_path_name, score)
        Returns:
            list : a list of tuples: (file_path_name, score) sorted in descending order of relevancy
        """
        for i in range(1, len(scores)):
            score = scores[i][1]
            new_score = scores[i]
            index = i - 1
            while index >= 0 and score > scores[index][1]:
                scores[index + 1] = scores[index]
                index -= 1
            scores[index + 1] = new_score
        return scores

    def search(self, query):
        """ search for the query terms in files.
        Args:
            query (str) : query input: e.g. “computer science”
        Returns:
            list :  a list of tuples: (file_path_name, score) sorted in descending order of relevancy
        """
        words = self.parse_words([query])
        scores = self.get_scores(words)
        return self.rank(scores)


if __name__ == '__main__':
    main()
