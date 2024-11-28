# youtube-dl-python
# YouTube Video Downloader

This project is a YouTube video downloader using `yt_dlp` for extracting and downloading video formats. It allows you to download videos individually or in bulk through a text file.

## Requirements

- Python 3.x
- `yt_dlp` library
- AV1 codec

## Installation

1. Clone this repository.
2. Install the required dependencies:
    ```bash
    pip install yt_dlp
    ```

## Usage

1. Run the script:
    ```bash
    python youtube-dl.py
    ```

2. Choose your mode:
    - Enter video URLs one by one.
    - Provide a text file containing multiple video URLs.

## Functionalities

- **Download Individual Videos**: 
  You can enter the URL of a YouTube video and choose the desired format from the available options.
- **Download Playlist from File**:
  You can provide a text file containing multiple YouTube video URLs, and the script will download each video in the chosen format.
- **Choose Video Quality**:
  For each video or playlist, you can select the desired video quality from the available formats.

## Example

### Download Individual Video

1. Run the script:
    ```bash
    python youtube-dl.py
    ```
2. Choose the mode:
    ```plaintext
    Voulez-vous entrer les liens un par un (1) ou via un fichier texte (2) ?
    ```
    Enter `1`.
3. Enter the video URL:
    ```plaintext
    Entrez l'URL de la vidéo YouTube :
    ```
4. Choose the format:
    ```plaintext
    Choisissez le format (1-XX):
    ```
5. The video will be downloaded to the `videos` directory.

### Download Playlist from File

1. Prepare a text file (e.g., `videos.txt`) with one YouTube URL per line.
2. Run the script:
    ```bash
    python youtube-dl.py
    ```
3. Choose the mode:
    ```plaintext
    Voulez-vous entrer les liens un par un (1) ou via un fichier texte (2) ?
    ```
    Enter `2`.
4. Enter the file path:
    ```plaintext
    Entrez le chemin du fichier texte contenant les URL des vidéos :
    ```
5. Choose the format for each video.
6. The videos will be downloaded to the `videos` directory.

## AV1 Codec

This script uses the AV1 codec for better video quality and compression. Make sure you have the AV1 codec installed on your system.

## Troubleshooting

- **Permission Errors**: Ensure you have write permissions to the `videos` directory.
- **Invalid URL**: Ensure the provided URLs are valid YouTube video links.

## Contact

If you have any questions or suggestions, please feel free to contact me at [zeleo789789@gmail.com](mailto:zeleo789789@gmail.com)

## License

Please just don't steal my code...