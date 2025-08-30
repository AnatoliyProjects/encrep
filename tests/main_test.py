# Encrep
# MIT license
# Copyright © 2025 Anatoly Petrov (petrov.projects@gmail.com)
# All rights reserved

"""Encrep unittest."""

# pylint: disable=import-error,missing-function-docstring,too-many-statements

import datetime
import os
import pathlib
import subprocess
import tempfile
import uuid

from moto import mock_aws  # type: ignore
from typer.testing import CliRunner

from encrep import app, ExclusionRule, Secrets


runner = CliRunner()


class TestEncrepCommands:
    """Test Encrep commands."""

    def test_setup_and_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_row:
            # 1) Paths
            tmp = pathlib.Path(tmp_row)
            keys = tmp / "encrep-secrets.json"
            git = tmp / ".git"
            gitignore = tmp / ".gitignore"
            git.mkdir()

            # 2) Default location
            res = runner.invoke(app, ["loc"])
            assert res.exit_code == 0
            assert "encrep-secrets.json" in res.output

            # 3) First try
            cin = [
                "AKIAIOSFODNN7EXAMPLE",
                "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "us-east-1",
                "encreptest",
                "y",
                "y",
                "suffix",
                "teststr",
                "n",
                "y",
            ]
            res = runner.invoke(
                app,
                ["setup", "--keys", str(keys)],
                "\n".join(cin),
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0
            assert keys.exists()
            secrets = Secrets.from_file(keys)
            assert secrets.aws_access_key_id == "AKIAIOSFODNN7EXAMPLE"
            assert (
                secrets.aws_secret_access_key
                == "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
            )
            assert secrets.encrep_secret_key is not None
            assert secrets.region == "us-east-1"
            assert secrets.bucket == "encreptest"
            assert secrets.excluded == [
                ExclusionRule(
                    pattern="encrep-secrets",
                    comp="prefix",
                ),
                ExclusionRule(pattern="teststr", comp="suffix"),
            ]

            # 4) Retry
            cin = [
                "y",
                "y",
                "AKIAIOSFODNN7EXAMPLE",
                "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "us-east-1",
                "encreptest",
                "y",
                "y",
                "suffix",
                "teststr",
                "n",
                "y",
            ]
            res = runner.invoke(
                app,
                ["setup", "--keys", str(keys)],
                "\n".join(cin),
                catch_exceptions=False,
            )
            assert res.exit_code == 0
            assert any(s.name.startswith("encrep-secrets from") for s in tmp.iterdir())

            # 5) Cleanup
            res = runner.invoke(
                app,
                ["cleanup", "--keys", str(keys)],
                "\n".join(cin),
                catch_exceptions=False,
            )
            assert res.exit_code == 0
            assert not keys.exists()

            # 6) Gitignore
            with open(gitignore, "rt", encoding="utf-8") as f:
                buf = f.read()
            assert "encrep-secrets.json" in buf
            assert any(s.startswith("encrep-secrets from") for s in buf.splitlines())

    @mock_aws
    def test_core(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_row:
            # 1) Paths
            tmp = pathlib.Path(tmp_row)
            keys = tmp / "encrep-secrets.json"
            name = uuid.uuid4().hex
            repo = tmp / name
            restored = tmp / (name + "-restored")
            ver = repo / "versioned.txt"
            unver = repo / "unversioned.txt"
            gitignore = repo / ".gitignore"

            # 2) Keys
            cin = [
                "AKIAIOSFODNN7EXAMPLE",
                "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "us-east-1",
                "encreptest",
                "y",
                "n",
            ]
            runner.invoke(
                app,
                ["setup", "--keys", str(keys)],
                "\n".join(cin),
                catch_exceptions=False,
            )

            # 3) Mocked repo
            repo.mkdir()
            with open(ver, "wt+", encoding="utf-8") as f:
                f.write("Hello versioned world!")
            with open(unver, "wt+", encoding="utf-8") as f:
                f.write("Hello unversioned world!")
            with open(gitignore, "wt+", encoding="utf-8") as f:
                f.write("unversioned.txt")
            subprocess.run(["git", "init"], cwd=repo, check=True)
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "Init commit"], cwd=repo, check=True)
            os.chdir(repo)

            # 4) Dump (repo + misc)
            cin = "y"  # create bucket?
            res = runner.invoke(
                app,
                ["dump", "project", "--src", str(repo), "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0

            # 5) Tree bucket
            res = runner.invoke(
                app,
                ["tree", "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0
            assert name in res.output

            # 6) List projects
            res = runner.invoke(
                app,
                ["ls", "project", "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0
            assert name in res.output

            # 7) List repo
            res = runner.invoke(
                app,
                ["ls", "repo", "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0
            assert name in res.output

            # 8) List misc
            res = runner.invoke(
                app,
                ["ls", "misc", "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0
            assert name in res.output

            # 9) Restore (repo + misc)
            cin = "y"  # Dir is not empty. Do you want to continue?
            res = runner.invoke(
                app,
                ["restore", "project", "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0
            with open(restored / "versioned.txt", "rt", encoding="utf-8") as f:
                buf = f.read()
            assert buf == "Hello versioned world!"
            with open(restored / "unversioned.txt", "rt", encoding="utf-8") as f:
                buf = f.read()
            assert buf == "Hello unversioned world!"

            # 10) Remove (repo only)
            cin = "y"  # Do you want to delete these files?
            res = runner.invoke(
                app,
                ["rm", "repo", "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0

            # 11) Drop (misc only)
            cin = "y"  # Do you want to delete these files?
            today = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d")
            res = runner.invoke(
                app,
                ["drop", "misc", "--start", today, "--end", today, "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 0

            # 12) List projects
            res = runner.invoke(
                app,
                ["ls", "project", "--keys", str(keys)],
                input=cin,
                catch_exceptions=False,
            )
            print(res.output)
            assert res.exit_code == 20
            assert "No objects found." in res.output
