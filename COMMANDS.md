# `encrep`

Encrep

CLI tool for dumping and restoring Git repos via AWS S3.
Encryption, easy management, and pretty printing.

**Usage**:

```console
$ encrep [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-v, --version`: Print a current version.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `setup`: Set up secrets, AWS region, and bucket name.
* `cleanup`: Remove the secrets file.
* `loc`: Show path to secrets file.
* `tree`: Display the structure of the AWS S3 bucket...
* `ls`: List the repos available from AWS S3.
* `dump`: Dump a repo to AWS S3.
* `restore`: Restore a repo from AWS S3.
* `rm`: Remove a single repo backup from AWS S3...
* `drop`: Delete multiple repo backups from AWS S3...

## `encrep setup`

Set up secrets, AWS region, and bucket name.

**Usage**:

```console
$ encrep setup [OPTIONS]
```

**Options**:

* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

## `encrep cleanup`

Remove the secrets file.

**Usage**:

```console
$ encrep cleanup [OPTIONS]
```

**Options**:

* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

## `encrep loc`

Show path to secrets file.

**Usage**:

```console
$ encrep loc [OPTIONS]
```

**Options**:

* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

## `encrep tree`

Display the structure of the AWS S3 bucket specified in the secrets file.

**Usage**:

```console
$ encrep tree [OPTIONS]
```

**Options**:

* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

## `encrep ls`

List the repos available from AWS S3.

**Usage**:

```console
$ encrep ls [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `project`: List all projects available from AWS S3.
* `repo`: List all bundles for a given repo...
* `misc`: List all misc archives for a given repo...

### `encrep ls project`

List all projects available from AWS S3.

**Usage**:

```console
$ encrep ls project [OPTIONS]
```

**Options**:

* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep ls repo`

List all bundles for a given repo available from AWS S3.

**Usage**:

```console
$ encrep ls repo [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep ls misc`

List all misc archives for a given repo available from AWS S3.

Misc archives contain files excluded from version control.

**Usage**:

```console
$ encrep ls misc [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

## `encrep dump`

Dump a repo to AWS S3.

**Usage**:

```console
$ encrep dump [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `project`: Invoke dump repo + dump misc with the same...
* `repo`: Bundle a given Git repo, encrypt it, and...
* `misc`: Create a misc archive for a given repo,...

### `encrep dump project`

Invoke dump repo + dump misc with the same arguments.

**Usage**:

```console
$ encrep dump project [OPTIONS]
```

**Options**:

* `-s, --src DIRECTORY`: Path to existing Git repo (cwd by default).  [env var: ENCREP_SRC]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep dump repo`

Bundle a given Git repo, encrypt it, and send to AWS S3.

**Usage**:

```console
$ encrep dump repo [OPTIONS]
```

**Options**:

* `-s, --src DIRECTORY`: Path to existing Git repo (cwd by default).  [env var: ENCREP_SRC]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep dump misc`

Create a misc archive for a given repo, encrypt it, and send to AWS S3.

Misc archives contain files excluded from version control.

**Usage**:

```console
$ encrep dump misc [OPTIONS]
```

**Options**:

* `-s, --src DIRECTORY`: Path to existing Git repo (cwd by default).  [env var: ENCREP_SRC]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

## `encrep restore`

Restore a repo from AWS S3.

**Usage**:

```console
$ encrep restore [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `project`: Invoke restore repo + restore misc with...
* `repo`: Download a Git bundle from AWS S3, decrypt...
* `misc`: Download the misc archive from AWS S3,...

### `encrep restore project`

Invoke restore repo + restore misc with the same arguments.

**Usage**:

```console
$ encrep restore project [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-d, --date [%Y-%m-%d]`: Creation date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_DATE]
* `-d, --dest DIRECTORY`: Path to restored repo (cwd.parent / cwd.name-restored by default).  [env var: ENCREP_DEST]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep restore repo`

Download a Git bundle from AWS S3, decrypt it, and clone to a given directory.

**Usage**:

```console
$ encrep restore repo [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-d, --date [%Y-%m-%d]`: Creation date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_DATE]
* `-d, --dest DIRECTORY`: Path to restored repo (cwd.parent / cwd.name-restored by default).  [env var: ENCREP_DEST]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep restore misc`

Download the misc archive from AWS S3, decrypt it, and unarchive into a given directory.

Misc archives contain files excluded from version control.

**Usage**:

```console
$ encrep restore misc [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-d, --date [%Y-%m-%d]`: Creation date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_DATE]
* `-d, --dest DIRECTORY`: Path to restored repo (cwd.parent / cwd.name-restored by default).  [env var: ENCREP_DEST]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

## `encrep rm`

Remove a single repo backup from AWS S3 for the specified date.

**Usage**:

```console
$ encrep rm [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `project`: Invoke rm repo + rm misc with the same...
* `repo`: Delete a single repo bundle from AWS S3.
* `misc`: Delete a single misc archive from AWS S3.

### `encrep rm project`

Invoke rm repo + rm misc with the same arguments.

**Usage**:

```console
$ encrep rm project [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-d, --date [%Y-%m-%d]`: Creation date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_DATE]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep rm repo`

Delete a single repo bundle from AWS S3.

**Usage**:

```console
$ encrep rm repo [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-d, --date [%Y-%m-%d]`: Creation date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_DATE]
* `-f, --force`: Don&#x27;t ask before file deletion.
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep rm misc`

Delete a single misc archive from AWS S3.

Misc archives contain files excluded from version control.

**Usage**:

```console
$ encrep rm misc [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-d, --date [%Y-%m-%d]`: Creation date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_DATE]
* `-f, --force`: Don&#x27;t ask before file deletion.
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

## `encrep drop`

Delete multiple repo backups from AWS S3 within a specified date range.

**Usage**:

```console
$ encrep drop [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `project`: Invoke drop repo + drop misc with the same...
* `repo`: Delete all repo bundles within a given...
* `misc`: Delete all misc archives within a given...

### `encrep drop project`

Invoke drop repo + drop misc with the same arguments.

**Usage**:

```console
$ encrep drop project [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-s, --start [%Y-%m-%d]`: Start date for a Git bundle or misc archive (earliest by default).  [env var: ENCREP_START; default: 0001-01-01 00:00:00]
* `-e, --end [%Y-%m-%d]`: End date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_END; default: 9999-12-31 00:00:00]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep drop repo`

Delete all repo bundles within a given date range from AWS S3.

**Usage**:

```console
$ encrep drop repo [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-s, --start [%Y-%m-%d]`: Start date for a Git bundle or misc archive (earliest by default).  [env var: ENCREP_START; default: 0001-01-01 00:00:00]
* `-e, --end [%Y-%m-%d]`: End date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_END; default: 9999-12-31 00:00:00]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.

### `encrep drop misc`

Delete all misc archives within a given date range from AWS S3.

**Usage**:

```console
$ encrep drop misc [OPTIONS]
```

**Options**:

* `-n, --name TEXT`: Repo name (cwd.name by default).  [env var: ENCREP_NAME]
* `-s, --start [%Y-%m-%d]`: Start date for a Git bundle or misc archive (earliest by default).  [env var: ENCREP_START; default: 0001-01-01 00:00:00]
* `-e, --end [%Y-%m-%d]`: End date for a Git bundle or misc archive (latest by default).  [env var: ENCREP_END; default: 9999-12-31 00:00:00]
* `-k, --keys FILE`: Path to secrets file (app_dir / &#x27;encrep-secrets.json&#x27; by default).  [env var: ENCREP_KEYS]
* `--help`: Show this message and exit.
