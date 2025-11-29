import numpy as np
from traj.dist import calc_distances_mvo, calc_frechet_mvo


## Lists
base_list = [1, 2, 3]
comps_list = [[1, 2, 3], [4, 5, 6], [99, 99, 99]]
result = calc_distances_mvo(base_vector=base_list, comparison_vectors=comps_list, distance_metric="cosine")
print(result)


base_list = [1, 2, 3]
comps_list = [[1, 2, 3], [4, 5, 6], [99, 99, 99]]
result = calc_frechet_mvo(base_vector=base_list, comparison_vectors=comps_list)
print(result)

## Arrays
base_array = np.array([1, 2, 3])
comps_array = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([99, 99, 99])]
result = calc_distances_mvo(base_vector=base_list, comparison_vectors=comps_list, distance_metric="cosine")
print(result)

base_array = np.array([1, 2, 3])
comps_array = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([99, 99, 99])]
result = calc_frechet_mvo(base_vector=base_list, comparison_vectors=comps_list)
print(result)