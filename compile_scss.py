import sass

def compile_scss(input_file, output_file):
    try:
        compiled_css = sass.compile(filename=input_file)

        with open(output_file, 'w') as f:
            f.write(compiled_css)

        print(f"Successfully compiled {input_file} to {output_file}")
    except Exception as e:
        print(f"Error compiling SCSS: {e}")


compile_scss('static/scss/style.scss', 'static/css/style.css')