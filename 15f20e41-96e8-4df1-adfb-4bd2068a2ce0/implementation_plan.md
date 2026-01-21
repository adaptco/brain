# Dockerize ADK CLI Implementation Plan

## Goal Description

The goal is to containerize the ADK CLI tools so they can be run reliably in any environment via Docker. This involves creating a `Dockerfile` and a shell script wrapper to build and run the container.

## User Review Required
>
> [!NOTE]
> The Docker image will be built securely from the local source. The wrapper script assumes Docker is installed and running.
> I will create a separate `requirements-cli.txt` to avoid installing heavy dependencies like `torch` which are not needed for the CLI.

## Proposed Changes

### ADK Core (`antigravity/implicit`)

#### [NEW] [Dockerfile](file:///c:/Users/eqhsp/.gemini/antigravity/implicit/Dockerfile)

- Base image: `python:3.11-slim`
- Installs dependencies from new `requirements-cli.txt`
- Copies source code (`cli` package)
- Sets entrypoint to the ADK CLI python module

#### [NEW] [requirements-cli.txt](file:///c:/Users/eqhsp/.gemini/antigravity/implicit/requirements-cli.txt)

- `PyYAML`
- `jsonschema`

#### [NEW] [docker_adk.sh](file:///c:/Users/eqhsp/.gemini/antigravity/implicit/docker_adk.sh)

- Shell script to build the image (if needed) and run the container.
- Mounts the current working directory to `/workspace` in the container.
- Forward arguments to the ADK CLI.

## Verification Plan

### Automated Tests

- Run `./docker_adk.sh --help` to verify the container runs and help is displayed.
- Run `./docker_adk.sh validate .` in a directory with known valid/invalid artifacts to verify functionality.
