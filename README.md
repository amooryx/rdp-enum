<div align="center">
  <img src="./banner.svg" alt="rdp-enum" width="800">
</div>

# rdp-enum

> RDP exposure, NLA, and security-layer enumeration

Part of a red-team tooling collection for **authorised** security testing.

## Install

```bash
git clone https://github.com/amooryx/rdp-enum.git
cd rdp-enum
```

## Usage

```bash
python rdp_enum.py <target>
```

| Flag | Description |
|---|---|
| `-o, --output` | Write the report to a file instead of standard output |
| `-v, --verbose` | Verbose output |
| `-y, --yes` | Skip the authorisation prompt |

The current implementation is a scaffold: it reports the supplied target and
states that no target checks were performed. It does not make network
connections. If the output file cannot be written, the command prints an error
and exits with status 2.

## Disclaimer

> **Authorised security testing only.** Use this against systems you own or have
> explicit written permission to test. The tool prompts for authorisation before
> acting and is provided for professional engagements, labs, and research.

## Author

**Omar Khalid** — [omareldemery.com](https://omareldemery.com) | [@amooryx](https://github.com/amooryx)

Certifications: OSCP+ · OSCP · CRTP · eWPTX · eCPPT · eCDFP · eCIR · eJPT
