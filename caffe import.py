    import numpy as npImagecaffe.set_mode_cpu()= 
    caffe.Net('/home/macbook-pro-amir/nn/traffic_signs/train_val_conv.prototxt', 
    '/home/macbook-pro-amir/nn/snapshots/conv/1/snapshot_iter_2000000.caffemodel', 
    caffe.TEST)("blobs {}\nparams {}".format(net.blobs.keys(), 
    net.params.keys()))"params['conv1']" + 
    str(net.params['conv1'])"params['conv1'][0].data.shape" + 
    str(net.params['conv1'][0].data.shape)"params['conv1'][1].data.shape" + 
    str(net.params['conv1'][1].data.shape)"params['conv2'][0].data.shape" + 
    str(net.params['conv2'][0].data.shape)"params['conv2'][1].data.shape" + 
    str(net.params['conv2'][1].data.shape)"params['fc6'][0].data.shape" + 
    str(net.params['fc6'][0].data.shape)"params['fc7'][0].data.shape" + 
    str(net.params['fc7'][0].data.shape)"params['fc8'][0].data.shape" + 
    str(net.params['fc8'][0].data.shape)= 
    np.array(Image.open('/home/macbook-pro-amir/nn/00035_00007_00001.JPEG'))_input = 
    im[np.newaxis, np.newaxis,:].blobs['data'].reshape(*im_input.shape).blobs['data'].data[...] = 
    im_input.forward()"blobs['data'].data.shape " + 
    str(net.blobs['data'].data.shape)"blobs['label'].data.shape " + 
    str(net.blobs['label'].data.shape)"blobs['conv1'].data.shape " + 
    str(net.blobs['conv1'].data.shape)"blobs['pool1'].data.shape " + 
    str(net.blobs['pool1'].data.shape)"blobs['norm1'].data.shape " + 
    str(net.blobs['norm1'].data.shape)"blobs['conv2'].data.shape " + 
    str(net.blobs['conv2'].data.shape)"blobs['pool2'].data.shape " + 
    str(net.blobs['pool2'].data.shape)"blobs['norm2'].data.shape " + 
    str(net.blobs['norm2'].data.shape)_npy_for_mean.py 

    import 
    numpycaffe=caffe.io.caffe_pb2.BlobProto()=open('/home/macbook-pro-amir/nn/traffic_signs/imagenet_mean_train_new_large_gec.binaryproto','rb') 
    file.read().ParseFromString(data)=a.data=numpy.asarray(means)_reshaped = 
    means.reshape(3,60,60).save('/home/macbook-pro-amir/nn/traffic_signs/imagenet_mean_train_new_large_gec2.npy',
    means_reshaped)

