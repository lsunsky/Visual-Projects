import pandas as pd

df = pd.read_csv("SHMetro/data/Coord-v3.1.csv")
line = {
    "1号线": ["富锦路", "友谊西路", "宝安公路", "共富新村", "呼兰路",
            "通河新村", "共康路", "彭浦新村", "汶水路", "上海马戏城",
            "延长路", "中山北路", "上海火车站", "汉中路", "新闸路",
            "人民广场", "黄陂南路", "陕西南路", "常熟路", "衡山路",
            "徐家汇", "上海体育馆", "漕宝路", "上海南站", "锦江乐园",
            "莲花路", "外环路", "莘庄"]
}

print(df[df.line == "1号线"])