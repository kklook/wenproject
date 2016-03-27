# -*- coding:utf-8 -*-
import re

pattern=re.compile(r'^(.*)周\(?(单|双)?\)? 星期(一|二|三|四|五|六|日) (.*)节$')
result=re.search(pattern,'7-10周 星期四 3-4节')
print result.group(3)