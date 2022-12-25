from auto_wjx_utils import *
from vj_config import *

def choose_none(a = 1):
  for _ in range(a):
    ctr.type('\t')

def choose_ans(a,s = None):
  '''
  用于单选题，表示在有 a 个选项的单选题中选择第 k 项
  '''
  if s is none:
    s = a
  if s == 0:
    choose_none(a)
  chooses_none(a)
  ctr.type('\n')
  chooses_none(s - a)

def chooses_ans(a,m,s):
  '''
  用于多选题，表示在有 a 个选项、m 个答案的多选题中选择
  '''
  choose_ans(s[0])
  for i in range(1,m):
    choose_ans(s[i] - s[i - 1])
  chooses_none(a - s[m - 1])

from selenium import webdriver

op = webdriver.EdgeOptions()
op.add_experimental_option('excludeSwitches', ['enable-automation'])
op.add_experimental_option('useAutomationExtension', False)
global browser
browser = webdriver.Edge(options = op)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
browser.get(URL)

from re import findall
from time import sleep

sleep(0.5)
ctr.type('\n') # 按下 Microsoft Edge 的“明白”
sleep(0.2)
choose_none() # 跳过问卷星的二维码

for t in range(1,t_num + 1):
  if sum[t] == 0:
    posr(t)
    continue
  findall_results = findall(r'label for="q(\d+)_(\d+)"',browser.page_source)
  cnt = 0
  for result in findall_results:
    if not isinstance(sum[t],tuple):
      # 单选题
      if result[0] == str(t):
        cnt += 1
        if result[1] == str(ans[t]):
          choose_ans(cnt,sum[t])
    else:
      # 多选题