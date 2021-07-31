from flask import render_template


def gen_html_error(code: int, desc: str):
    code_names = {"400": "Bad Request", "415": "Unsupported Media Type", "404": "Not Found"}

    name = code_names[str(code)]
    return render_template(
        "error.html", error_code=code, error_name=name, error_desc=desc
    ), code
