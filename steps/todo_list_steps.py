from behave import *
from todo_list import ToDoListManager

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoListManager()

@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo_list = ToDoListManager()
    for row in context.table:
        task_name = row['Task']
        context.todo_list.add_task(task_name)

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo_list.add_task(task)

@when("the user lists all tasks")
def step_impl(context):
    # Captura la salida real y almacénala en context.list_output
    from io import StringIO
    import sys

    original_stdout = sys.stdout
    sys.stdout = StringIO()
    context.todo_list.list_tasks()
    sys.stdout.seek(0)
    context.list_output = sys.stdout.read()
    sys.stdout = original_stdout
    
@then("the expected output should be")
def step_impl(context):
    expected_output = context.text.splitlines()
    actual_output = context.list_output.splitlines()

    for expected_line in expected_output:
        assert expected_line.strip() in actual_output

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.todo_list.mark_task_completed(task)

@when('the user removes task "{task}"')
def step_impl(context, task):
    context.todo_list.remove_task(task)

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_tasks()

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert any(task_obj.name == task for task_obj in context.todo_list.tasks)

@then('the output should contain')
def step_impl(context):
    expected_output = context.text.strip()
    assert expected_output in context.list_output

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    assert all(task_obj.name != task for task_obj in context.todo_list.tasks)


@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoListManager()
    context.todo_list.add_task("Buy groceries")
    context.todo_list.add_task("Pay bills")
    
@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    task_found = any(task_obj.name == task and task_obj.status == "Completed" for task_obj in context.todo_list.tasks)
    assert task_found


@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0
