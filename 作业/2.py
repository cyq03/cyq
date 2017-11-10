＃！/ usr / bin / python
导入重新

行=  “猫比狗聪明”

searchObj = re.search（r '（。*？）。* smarter（。*？）。* '，line，re.M | re.I）

如果 searchObj：
    print（“ searchObj.group（）：”，searchObj.group（））
    print（“ searchObj.group（1）：”，searchObj.group（1））
    print（“ searchObj.group（2）：”，searchObj.group（2））
其他：
    打印（“没有发现!! ”）
