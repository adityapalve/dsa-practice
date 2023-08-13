
ds = {
	
}


st = set(x for e in ds for x in e)
print(st)



!pip install git+https://github.com/rwalk/gsdmm.git

from gsdmm import MovieGroupProcess

texts = B_clean["gram_model_tweets"]

mgp = MovieGroupProcess(K=15, alpha=0.01, beta=0.01, n_iters=500)

vocab = set(x for tweet in texts for x in tweet)
n_terms = len(vocab)
model = mgp.fit(texts, n_terms)

def top_words(cluster_word_distribution, top_cluster, values):
    for cluster in top_cluster:
        sort_dicts =sorted(mgp.cluster_word_distribution[cluster].items(), key=lambda k: k[1], reverse=True)[:values]
        print("\nCluster %s : %s"%(cluster,sort_dicts))


doc_count = np.array(mgp.cluster_doc_count)
print('Number of documents per topic :', doc_count)

# topics sorted by the number of document they are allocated to
top_index = doc_count.argsort()[-10:][::-1]
print('\nMost important clusters (by number of docs inside):', top_index)
# show the top 5 words in term frequency for each cluster 
top_words(mgp.cluster_word_distribution, top_index, 10)