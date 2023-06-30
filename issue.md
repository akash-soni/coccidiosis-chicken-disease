## Issuse encountered while downloading VGG16

Solution:

    Update your SSL certificates:
        For Windows: You can download the latest SSL certificates from the official website at https://curl.se/ca/cacert.pem. Save the file to a location on your computer.
        For macOS: Update your macOS system to the latest version, which should include the latest SSL certificates.

    Set the SSL certificate path:
        For Windows: Open the command prompt and set the SSL_CERT_FILE environment variable to the path where you saved the downloaded SSL certificates file. For example, set SSL_CERT_FILE=C:\path\to\cacert.pem.
        For macOS: Open Terminal and set the SSL_CERT_FILE environment variable by running the following command: export SSL_CERT_FILE=/path/to/cacert.pem.

    Retry downloading the VGG16 model.
