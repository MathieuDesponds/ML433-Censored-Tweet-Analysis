# Best params used for France and Russian Federation 
params_F = { 
    'UMAP' : {
        'metric' : 'cosine', 
        'n_neighbors' : 15, 
        'n_components' : 20, 
        'min_dist' : 0.3, 
        'low_memory' : False,
        'random_state': 8
    },
    'HDBSCAN': {
        'min_cluster_size':15,
        'min_samples': 1,
        'cluster_selection_epsilon': 0.6,
        'metric': 'euclidean',                      
        'cluster_selection_method': 'eom',
        'prediction_data': True}
}

# Best params used for India, Germany and Turkey
params_I = {
    'UMAP' : {
        'metric' : 'cosine', 
        'n_neighbors' : 15, 
        'n_components' : 40, 
        'min_dist' : 0.1, 
        'low_memory' : False,
        'random_state': 8
    },
    'HDBSCAN': {
        'min_cluster_size':15,
        'min_samples': 1,
        'cluster_selection_epsilon': 0.3,
        'metric': 'euclidean',                      
        'cluster_selection_method': 'eom',
        'prediction_data': True}
}