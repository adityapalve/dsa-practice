def get_topics_lists(model, top_clusters, n_words):
    topics = []
    
    for cluster in top_clusters:
        sorted_dict = sorted(model.cluster_word_distribution[cluster].items(), key=lambda k: k[1], reverse=True)[:n_words]
        topic = []
        for k,v in sorted_dict:
            topic.append(k)
        
        topics.append(topic)
        return topics
        
topics = get_topics_lists(mgp, top_index,15)
cm_gsdmm = CoherenceModel(topics=topics, dictionary=dictionary, 
                          corpus=corpus,
                          texts=texts[:1000],
                          coherence='c_v')

coherencemodel_umass = CoherenceModel(topics=topics, corpus=corpus, dictionary=dictionary, texts=texts[:1000], coherence='u_mass')
# get coherence value
# perplexity_score = np.exp2(-model.log_perplexity(corpus))
coherence_gsdmm = cm_gsdmm.get_coherence()
ch_um = coherencemodel_umass.get_coherence()
# coherence_values_cv.append(coherence_gsdmm)

print("cv:", coherence_gsdmm)
print("umass:", ch_um)