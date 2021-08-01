import logging
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)  #设置全局，等同于logger.setLevel(10)  可传0,10,20,30,40,50
handler1 = logging.StreamHandler()#StreamHandler用于输出到控制台
handler1.setLevel(30)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
logger.addHandler(handler1)

#将日志输出到文件，直接在当前目录生成一个test.log的文件,a表示追加，一直记录在这个文件的后面
handler2 =logging.FileHandler('./test.log', 'a', encoding='utf-8') #encoding='utf-8'日志文件输出中不乱码
handler2.setLevel(10)  #可以单独设置logging级别，局部使用
handler2.setFormatter(formatter)
logger.addHandler(handler2)

logger.info('hello')
