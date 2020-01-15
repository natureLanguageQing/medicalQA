from QA import instructions, drug_names


def get_medical_name(words: str):
    """
    最大匹配
    :param words:
    :return:
    """
    medical_name_recall = []
    for i in drug_names.values.tolist():
        if i[0] in words:
            medical_name_recall.append(i[0])
    index = 0
    answer = ""
    for i in medical_name_recall:
        if len(i) > index:
            answer = i
            index = len(i)
    return answer


# lc.loc[lc["grade"] == "B"].head()
var = instructions.loc[instructions["name"] == "同仁堂 锁阳固精丸 9g*10丸"]
# .str.contains(r'.*?n.*')
print(var)
var = instructions.loc[instructions["name"].str.contains(r'同仁堂')]
print(var)
# 十味诃子丸的成分是什么
question_drug = get_medical_name("十味诃子丸的成分是什么")
print("question_drug", question_drug)
answers_recall = instructions.loc[instructions["name"].str.contains(question_drug)]
print(answers_recall.count())
print("answers_recall.shape(0)", answers_recall.shape[0])
print("question:","十味诃子丸的成分是什么")
print("answer:", question_drug, "的成分是", answers_recall["chengfen"].values.tolist()[0])
