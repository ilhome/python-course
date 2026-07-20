def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }

run_cases = [
    (
        "bloodwarrior123",
        "server1",
        5,
        1,
        {
            "name": "bloodwarrior123",
            "server": "server1",
            "level": 5,
            "rank": 1,
            "id": "bloodwarrior123#server1",
        },
    ),
    (
        "fronzenboi",
        "server2",
        2,
        1,
        {
            "name": "fronzenboi",
            "server": "server2",
            "level": 2,
            "rank": 1,
            "id": "fronzenboi#server2",
        },
    ),
]

submit_cases = run_cases + [
    (
        "slasher69",
        "server3",
        2,
        5,
        {
            "name": "slasher69",
            "server": "server3",
            "level": 2,
            "rank": 5,
            "id": "slasher69#server3",
        },
    ),
    (
        "icequeen",
        "server4",
        3,
        2,
        {
            "name": "icequeen",
            "server": "server4",
            "level": 3,
            "rank": 2,
            "id": "icequeen#server4",
        },
    ),
    (
        "shadowmaster",
        "server5",
        4,
        3,
        {
            "name": "shadowmaster",
            "server": "server5",
            "level": 4,
            "rank": 3,
            "id": "shadowmaster#server5",
        },
    ),
    (
        "silentslasher",
        "server6",
        5,
        4,
        {
            "name": "silentslasher",
            "server": "server6",
            "level": 5,
            "rank": 4,
            "id": "silentslasher#server6",
        },
    ),
    (
        "hypershadow",
        "server7",
        3,
        5,
        {
            "name": "hypershadow",
            "server": "server7",
            "level": 3,
            "rank": 5,
            "id": "hypershadow#server7",
        },
    ),
]


def test(name, server, level, rank, expected_output):
    try:
        result = get_character_record(name, server, level, rank)
        for key, expected in expected_output.items():
            actual = result[key]
            print(f"Expected: {key}: {expected}")
            print(f"Actual:   {key}: {actual}\n")
            if actual != expected:
                if type(actual) is not type(expected):
                    print(
                        f"'{key}' values are different types! Expected {type(expected).__name__}, got {type(actual).__name__}"
                    )
                print("Fail")
                return False

        if result != expected_output:
            print("Result object is incorrect:")
            for key, value in result.items():
                print(f" * {key}: {value}")
            print("Fail")
            return False

        print("Pass")
        return True
    except Exception as exc:
        print(f"Exception: {exc}")
        print("Fail")
        return False


def main():
    passed = failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for index, test_case in enumerate(test_cases, start=1):
        print("---------------------------------")
        print(f"Test Case #{index}\n")
        if test(*test_case):
            passed += 1
        else:
            failed += 1

    print("============= PASS ==============" if failed == 0 else "============= FAIL ==============")
    if skipped:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = run_cases if "__RUN__" in globals() else submit_cases

if __name__ == "__main__":
    main()
