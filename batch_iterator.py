import numpy as np

def iterate_minibatches(*to_split, batchsize=1, shuffle=False):
    res = [np.array(x) for x in to_split]
    for x in res:
        assert x.shape[0] == res[0].shape[0]
    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs), batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield [x[excerpt] for x in res]
