import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import rdp_enum


class RunTests(unittest.TestCase):
    def test_report_is_written_to_stdout_by_default(self):
        stdout = io.StringIO()
        args = SimpleNamespace(target="rdp.example", output=None)

        with contextlib.redirect_stdout(stdout):
            result = rdp_enum.run(args)

        self.assertEqual(result, 0)
        self.assertIn("[*] target : rdp.example", stdout.getvalue())
        self.assertIn("no target checks were performed", stdout.getvalue())

    def test_report_is_written_to_requested_file(self):
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "report.txt"
            stdout = io.StringIO()
            args = SimpleNamespace(target="192.0.2.10", output=str(output_path))

            with contextlib.redirect_stdout(stdout):
                result = rdp_enum.run(args)

            report = output_path.read_text(encoding="utf-8")
            self.assertEqual(result, 0)
            self.assertEqual(stdout.getvalue(), "")
            self.assertIn("[*] target : 192.0.2.10", report)
            self.assertIn("no target checks were performed", report)

    def test_output_write_error_is_reported_with_nonzero_status(self):
        with tempfile.TemporaryDirectory() as directory:
            stderr = io.StringIO()

            with contextlib.redirect_stderr(stderr):
                result = rdp_enum.main(["rdp.example", "-y", "-o", directory])

        self.assertEqual(result, 2)
        self.assertIn("could not write report", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
