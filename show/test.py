# -*- coding:utf-8 -*-
import re

pattern=re.compile(r'(.*)周\(?(单|双)?\)? 星期(一二|三|四|五|六|日) (.*)节')
result=re.search(pattern,'1-17周 星期二 7-8节')
print result.group(1)