from behave import *

from todo_list import ToDoListManager

@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo_list = ToDoListManager()
    for row in context.table:
        task_name = row['Task']
        context.todo_list.add_task(task_name)

@when('the user lists all tasks')
def step_impl(context):
    from io import StringIO
    import sys
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    context.todo_list.list_tasks()
    context.list_output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

@then('the output should contain:')
def step_impl(context):
    expected_output = context.text.strip()
    assert context.list_output == expected_output

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.todo_list.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for task_obj in context.todo_list.tasks:
        if task_obj.name == task:
            assert task_obj.status == 'Completed'
            break

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0

@when('the user removes task "{task}"')
def step_impl(context, task):
    context.todo_list.remove_task(task)

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    for task_obj in context.todo_list.tasks:
        assert task_obj.name != task
