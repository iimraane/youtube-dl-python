import yt_dlp
import os

def get_video_formats(url):
    # Extraire les formats disponibles de la vidéo
    ydl_opts = {
        'skip_download': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        return formats

def download_video(url, format_choice, download_dir='videos'):
    try:
        # Vérifier les permissions et créer le répertoire 'videos' s'il n'existe pas
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        if not os.access(download_dir, os.W_OK):
            raise PermissionError(f"Permission denied for directory: {download_dir}")

        # Options de téléchargement
        ydl_opts = {
            'format': format_choice,  # Sélection de la qualité choisie
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Où enregistrer la vidéo
        }

        # Téléchargement de la vidéo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Afficher l'endroit où la vidéo a été téléchargée
        print(f"La vidéo a été téléchargée dans : {os.path.abspath(os.path.join(download_dir, '%(title)s.%(ext)s'))}")

        print("Téléchargement terminé !")

    except Exception as e:
        print(f"Erreur lors du téléchargement : {e}")

def show_available_formats(url):
    formats = get_video_formats(url)
    print("Formats disponibles :")
    for i, f in enumerate(formats):
        format_info = f"{i + 1}. {f['format_id']} - {f['resolution'] if 'resolution' in f else 'audio only'} - {f['ext']} - {f['format_note'] if 'format_note' in f else ''}"
        print(format_info)

    return formats

def download_playlist(file_path, download_dir='videos'):
    try:
        # Vérifier les permissions et créer le répertoire 'videos' s'il n'existe pas
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        if not os.access(download_dir, os.W_OK):
            raise PermissionError(f"Permission denied for directory: {download_dir}")

        with open(file_path, 'r') as file:
            links = file.readlines()

        for url in links:
            url = url.strip()
            formats = get_video_formats(url)
            print(f"Téléchargement des formats pour {url}")

            # Demander à l'utilisateur de choisir un format pour chaque vidéo
            while True:
                try:
                    choice = int(input(f"Choisissez le format pour {url} (1-{len(formats)}): ")) - 1
                    if 0 <= choice < len(formats):
                        break
                    else:
                        print(f"Veuillez entrer un nombre entre 1 et {len(formats)}.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

            chosen_format = formats[choice]['format_id']
            download_video(url, chosen_format, download_dir)

    except Exception as e:
        print(f"Erreur lors du téléchargement de la playlist : {e}")

if __name__ == "__main__":
    while True:
        choix_mode = input("Voulez-vous entrer les liens un par un (1) ou via un fichier texte (2) ? ")

        if choix_mode == '1':
            video_url = input("Entrez l'URL de la vidéo YouTube : ")
            formats = show_available_formats(video_url)

            # Demander à l'utilisateur de choisir un format
            while True:
                try:
                    choice = int(input(f"Choisissez le format (1-{len(formats)}): ")) - 1
                    if 0 <= choice < len(formats):
                        break
                    else:
                        print(f"Veuillez entrer un nombre entre 1 et {len(formats)}.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

            chosen_format = formats[choice]['format_id']
            download_video(video_url, chosen_format)

        elif choix_mode == '2':
            download_dir = os.path.abspath('videos.txt')
            download_playlist(download_dir)

        else:
            print("Choix invalide. Veuillez choisir 1 ou 2.")

        another = input("Voulez-vous télécharger autre chose ? (oui/non) : ")
        if another.lower() != 'oui':
            break
