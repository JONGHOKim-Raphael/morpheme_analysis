import konlpy
import nltk
from tqdm import tqdm
import logging


logger = logging.getLogger(__name__)

def chunk_sentence(sentence) -> nltk.tree.Tree:
    # POS tag a sentence
    ## NOTE tag: Kkma, Komoran, Hannanum, Okt, Mecab
    tag = konlpy.tag.Kkma()
    words = tag.pos(sentence)

    # Define a chunk grammar, or chunking rules, then chunk
    grammar = """
    NP: {<N.*>*<Suffix>?}   # Noun phrase
    VP: {<V.*>*}            # Verb phrase
    AP: {<A.*>*}            # Adjective phrase
    """
    parser = nltk.RegexpParser(grammar)
    chunks = parser.parse(words)

    logger.debug("# Chunking with " + tag.__class__.__name__)
    logger.debug("# Sentence: " + sentence)
    logger.debug("# Print whole tree")
    logger.debug("\n" + chunks.pformat())
    logger.debug("# Print noun phrases only")

    for subtree in chunks.subtrees():
        if subtree.label()=='NP':
            logger.debug(' '.join((e[0] for e in list(subtree))))
            logger.debug(subtree.pformat())

    return chunks


def chunk_sentences(sentences) -> [nltk.tree.Tree]:
    trees = []
    for sentence in tqdm(iterable=sentences, desc="chunking sentences..."):
        trees.append(chunk_sentence(sentence))

    return trees
