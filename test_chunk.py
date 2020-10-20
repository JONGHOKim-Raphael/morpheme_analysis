import chunk
import logging


logging.basicConfig(level=logging.DEBUG)

sentence = u'만 6세 이하의 초등학교 취학 전 자녀를 양육하기 위해서는'
chunk.chunk_sentence(sentence)
