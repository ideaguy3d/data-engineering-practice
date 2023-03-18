"""
just a practice file from a course I'm studying on Udemy

can be run from the command line with:
$ spark-submit u_com_read_txt.py
"""
from pyspark import SparkConf, SparkContext

sample_weather_file = '/Users/juliushernandez/Documents/GitHub/__dc_pipelines__/evergreen/evergreen_custom_payloads_sample_data/payload.com.apple.hai.Evergreen.Weather.json'
nums_file = 'data/nums.txt'
txt_file = 'data/text.txt'
mango_txt = 'data/mango.txt'
conf = SparkConf().setAppName('PySparkPractice')
sc = SparkContext(conf=conf).getOrCreate()

def txt_split(s):
    s_list = s.split(' ')
    l2 = []
    for v in s_list:
        l2.append(int(v) * 2)
    return l2

def letter_count(s):
    words = s.split(' ')
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))
    return word_lengths

def practice1():
    rdd_text = sc.textFile(nums_file)
    l_text = rdd_text.collect()
    print(l_text)

    rdd_text2 = rdd_text.map(txt_split)
    l_text2 = rdd_text2.collect()
    print(l_text2)

    rdd_words = sc.textFile(txt_file)
    print('\n--> getting lengths of each word for\n', rdd_words.collect(), '\n')
    l_words = rdd_words.map(letter_count)
    l_words = l_words.collect()
    print('\nlengths =\n', l_words)

def practice_map():
    rdd_words = sc.textFile(txt_file)

    rdd_pipe_words_map = rdd_words.map(lambda s: [len(s) for s in s.split(' ')])
    print('\n_> length of all the words\n', rdd_pipe_words_map.collect())

    rdd_pipe_words_flat_map = rdd_words.flatMap(lambda s: s.split(' '))
    rdd_pipe_words_flat_map_len = rdd_words.flatMap(lambda s: [len(s) for s in s.split(' ')])
    print('\n_> Flat Map version\n', rdd_pipe_words_flat_map.collect(),
          '\n', rdd_pipe_words_flat_map_len.collect())

def practice_filter():
    rdd_mango = sc.textFile(mango_txt)
    def filter_ac(s):
        if s[0] in ['a', 'c']:
            return False
        return True

    r_p_mango = rdd_mango.filter(filter_ac)
    print('\n_> filtered result:\n', r_p_mango.collect())

def practice_distinct():
    rdd_nums = sc.textFile(nums_file)
    r_p_nums = rdd_nums.flatMap(lambda s: s.split(' '))
    print('\n_> flat map:\n', r_p_nums.collect())

def main():
    # practice1()
    # practice_map()
    # practice_filter()
    practice_distinct()
    b12 = 1

if __name__ == '__main__':
    main()
    print('\n\n\t\t _> Spark Job complete 🤗 ✅ \n\n')


# EOF
