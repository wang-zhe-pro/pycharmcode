from selenium import webdriver
import time
import re
import jieba
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl




class Guidian(object):

    def __init__(self):
        # 开始时的url
        self.start_url = "http://www.gliet.edu.cn/xwzx/gdxw.htm"
        # 实例化一个Chrome对象

        self.driver = webdriver.Chrome()
        #设置等待
        self.driver.implicitly_wait(10)
        # 用来写csv文件的标题
        self.start_csv = True

    def get_content(self):




        while True:
            texts = []
            dates = []
            # 此处是获取网页页面的新闻标题和日期
            lists =self.driver.find_elements_by_xpath('//table[@class="table-set"]//tbody//tr')
            for list in lists:

                if list.find_element_by_xpath('.//a[@target="_blank"]').text == "":
                    continue
                text = list.find_element_by_xpath('.//a[@target="_blank"]').text
                texts.append(text)
                date = list.find_element_by_xpath('.//td[1]').text
                dates.append(date)
            self.save_csv(texts,dates)
            #此处则是判断是否最后一页
            try:
                next_page = self.driver.find_element_by_link_text('下页')

                next_page.click()   #自动点击下一页

            except:
                print("到尾页了，爬取完毕")
                self.driver.quit()
                break





    def save_csv(self, texts,dates):


        with open('./桂电新闻demo.csv', 'a', encoding='utf-8') as f:
            if self.start_csv:
                f.write("时间,标题\n")
                self.start_csv = False
            # 将字符串写入csv文件
            for date,text in zip(dates,texts):
                str=date+','+text
                f.write(str)
                f.write('\n')




    def plot(self):
        mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像中文显示为方块的问题
        txt = open("桂电新闻.csv", "r", encoding="utf8").read()
        words = jieba.lcut(txt)  # 使用精确模式对文本进行分词
        counts = {}  # 通过键值对的形式存储词语及其出现的次数

        for word in words:
            if len(word) == 1 or word.isdigit() == True:  # 单个词语不计算在内
                continue
            else:
                counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1

        items = list(counts.items())  # 将键值对转换成列表
        items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序

        list_word = []  # 保存新闻热词

        list_count = []  # 保存出现次数

        for i in range(10):
            word, count = items[i]
            list_word.append(word)
            list_count.append(count)
        tuple_word = tuple(list_word)
        # 此处设置plt的初始参数来绘图

        y_pos = (range(10))
        plt.bar(y_pos, list_count, align='center', alpha=0.8)
        plt.xticks(y_pos, tuple_word)
        plt.ylabel(u'出现次数')
        plt.title(u'桂电新闻十大热词')

        plt.show()
        plt.figure(figsize=(6, 9))
        # 定义饼状图的标签，标签是列表
        labels_year = [str(x) for x in range(2017, 2022)]
        # 每个标签占多大，会自动去算百分比
        sizes = []
        txt = open("桂电新闻demo.csv", "r", encoding="utf8").read()
        for year in labels_year:
            count = txt.count(str(year))
            sizes.append(count)

        colors = ['darkcyan', 'yellowgreen', 'lightskyblue']
        # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
        explode = (0.01,) * len(sizes)


        patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels_year, colors=colors,
                                          labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                          startangle=90, pctdistance=0.6)

        # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
        # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
        # shadow，饼是否有阴影
        # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
        # pctdistance，百分比的text离圆心的距离
        # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

        # 改变文本的大小
        # 方法是把每一个text遍历。调用set_size方法设置它的属性
        for t in l_text:
            t.set_size = (30)
        for t in p_text:
            t.set_size = (20)
        # 设置x，y轴刻度一致，这样饼图才能是圆的
        plt.axis('equal')
        plt.legend()
        plt.show()


    def run(self):
        # 启动chrome并定位到相应页面
        self.driver.get(self.start_url)
        self.get_content()
        self.plot()






if __name__ == '__main__':
    guidian_spider = Guidian()
    guidian_spider.run()