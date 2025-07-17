import pytest,webbrowser,os,time,sys


def main(suite_name=None):
    # Base pytest arguments
    pytest_args = [
        "tests",
        "-v",
        "--tb=short",
        "--html=report.html",
        "--self-contained-html"
    ]

    # If a suite is specified, add the marker
    if suite_name and suite_name.lower() != "all":
        print(suite_name)
        pytest_args += ["-m", suite_name]

    pytest.main(pytest_args)
    report_path = os.path.abspath("report.html")
    webbrowser.open("file://" + report_path)


if __name__ == "__main__":
    # Get suite name from command line, default to "all"
    selected_suite = sys.argv[1] if len(sys.argv) > 1 else "all"

    while True:
        main(selected_suite)  # run all testcases
        # main("smoke")   #run only sepcific testcase
        time.sleep(120)  # Repeat every 2 minutes