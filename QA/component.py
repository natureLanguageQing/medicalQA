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


# 十味诃子丸的成分是什么
for i in drug_names.values.tolist():
    if "(" in i[0] or ")" in i[0]:
        continue
    question_drug = get_medical_name(i[0]+"的成分是什么")
    # 因为我并没有对话数据集，所以这个部分应该是一个分类模型去决策寻找哪个关系。
    print("下一个问题")
    print("question_drug", question_drug)
    answers_recall = instructions.loc[instructions["name"].str.contains(question_drug)]
    # print(answers_recall.count())
    # print("answers_recall.shape(0)", answers_recall.shape[0])
    print("question:", i[0]+"的成分是什么")
    if answers_recall.shape[0] == 0:
        print("without_answer：暂无相关数据，已经责令运营快速补充数据，请稍后哟！！")
    elif answers_recall.shape[0] == 1:
        print("answer:", question_drug, "的成分是", answers_recall["chengfen"].values.tolist()[0])
    elif answers_recall.shape[0] > 2:
        wait_choose = ""
        wait_chooses = answers_recall.name.values.tolist()
        for i in range(len(wait_chooses)):
            if i != len(wait_chooses)-1:
                wait_choose += wait_chooses[i] + "、"
            else:
                wait_choose += wait_chooses[i] + "。"
        print("exception_answer:", "名字包含", question_drug, "有", wait_choose, "请问你问的是哪一种？")
