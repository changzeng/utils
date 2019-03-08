# 初始化全局变量
sess.run(tf.global_variables_initializer())

# 获得变量的两种方式
# 两种获取变量方法的对比。Variable：创建变量。get_variable：获得一个变量，如果不存在则创建
tf.Variable(tf.random_normal([height, width]))
tf.get_variable(name='weights', shape=[784, 200], initializer=tf.random_normal_initializer())

# name_scope与variable_scope的区别
# name_scope的前缀只会加在以Variable方式创建的变量前
# variable_scope的前缀会加在Variable和get_variable创建的变量前
