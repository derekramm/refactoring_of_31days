#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""


# 分解复杂判断
# 今天的重构基于 c2 的 wiki 条目。
# Los Techies 的 Chris Missal 同样也些了一篇关于反模式的 post。
# 简单地说，当你使用大量的嵌套条件判断时，形成了箭头型的代码，这就是箭头反模式(arrowhead antipattern)。
# 我经常在不同的代码库中看到这种现象，这提高了代码的圈复杂度(cyclomatic complexity)。
# 下面的例子演示了箭头反模式:

class Security:
    def __init__(self, i_security_checker):
        self.i_security_checker = i_security_checker

    def has_access(self, user, permission, exemptions):
        has_permission = False
        if user is not None:
            if permission is not None:
                if len(exemptions) > 0:
                    if self.i_security_checker.check_permission(user, permission) or (permission in exemptions):
                        has_permission = True
        return has_permission


# 移除箭头反模式的重构和封装条件判断一样简单。
# 这种方式的重构在方法执行之前往往会评估各个条件， 这有点类似于契约式设计验证。
# 下面是重构之后的代码：

class Security:
    def __init__(self, i_security_checker):
        self.i_security_checker = i_security_checker

    def has_access(self, user, permission, exemptions):
        if (user is None) or (permission is None):
            return False
        if permission in exemptions:
            return True
        return self.i_security_checker.check_permission(user, permission)

# 如你所见，该方法大大整价了可读性和以后的可维护性。不难看出，该方法的所有可能的路径都会经过验证。
