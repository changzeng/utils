#	显示行号
set	nu
set	number

#	关闭行号
set	nonu
set	nonumber

#	替换
:1,$:s/aaa/bbb/g

# 打开文件树侧边栏
:NERDTreeToggle

# 删除包含特定支付串的行
:g/pattern/d

# 设置水平制表符为4空格
set ts=4