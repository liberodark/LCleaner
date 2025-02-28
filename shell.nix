{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.pillow
    python3Packages.tkinter
  ];

  shellHook = ''
    echo "Run LCleaner"
    python lcleaner.py
  '';
}

