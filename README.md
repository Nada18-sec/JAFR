# JAFR
This is a basic  Python scripts that adds, lists and manages tasks and meetings. 

# Setup and Installation:
1. Install pytest for the tests to run;
    - 'pip install pytest'
    - Run 'pytest test_jafr.py' 
2. Make 'jafr.sh' executable using 'chmod +x jafr.sh'
3. Use the commands below to run jafr

# Jafr Behavior:
1. Adding a Task:
Users can add tasks with a description and a due date.
$ jafr add "Finish project proposal" 2023-09-10
Task added: Finish project proposal by 2023-09-10

2. Listing Tasks:
Users can list all tasks.
$ jafr list
1. [ ] Finish project proposal (2023-09-10)

3. Marking Tasks as Done:
Users can mark tasks as done.
$ jafr done 1
Marked task 1 as done.

4. Adding a Meeting:
Users can add meetings with a description and a date/time.
$ jafr meet "Team meeting" 2023-09-15 14:30
Meeting added: Team meeting on 2023-09-15 at 14:30

5. Listing Meetings:
Users can list all meetings.
$ jafr meet list
1. [ ] Team meeting (2023-09-15 at 14:30)
