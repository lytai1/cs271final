from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
  
warnings.filterwarnings(action = 'ignore') 
  
import gensim 
from gensim.models import Word2Vec 

def convert_w2v(fileName):
    print("Generating word2vec for " + fileName)
    f = open(fileName, "r")
    embedding_matrix = []
    for x in f:
        data = x.split(",")
        data = data[:-1]
        # print(data)
        model1 = gensim.models.Word2Vec([data], min_count = 0, size = 2, window = 7, sorted_vocab=True) 
        embedding_vector = []
        for i in range(256):
            if str(i) in model1.wv.vocab:
                embedding_vector.extend(model1.wv[str(i)])
            else:
                embedding_vector.extend([0,0])
        embedding_matrix.append(embedding_vector)
    f.close()
    return embedding_matrix
def write_file(fileName, embedding_matrix):
    print("writing " + fileName)
    f = open(fileName, "w")
    for vector in embedding_matrix:
        for v in vector:
            f.write(str(v) + ",")
        f.write("\n")
    f.close()
def main():
    fileName = "../processed_data/challenge_100.csv"
    embedding_matrix = convert_w2v(fileName)
    fileName = "../processed_data/challenge_100_vec.csv"
    write_file(fileName, embedding_matrix)

    fileName = "../processed_data/label/BHO.csv"
    embedding_matrix = convert_w2v(fileName)
    fileName = "../processed_data/label/BHO_vec.csv"
    write_file(fileName, embedding_matrix)

    fileName = "../processed_data/label/CeeInject.csv"
    embedding_matrix = convert_w2v(fileName)
    fileName = "../processed_data/label/CeeInject_vec.csv"
    write_file(fileName, embedding_matrix)

    fileName = "../processed_data/label/FakeRean.csv"
    embedding_matrix = convert_w2v(fileName)
    fileName = "../processed_data/label/FakeRean_vec.csv"
    write_file(fileName, embedding_matrix)

    fileName = "../processed_data/label/OnLineGames.csv"
    embedding_matrix = convert_w2v(fileName)
    fileName = "../processed_data/label/OnLineGames_vec.csv"
    write_file(fileName, embedding_matrix)

    fileName = "../processed_data/label/Renos.csv"
    embedding_matrix = convert_w2v(fileName)
    fileName = "../processed_data/label/Renos_vec.csv"
    write_file(fileName, embedding_matrix)

    fileName = "../processed_data/label/Vobfus.csv"
    embedding_matrix = convert_w2v(fileName)
    fileName = "../processed_data/label/Vobfus_vec.csv"
    write_file(fileName, embedding_matrix)

    fileName = "../processed_data/label/Winwebsec.csv"
    embedding_matrix = convert_w2v(fileName)
    fileName = "../processed_data/label/Winwebsec_vec.csv"
    write_file(fileName, embedding_matrix)
main()