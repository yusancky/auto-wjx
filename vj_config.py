URL = 'https://ks.wjx.top/vj/wFlPipW.aspx' # 问卷的 URL
t_num = 2 # 问卷的题目总数
sum = [0,0,3,(5)] # sum[0] 用于占位，其他的 0 表示调用函数 posr(t) 完成第 t 题，正数表示第 t 题共有 ans[t] 个选项，元组表示多选题的选项数量
ans = [0,0,1,[2,3]]  # ans[0] 用于占位，正数表示第 t 题选择第 ans[t] 个选项

def post(t):
  '''
  在 sum[t] 为 0 时运行，主要用于执行非选择题及未加入的多选题。
  '''
  if t == 1:
    choose_none()
    ctr.type('测试人员')