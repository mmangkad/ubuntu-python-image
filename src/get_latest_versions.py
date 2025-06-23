import json
import re
import requests
import sys
from bs4 import BeautifulSoup # A powerful library for parsing HTML

def get_latest_openssl():
    """
    Finds the latest stable OpenSSL version by parsing the GitHub releases page.
    It specifically looks for the release marked with the "Latest" label.
    """
    try:
        url = "https://github.com/openssl/openssl/releases"
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the green "Latest" label, which is unique to the latest stable release
        latest_label = soup.find("a", href="/openssl/openssl/releases/latest")
        if not latest_label:
            print("Error: Could not find the 'Latest' release label on the GitHub page.", file=sys.stderr)
            return None

        # Find the parent container of the release section that contains the label
        release_section = latest_label.find_parent("div", class_="d-flex")
        if not release_section:
            print("Error: Could not find the parent release section for the 'Latest' label.", file=sys.stderr)
            return None
        
        # Within that section, find the main link which contains the version number in its text
        version_link = release_section.find("a", href=re.compile(r"/openssl/openssl/releases/tag/openssl-"))
        if not version_link:
            print("Error: Could not find the version link within the 'Latest' release section.", file=sys.stderr)
            return None

        # Extract text like "OpenSSL 3.5.0" and clean it up to "3.5.0"
        version_text = version_link.text.replace("OpenSSL", "").strip()
        if re.match(r"^\d+\.\d+\.\d+[a-z]*$", version_text):
            return version_text

    except Exception as e:
        print(f"An unexpected error occurred while fetching the OpenSSL version: {e}", file=sys.stderr)
    
    return None

def get_latest_python_patch(minor_version):
    """Finds the latest patch number for a given Python minor version (e.g., 3.12)."""
    try:
        url = "https://www.python.org/downloads/source/"
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        pattern = re.compile(rf"Python {re.escape(minor_version)}\.(\d+)")
        matches = [int(p) for p in pattern.findall(response.text)]
        
        if matches:
            return f"{minor_version}.{max(matches)}"
        else:
            print(f"Error: No patch versions found for Python {minor_version}", file=sys.stderr)

    except Exception as e:
        print(f"An unexpected error occurred while fetching the Python {minor_version} version: {e}", file=sys.stderr)
        
    return None


if __name__ == "__main__":
    with open("versions.json", "r") as f:
        config = json.load(f)

    build_matrix = {"include": []}
    
    print("--- Starting Version Discovery ---", file=sys.stderr)
    latest_openssl = get_latest_openssl()
    
    if not latest_openssl:
        print("Fatal: Could not determine the latest OpenSSL version. Aborting.", file=sys.stderr)
        sys.exit(1) # Exit with an error code to fail the workflow
        
    print(f"Latest OpenSSL version found: {latest_openssl}", file=sys.stderr)

    for ubuntu in config["ubuntu_versions"]:
        for py_minor in config["python_versions"]:
            print(f"Searching for latest patch of Python {py_minor}...", file=sys.stderr)
            latest_python = get_latest_python_patch(py_minor)
            
            if not latest_python:
                print(f"Fatal: Could not determine latest patch for Python {py_minor}. Aborting.", file=sys.stderr)
                sys.exit(1) # Exit with an error code
                
            print(f"Latest Python {py_minor} version found: {latest_python}", file=sys.stderr)
            
            build_matrix["include"].append({
                "ubuntu_version": ubuntu,
                "python_version": latest_python,
                "openssl_version": latest_openssl,
            })

    # The final, clean JSON is the ONLY thing printed to standard output
    print(json.dumps(build_matrix))
