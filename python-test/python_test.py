import json
import random
import pytest


class TestClass:
    # Parameterized pytest
    # with open('data.txt', 'r') as file:
    #     data = json.loads(file.read())
    #
    # @pytest.mark.parametrize("args", data)
    # def test_method(self, args)
    def test_method(self, ) -> (dict, dict, dict, dict, ):
        # NOTE: Get all the parse commands
        with open('data.txt', 'r') as file:
            data = json.loads(file.read())
        parse_commands = []
        [parse_commands.append(row.copy()) for row in data if 'function' in row and row['function'] == 'parse']
        print(f"parse_commands: {parse_commands}")
        # NOTE: Get all the copy commands
        copy_commands = []
        [copy_commands.append(row.copy()) for row in data if 'function' in row and row['function'] == 'copy']
        print(f"copy_commands: {copy_commands}")
        # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
        functional_commands = []
        counter = 0
        for row in parse_commands:
            counter += 1
            new_row = row.copy()
            new_row['_list'] = 'parse'
            new_row['_counter'] = counter
            functional_commands.append(new_row)
        counter = 0
        for row in copy_commands:
            counter += 1
            new_row = row.copy()
            new_row['_list'] = 'copy'
            new_row['_counter'] = counter
            functional_commands.append(new_row)
        print(f"functional_commands: {functional_commands}")
        # NOTE: Get random sampling of data
        random_commands = []
        random_commands = random.sample(data, 2)
        print(f"random_commands: {random_commands}")
        return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    obj = TestClass()
    parse_commands, copy_commands, functional_commands, random_commands = obj.test_method()
    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
