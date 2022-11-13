URL = 'https://ks.wjx.top/vj/wFlPipW.aspx' # 问卷的 URL
t_num = 2 # 问卷的题目总数
sum = [0,0,3] # sum[0] 用于占位，其他的 0 表示调用函数 posr(t) 完成第 t 题，正数表示第 t 题共有 ans[t] 个选项
ans = [0,0,1]  # ans[0] 用于占位，正数表示第 t 题选择第 ans[t] 个选项

def posr(t):
  '''
  在 sum[t] 为 0 时运行，主要用于执行非选择题及未加入的多选题。
  '''
  if t == 1:
    import pynput
    ctr = pynput.keyboard.Controller()
    ctr.type('\t测试人员')

def choose_ans(a,s):
  '''
  用于单选题，表示在有 a 个选项的单选题中选择第 k 项，未来也将用于多选题
  '''
  import pynput
  ctr = pynput.keyboard.Controller()
  for _ in range(a):
    ctr.type('\t')
  ctr.type('\n')
  for _ in range(s - a):
    ctr.type('\t')

from selenium import webdriver
op = webdriver.EdgeOptions()
op.add_experimental_option('excludeSwitches', ['enable-automation'])
op.add_experimental_option('useAutomationExtension', False)
global browser
browser = webdriver.Edge(options = op)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
browser.get(URL)

from re import findall
findall_results = findall(r'label for="q(\d+)_(\d+)"',browser.page_source)

from time import sleep
import pynput
ctr = pynput.keyboard.Controller()
sleep(0.5)
ctr.type('\n') # 按下 Microsoft Edge 的“明白”
sleep(0.2)
ctr.type('\t') # 跳过问卷星的二维码

for t in range(1,t_num + 1):
  if sum[t] == 0:
    posr(t)
    continue
  cnt = 0
  for result in findall_results:
    if result[0] == str(t):
      cnt += 1
      if result[1] == str(ans[t]):
        choose_ans(cnt,sum[t])