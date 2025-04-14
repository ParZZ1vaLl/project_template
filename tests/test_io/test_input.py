import pandas as pd
from app.io.input import read_file_python, read_file_pandas

class TestReadFilePython:

    def test_returns_string_if_file_exists(self, tmp_path):
        file_dir = tmp_path / "files"
        file_dir.mkdir()
        file_path = file_dir / "sample.txt"
        file_path.write_text("Sample content")

        result = read_file_python(str(file_path))

        assert isinstance(result, str)

    def test_returns_none_for_missing_file(self):
        missing_path = "nonexistent_file.txt"
        result = read_file_python(missing_path)

        assert result is None

    def test_reads_exact_file_content(self, tmp_path):
        expected_text = "Exact match content"
        file_dir = tmp_path / "texts"
        file_dir.mkdir()
        file_path = file_dir / "text.txt"
        file_path.write_text(expected_text)

        result = read_file_python(str(file_path))

        assert result == expected_text


class TestReadFilePandas:

    def test_returns_dataframe_if_file_exists(self, tmp_path):
        csv_dir = tmp_path / "csvs"
        csv_dir.mkdir()
        csv_file = csv_dir / "data.csv"
        csv_file.write_text("id,name\n1,Alice\n2,Bob")

        result = read_file_pandas(str(csv_file))

        assert isinstance(result, pd.DataFrame)

    def test_returns_none_if_csv_file_missing(self):
        fake_path = "missing.csv"
        result = read_file_pandas(fake_path)

        assert result is None

    def test_correct_dataframe_content(self, tmp_path):
        expected_df = pd.DataFrame({
            "col1": ["a", "b", "c"],
            "col2": [10, 20, 30]
        })

        output_dir = tmp_path / "dataframes"
        output_dir.mkdir()
        file_path = output_dir / "frame.csv"
        expected_df.to_csv(file_path, index=False)

        result_df = read_file_pandas(str(file_path))

        assert expected_df.equals(result_df)