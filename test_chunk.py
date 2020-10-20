import chunk
import logging


logging.basicConfig(level=logging.DEBUG,
                    handlers=[
                        #logging.StreamHandler(),
                        logging.FileHandler("_test_chunk.log")
                    ])


# Test chunk.chunk_sentence()
logging.debug("# Start testing chunk.chunk_sentence()...")
sentence = u'만 6세 이하의 초등학교 취학 전 자녀를 양육하기 위해서는'
chunk.chunk_sentence(sentence)
logging.debug("# Finished testing chunk.chunk_sentence()")


# Test chunk.chunk_sentences()
logging.debug("# Start testing chunk.chunk_sentences()...")
test_file = open('message.tsv', 'r')
sentences = test_file.readlines()
chunk.chunk_sentences(sentences)
logging.debug("# Finished testing chunk.chunk_sentences()")
