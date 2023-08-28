from subprocess import Popen, PIPE

def test_add_task():
    process = Popen(["./jafr.sh", "add", "Finish project proposal", "2023-09-10"], stdout=PIPE, text=True)
    output = process.communicate()[0]
    assert "Task added" in output

# More test functions for other commands...

if __name__ == "__main__":
    test_add_task()
    # Call other test functions here
