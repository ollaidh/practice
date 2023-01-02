import argparse
import os
from pathlib import Path


class LengthChecker:
    def check(self, line: str) -> bool:
        return len(line) <= 79

    def error_number(self) -> str:
        return 'S001'

    def error_msg(self) -> str:
        return 'Too long'


class IdentFourChecker:
    def check(self, line: str) -> bool:
        ident = 0
        for letter in line:
            if letter == ' ':
                ident += 1
            else:
                break
        return ident % 4 == 0

    def error_number(self) -> str:
        return 'S002'

    def error_msg(self) -> str:
        return 'Indentation is not a multiple of four'


class UnnecSemicolonChecker:
    def check(self, line: str) -> bool:
        quoteopen = False
        for letter in line:
            if not quoteopen:
                if letter == '#':
                    break
                if letter == '\'':
                    quoteopen = True
                    pass
                if letter == ';':
                    return False
            else:
                if letter == '\'':
                    quoteopen = False
                    pass
        return True

    def error_number(self) -> str:
        return 'S003'

    def error_msg(self) -> str:
        return 'Unnecessary semicolon after a statement'


class TwoSpacesChecker:
    def check(self, line: str) -> bool:
        try:
            comment_index = line.index('#')
            if comment_index == 0:
                return True
            if comment_index < 2:
                return False
            if line[comment_index - 1] != ' ' or line[comment_index - 2] != ' ':
                return False
            return True
        except ValueError:
            pass
        return True

    def error_number(self) -> str:
        return 'S004'

    def error_msg(self) -> str:
        return 'Less than two spaces before inline comments'


class TodoChecker:
    def check(self, line: str) -> bool:
        try:
            comment_index = line.index('#')
            if 'TODO' in line[comment_index:len(line)].upper():
                return False
        except ValueError:
            pass
        return True

    def error_number(self) -> str:
        return 'S005'

    def error_msg(self) -> str:
        return 'TODO found'


class BlankLinesChecker:
    def __init__(self):
        self.counter = 0

    def check(self, line: str) -> bool:
        if line != '\n':
            counter, self.counter = self.counter, 0
            return counter <= 2
        self.counter = self.counter + 1
        return True

    def error_number(self) -> str:
        return 'S006'

    def error_msg(self) -> str:
        return 'More than two blank lines preceding a code line'


class Code:
    def check_file(self, file_name):
        with open(file_name, 'r') as file:
            checkers = [LengthChecker(),
                        IdentFourChecker(),
                        UnnecSemicolonChecker(),
                        TwoSpacesChecker(),
                        TodoChecker(),
                        BlankLinesChecker()]
            current_line = 1
            for line in file:
                for checker in checkers:
                    if not checker.check(line):
                        print(f"{file_name}: Line {current_line}: {checker.error_number()} {checker.error_msg()}")
                current_line += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src_path')
    args = parser.parse_args()
    src_path = args.src_path

    if Path(src_path).is_file():
        code = Code()
        code.check_file(src_path)
    else:
        code = Code()
        for file_name in os.listdir(src_path):
            if file_name == 'tests.py':  # ¯\_(ツ)_/¯ JB Academy
                continue
            if file_name.endswith(".py"):
                code.check_file(str(Path(src_path) / file_name))
