from gendiff.gendiff import generate_diff

def test_gendiff():
    answer = generate_diff("files/file1.json", "files/file2.json")
    with open("tests/fixtures/correct_answer.txt", "r") as test_file:
        correct_answer = test_file.read()
        # correct_answer = "{\n- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n}"
        assert answer == correct_answer
        test_file.close()