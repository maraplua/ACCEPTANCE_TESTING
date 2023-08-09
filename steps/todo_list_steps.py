from behave import *

from todo_list import ToDoListManager

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoListManager()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert any(task.name == t.name for t in context.todo_list.tasks)

# Implement the remaining step definitions for other scenarios
