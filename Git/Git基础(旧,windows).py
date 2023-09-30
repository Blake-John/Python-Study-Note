# Git GUI：Git提供的图形界面工具
# Git Bash：Git提供的命令行工具
# 当安装Git后首先要做的事情是设置用户名称和email地址。这是非常重要的，因为每次Git提交都会使用
# 该用户信息

# 1——基本配置
# 1. 打开Git Bash
# 2. 设置用户信息
# git config --global user.name "name"
# git config --global user.email "email"
# 查看配置信息
# git config --global user.name
# git config --global user.email

# 1.1——为常用指令配置别名（可选）
# 有些常用的指令参数非常多，每次都要输入好多参数，我们可以使用别名。
# 1. 打开用户目录，创建 .bashrc 文件
# 部分windows系统不允许用户创建点号开头的文件，可以打开gitBash,执行 touch ~/.bashrc
# 2. 在 .bashrc 文件中输入如下内容：
# #用于输出git提交日志
# alias git-log='git log --pretty=oneline --all --graph --abbrev-commit'
# #用于输出当前目录所有文件及基本信息
# alias ll='ls -al'
# 3. 打开gitBash，执行 source ~/.bashrc

# 2——解决GitBash乱码问题
# 1. 打开GitBash执行下面命令
#    git config --global core.quotepath false
# 2. ${git_home}/etc/bash.bashrc 文件最后加入下面两行
#    export LANG="zh_CN.UTF-8"
#    export LC_ALL="zh_CN.UTF-8"

# 3——获取本地仓库
# 要使用Git对我们的代码进行版本控制，首先需要获得本地仓库
# 1）在电脑的任意位置创建一个空目录（例如test）作为我们的本地Git仓库
# 2）进入这个目录中，点击右键打开Git bash窗口
# 3）执行命令git init
# 4）如果创建成功后可在文件夹下看到隐藏的.git目录。

# 4——基础操作指令
# Git工作目录下对于文件的修改(增加、删除、更新)会存在几个状态，这些修改的状态会随着我们执行Git
# 的命令而发生变化。
# *本章节主要讲解如何使用命令来控制这些状态之间的转换：
#  1.git add (工作区 --> 暂存区)
#  2.git commit (暂存区 --> 本地仓库)

# *查看修改的状态（status）
#  作用：查看的修改的状态（暂存区、工作区）
#  命令形式：git status

# *添加工作区到暂存区(add)
#  作用：添加工作区一个或多个文件的修改到暂存区
#  命令形式：git add 单个文件名|通配符
#  将所有修改加入暂存区：git add .

# *提交暂存区到本地仓库(commit)
#  作用：提交暂存区内容到本地仓库的当前分支
#  命令形式：git commit -m '注释内容'

# *查看提交日志(log)
# 作用:查看提交记录
# 命令形式：git log [option]
#  *options
#    --all 显示所有分支
#    --pretty=oneline 将提交信息显示为一行
#    --abbrev-commit 使得输出的commitId更简短
#    --graph 以图的形式显示

# *版本回退
# 作用：版本切换
# 命令形式：git reset --hard commitID
#   commitID 可以使用 git-log 或 git log 指令查看
# 如何查看已经删除的记录？
#   git reflog
#   这个指令可以看到已经删除的提交记录

