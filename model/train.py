import numpy as np
import tensorflow as tf
import model
import util
import dataset
import time
import os
import progressbar
import time

# ### Setting params, dirs, and loading data

print 'Setting params, dirs, and loading data'
# In[2]:
try:
    paths = ['./out/', './params']
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
                    
    data = dataset.read()
    batch_size = 100
    learning_rate = 0.0001
    beta1 = 0.5
    z_size = 51200
    save_interval = 1



    # ###  Creating Placeholders

    # In[3]:

    print 'Creating Placeholders...'

    x = tf.placeholder(tf.float32, [batch_size, 32, 32, 32, 1])
    z = tf.placeholder(tf.float32, [batch_size, z_size])
    train = tf.placeholder(tf.bool)


    # ### Create Generator and Discriminator Object
    # #### Setting up labels, loss functions, other parameters

    # In[4]:

    print 'Create Generator and Discriminator...'
    G = model.Generator(z_size)
    D = model.Discriminator()
    x_ = G(z)
    y_ = D(x_, train)

    y = D(x, train)

    print 'Setting up labels, loss functions, other parameters'
    label_real = np.zeros([batch_size, 2], dtype=np.float32)
    label_fake = np.zeros([batch_size, 2], dtype=np.float32)
    label_real[:, 0] = 1
    label_fake[:, 1] = 1

    loss_G = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_, tf.constant(label_real)))
    loss_D = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_, tf.constant(label_fake)))
    loss_D += tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, tf.constant(label_real)))

    var_G = [v for v in tf.trainable_variables() if 'g_' in v.name]
    var_D = [v for v in tf.trainable_variables() if 'd_' in v.name]

    opt_G = tf.train.AdamOptimizer(learning_rate, beta1).minimize(loss_G, var_list=var_G)
    opt_D = tf.train.AdamOptimizer(learning_rate, beta1).minimize(loss_D, var_list=var_D)

    saver = tf.train.Saver()


    # ### Setting up Progressbar

    # In[ ]:

    print 'Setting up Progressbar'
    progress = progressbar.ProgressBar()


    # ### Running Voxel-dcgan

    # In[ ]:

    print 'Running Voxel-dcgan'
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True

    with tf.Session(config=config) as sess:
        
        sess.run(tf.initialize_all_variables(), feed_dict={train:True})
        total_batch = data.train.num_examples / batch_size

        for epoch in progress(xrange(1, 125)):  # Repeat this process 50 times

            for i in xrange(total_batch):
                voxels = np.expand_dims(data.train.next_batch(batch_size), 4)
                batch_z = np.random.uniform(-1, 1, [batch_size, z_size]).astype(np.float32)

                sess.run(opt_G, feed_dict={z:batch_z, train:True})
                sess.run(opt_D, feed_dict={x:voxels, z:batch_z, train:True})

                with open("out/loss.csv", 'a+') as f:
                    f.write('Current Time:' + time.strftime("%c") + " ")
                    batch_loss_G = sess.run(loss_G, feed_dict={z:batch_z, train:False})
                    batch_loss_D = sess.run(loss_D, feed_dict={x:voxels, z:batch_z, train:False})
                    msg = "{0}, {1}, {2:.8f}, {3:.8f}".format(epoch, i, batch_loss_G, batch_loss_D)
                    f.write(msg+'\n')
                    #print msg

            batch_z = np.random.uniform(-1, 1, [batch_size, z_size]).astype(np.float32)
            voxels = sess.run(x_, feed_dict={z:batch_z})

            for j, v in enumerate(voxels[:5]):
                v = v.reshape([32, 32, 32]) > 0

                util.save_binvox(v, "out/epoch{0}-{1}.binvox".format(epoch, j))

            if epoch % save_interval == 0:
                saver.save(sess, "params/epoch{0}.ckpt".format(epoch))

except:
    pass

