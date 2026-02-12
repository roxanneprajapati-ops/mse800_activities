import os
import sys
import subprocess

def main():
    cv_file = os.getenv("BATCH_CV_FILE", "/app/inputs/resume-sample.pdf")
    out_file = os.getenv("BATCH_OUT_FILE", "/app/output/result.txt")

    # Run main.py in non-interactive mode
    cmd = ["python", "main.py", "--file", cv_file, "--out", out_file]
    print("Running batch:", " ".join(cmd))
    result = subprocess.run(cmd)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
