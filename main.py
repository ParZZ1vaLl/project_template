from app.io.input import input_console, read_file_python, read_file_pandas
from app.io.output import output_console, write_file_python, write_file_pandas


def main():
    inp_cons = input_console()
    file_to_read = "data/read_file.csv"
    data_py = read_file_python(file_to_read)
    data_pd = read_file_pandas(file_to_read)

    output_console(inp_cons)
    output_console(data_py)
    output_console(data_pd)
    file_to_write = "data/write_file.txt"
    write_file_python(file_to_write, inp_cons)
    write_file_python(file_to_write, data_py)
    write_file_python(file_to_write, data_pd.to_string())
    write_file_pandas("data/write_file.csv", data_pd)


if __name__ == '__main__':
    main()