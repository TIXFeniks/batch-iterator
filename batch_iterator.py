import numpy as np

def iterate_minibatches(*to_split, **kwargs):
    """
        generates batches from the data, passed as first arguments
        
        arguments:
        -batchsize: the number of rows in a batch
        -shuffle: if True shuffles the data and yields shuffled batches
    """
    batchsize=1
    shuffle=False
    if 'batchsize' in kwargs:
        batchsize = kwargs['batchsize']
    
    if 'shuffle' in kwargs:
        shuffle = kwargs['shuffle']

    res = [np.array(x) for x in to_split]
    size = res[0].shape[0]
    for x in res:
        assert x.shape[0] == size
    if shuffle:
        indices = np.arange(size)
        np.random.shuffle(indices)
    for start_idx in range(0, size, batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield [x[excerpt] for x in res]
