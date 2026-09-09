import os
from pathlib import Path
import shutil

# Pfade
natural_images_dir = r"C:\Users\mat4b\PycharmProjects\IGMR_Dimonta\screw_detection\Datasets\igmr_artificial_dataset_v2\natural\images"
natural_labels_dir = r"C:\Users\mat4b\PycharmProjects\IGMR_Dimonta\screw_detection\Datasets\igmr_artificial_dataset_v2\natural\labels"
data_root = r"C:\Users\mat4b\PycharmProjects\IGMR_Dimonta\screw_detection\Datasets"

# Stelle sicher, dass labels Ordner existiert
os.makedirs(natural_labels_dir, exist_ok=True)

# Hole alle Image-Dateien
image_files = os.listdir(natural_images_dir)
print(f"Gefundene Images: {len(image_files)}")

# Für jede Image-Datei, finde die entsprechende Label-Datei
copied_count = 0
not_found_count = 0
not_found_files = []

for image_file in image_files:
    # Entferne die Dateiendung
    base_name = os.path.splitext(image_file)[0]
    
    # Suche die .txt Datei mit dem gleichen Namen in allen Daten-Unterordnern
    found = False
    
    # Durchsuche alle Ordner in data_root
    for root, dirs, files in os.walk(data_root):
        if "labels" in dirs or "labels/" in root:
            labels_folder = os.path.join(root, "labels") if "labels" in dirs else root
            txt_file = os.path.join(labels_folder, f"{base_name}.txt")
            
            if os.path.exists(txt_file):
                print(f"✓ Gefunden: {txt_file}")
                dest_path = os.path.join(natural_labels_dir, f"{base_name}.txt")
                shutil.copy2(txt_file, dest_path)
                copied_count += 1
                found = True
                break
    
    if not found:
        not_found_count += 1
        not_found_files.append(base_name)
        print(f"✗ Nicht gefunden: {base_name}")

print(f"\n--- Zusammenfassung ---")
print(f"Kopiert: {copied_count}")
print(f"Nicht gefunden: {not_found_count}")

if not_found_files:
    print(f"\nDateien ohne Label-Entsprechung:")
    for f in not_found_files[:10]:  # Zeige erste 10
        print(f"  - {f}")
    if len(not_found_files) > 10:
        print(f"  ... und {len(not_found_files) - 10} weitere")
