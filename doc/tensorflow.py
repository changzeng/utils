# 初始化全局变量
sess.run(tf.global_variables_initializer())

# 获得变量的两种方式
# 两种获取变量方法的对比。Variable：创建变量。get_variable：获得一个变量，如果不存在则创建
tf.Variable(tf.random_normal([height, width]))
tf.get_variable(name='weights', shape=[784, 200], initializer=tf.random_normal_initializer())

# name_scope与variable_scope的区别
# name_scope的前缀只会加在以Variable方式创建的变量前
# variable_scope的前缀会加在Variable和get_variable创建的变量前

# 保存模型
saver = tf.train.Saver(tf.global_variables(), max_to_keep=1)
# sess: 会话, model_prefix: 模型名前缀(总共生成三个文件), global_step: 步数
saver.save(sess, model_prefix, global_step=step)

# 保存图中的变量
tf.add_to_collection("accu", self.accu)

# 加载图
tf.train.import_meta_graph(os.path.join(model_path, meta_name))

# 还原会话
saver.restore(sess, tf.train.latest_checkpoint(model_path))

# 加载图中的变量
tf.get_collection("predictions")[0]
graph.get_collection("recall")[0]

# 获得tensor的形状
tf.shape(tensor)

# 限制使用GPU的比例
config.gpu_options.per_process_gpu_memory_fraction = 0.9

